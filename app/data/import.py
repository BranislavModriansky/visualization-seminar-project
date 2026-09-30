import polars as pl
from pathlib import Path

dkcat_df = pl.read_csv(r"hf://datasets/RosettaCommons/CatPred-DB/kcat/kcat_train.csv")
km_df = pl.read_csv(r"hf://datasets/RosettaCommons/CatPred-DB/km/km_train.csv")

dkcat_df.write_csv(Path(__file__).parent / "cache/raw/kcat_train.csv")
km_df.write_csv(Path(__file__).parent / "cache/raw/km_train.csv")
