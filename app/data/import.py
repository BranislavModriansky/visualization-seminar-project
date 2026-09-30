import polars as pl
from pathlib import Path

kcat_splits = {'train': 'kcat/kcat_train.csv', 'test': 'kcat/kcat_test.csv', 'val': 'kcat/kcat_val.csv'}
km_splits = {'train': 'km/km_train.csv', 'test': 'km/km_test.csv', 'val': 'km/km_val.csv'}

for csv in list(kcat_splits.values()) + list(km_splits.values()):
    df = pl.read_csv("hf://datasets/RosettaCommons/CatPred-DB/" + csv, schema_overrides={'temperature': pl.Float64})

    df.write_csv(Path(__file__).parent / "cache/raw/" / Path(csv).name)