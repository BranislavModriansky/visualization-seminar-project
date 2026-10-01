from typing import Optional
from pathlib import Path

import polars as pl

from warnings import warn


# Helper functions for processing kcat and km data
# -------------------------------------------------

def _drop_invalid_entries(dfs: list[pl.DataFrame], **kw):
    if kw.get("verbose", False):
        print("\n_drop_invalid_entries():")

    for i, df in enumerate(dfs):
        if kw.get("verbose", False):
            print(f"\nProcessing DataFrame {i}:")
            print(f"Shape of DataFrame {i} before cleaning: \n{df.shape}")

        dfs[i] = df.drop_nulls().unique()

        if kw.get("verbose", False):
            print(f"Shape of DataFrame {i} after cleaning (drop_nulls + unique): \n{dfs[i].shape}")

    return dfs

def _remove_columns(df, *, columns: list = None, right_from: Optional[str | int] = None, left_from: Optional[str | int] = None, **kw):

    if kw.get("verbose", False):
        print(f"\n_remove_columns():")
        print(f"Removing columns from the input DataFrame.")
        print(f"{len(df.columns)} columns in the input DataFrame: \n{df.columns}")

    if columns is not None:
        df = df.drop(columns)

    if right_from is not None:
        idx = df.get_column_index(right_from)
        df = df.drop(df.columns[idx:])

    if left_from is not None:
        idx = df.get_column_index(left_from)
        df = df.drop(df.columns[:idx])

    if columns is None and right_from is None and left_from is None:
        warn("No input to remove_columns() func. No columns removed.", category=UserWarning, stacklevel=2)

    if kw.get("verbose", False):
        print(f"{len(df.columns)} columns in the result DataFrame: \n{df.columns}")
    
    return df


def _get_shared_reactions(dfs: tuple[pl.DataFrame, pl.DataFrame], **kw):
    if kw.get("verbose", False):
        print(f"\n_get_shared_reactions():")

    if not dfs or len(dfs) != 2:
        raise ValueError("Expected a tuple of two DataFrames.")

    dfs = list(dfs)

    def _make_uid_str_column(dfs: list[pl.DataFrame]):
        for i, df in enumerate(dfs):
            if kw.get("verbose", False):
                print(f"Shape of DataFrame {i} before filtering: {df.shape}")

            dfs[i] = df.with_columns(
                (pl.col('uniprot') + '_' + pl.col('substrate_smiles')).alias('uid_str')
            ).filter(
                pl.col('uid_str').is_unique()
            )
        return dfs

    def _filter_to_shared_reactions(df, uids: list):
        return df.filter(
            pl.col('uid_str').is_in(uids)
        )

    def _assign_int_uid_column(dfs: list[pl.DataFrame]):
        for i, df in enumerate(dfs):
            if kw.get("verbose", False):
                print(f"Shape of DataFrame {i} after filtering to only shared entries: {df.shape}")
            
            dfs[i] = df.sort('uid_str').with_row_index('uid_int', offset=0)
        return dfs

    dfs = _make_uid_str_column(dfs)

    dfs[0] = _filter_to_shared_reactions(dfs[0], dfs[1].select('uid_str').to_series().to_list())
    dfs[1] = _filter_to_shared_reactions(dfs[1], dfs[0].select('uid_str').to_series().to_list())

    dfs = _assign_int_uid_column(dfs)

    return tuple(dfs)



# Load and categorize raw kcat and km CSVs
files = ['kcat_train.csv', 'kcat_test.csv', 'kcat_val.csv', 'km_train.csv', 'km_test.csv', 'km_val.csv']

kcat_files = [] 
km_files = []

for file in files:
    df = pl.read_csv(Path(__file__).parent / "cache/raw" / file)

    if file.startswith('kcat'):
        kcat_files.append(df)
    elif file.startswith('km'):
        km_files.append(df)


# Concatenate to get single kcat and km DataFrames with only unique and non-null rows
kcat_df = pl.concat(kcat_files)
km_df = pl.concat(km_files)

kcat_df, km_df = _drop_invalid_entries([kcat_df, km_df], verbose=True)

# Remove all (unnecessary) columns to the right of 'pdbpath'
kcat_df = _remove_columns(kcat_df, right_from='pdbpath', verbose = True)
km_df = _remove_columns(km_df, right_from='pdbpath', verbose = True)

# Rename 'reactant_smiles' column to 'substrate_smiles' in kcat DataFrame
kcat_df = kcat_df.rename({'reactant_smiles': 'substrate_smiles'})

# Get shared reactions between kcat and km DataFrames
kcat_df, km_df = _get_shared_reactions((kcat_df, km_df), verbose=True)

kcat_df.write_csv(Path(__file__).parent / "cache/processed/kcat_processed.csv")
km_df.write_csv(Path(__file__).parent / "cache/processed/km_processed.csv")
