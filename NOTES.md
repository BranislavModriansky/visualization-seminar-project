# PV251 Visualization **Seminar Project**


## References | Used Libraries | Tools

### Python Libraries:
* [Polars](https://docs.pola.rs/)


## I. Data source

Dataset used in this project: [CatPred-DB](https://huggingface.co/datasets/RosettaCommons/CatPred-DB) *...further description*

Kcat and Km datasets were downloaded including: 
- training (kcat_train, km_train);
- testing (kcat_test, km_test);
- evaluation (kcat_val, km_val).


## II. Data processing

1. Downloaded datasets were categorized and concatenated into single Kcat and Km DataFrames;

2. Columns not needed for intended analyses were removed from the result DataFrames;

3. All rows with missing values were removed;

4. Duplicate rows were removed;

5. Both datasets were reduced to shared entires;
    1. A unique id string (uid_str) merging the enzyme (uniprot id) + substrate strings was assigned to both datasets;
    2. Only the uid_str entries included in the both datasets were retained both in the Kcat and Km DataFrames;
    3. The uid_str values were matched with a newly created uid_int.

6. The result DataFrames were saved as CSVs
