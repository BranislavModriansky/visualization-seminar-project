from pathlib import Path
import polars as pl

kcat_df_raw = pl.read_csv(Path(__file__).parent / "cache/raw/kcat_train.csv")
km_df_raw = pl.read_csv(Path(__file__).parent / "cache/raw/km_train.csv")


def clean_data(df):

    idx = df.get_column_index('pdbpath')  # get the index of the 'pdbpath' column
    df = df.drop(df.columns[idx:]).drop_nulls()  # drop all columns from 'pdbpath' onwards and remove rows with null values

    return df

kcat_df = clean_data(kcat_df_raw)
km_df = clean_data(km_df_raw)


def shared_reaction_params(_kcat_df, _km_df):

    reaction_keys = {
        'uniprot_id': 'uniprot', 
        'kcat_substrate_str': 'reactant_smiles',
        'km_substrate_str': 'substrate_smiles'
    }

    unique_reactions = (
        pl.concat([
            _kcat_df.select(
                [reaction_keys['uniprot_id'], 
                 reaction_keys['kcat_substrate_str']]
            ).rename({reaction_keys['kcat_substrate_str']: 'smiles'}),
            _km_df.select(
                [reaction_keys['uniprot_id'], 
                 reaction_keys['km_substrate_str']]
            ).rename({reaction_keys['km_substrate_str']: 'smiles'})
        ]).unique().with_columns(
            reaction_id = pl.int_range(1, pl.len() + 1)
        )
    )

    _kcat_df = _kcat_df.join(
        unique_reactions.rename({'smiles': reaction_keys['kcat_substrate_str']}),
        on=[reaction_keys['uniprot_id'], reaction_keys['kcat_substrate_str']],
        how='left'
    )

    _km_df = _km_df.join(
        unique_reactions.rename({'smiles': reaction_keys['km_substrate_str']}),
        on=[reaction_keys['uniprot_id'], reaction_keys['km_substrate_str']],
        how='left'
    )

    return _kcat_df, _km_df


kcat_df_shared, km_df_shared = shared_reaction_params(kcat_df, km_df)

kcat_df_shared.write_csv(Path(__file__).parent / "cache/processed/kcat_train_shared.csv")
km_df_shared.write_csv(Path(__file__).parent / "cache/processed/km_train_shared.csv")