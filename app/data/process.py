from pathlib import Path
import polars as pl

files = ['kcat_train.csv', 'kcat_test.csv', 'kcat_val.csv', 'km_train.csv', 'km_test.csv', 'km_val.csv']

kcat_files = [] 
km_files = []

for file in files:
    df = pl.read_csv(Path(__file__).parent / "cache/raw" / file)

    # print(key, files[key].head())

    if file.startswith('kcat'):
        kcat_files.append(df)
    elif file.startswith('km'):
        km_files.append(df)

kcat_df = pl.concat(kcat_files)
km_df = pl.concat(km_files)


def clean_data(df):

    idx = df.get_column_index('pdbpath')  # get the index of the 'pdbpath' column
    df = df.drop(df.columns[idx:]).drop_nulls()  # drop all columns from 'pdbpath' onwards and remove rows with null values

    return df

kcat_df = clean_data(kcat_df)
km_df = clean_data(km_df)


kcat_df = kcat_df.rename({'reactant_smiles': 'substrate_smiles'})


def shared_reaction_params(_kcat_df, _km_df, *, filter: bool = True):

    def add_uid_str_column(df):
        return df.with_columns(
            (pl.col('uniprot') + '_' + pl.col('substrate_smiles')).alias('uid_str')
        ).filter(
            pl.col('uid_str').is_unique()
        )

    _kcat_df = add_uid_str_column(_kcat_df)
    _km_df = add_uid_str_column(_km_df)

    if not filter:
        return _km_df, _kcat_df

    
    _km_df_shared = _km_df.filter(
        pl.col('uid_str').is_in(
            _kcat_df.select('uid_str').to_series().to_list()
        )
    )
    return _km_df_shared, _kcat_df.filter(
        pl.col('uid_str').is_in(
            _km_df_shared.select('uid_str').to_series().to_list()
        )
    )


kcat_df_shared, km_df_shared = shared_reaction_params(kcat_df, km_df)

kcat_df_shared.write_csv(Path(__file__).parent / "cache/processed/kcat_train_processed.csv")
km_df_shared.write_csv(Path(__file__).parent / "cache/processed/km_train_processed.csv")