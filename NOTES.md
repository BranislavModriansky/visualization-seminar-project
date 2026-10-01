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

1. Downloaded datasets were categorized and concatenated into single Kcat (23151, 26) and Km DataFrames (41174, 23);

2. Duplicate rows and rows with missing values were removed - Kcat (19640, 26), Km (38615, 23);

3. Columns not needed for intended analyses were removed from the result DataFrames;

4. Both datasets were reduced to shared entires;
    1. A unique id string (uid_str) merging the enzyme (uniprot id) + substrate strings was assigned to both datasets;
    2. Only the uid_str entries included in the both datasets were retained both in the Kcat and Km DataFrames;
    3. The uid_str values were matched with a newly created uid_int.

5. The result Kcat (2022, 16) and Km (2022, 13) DataFrames were saved as CSVs
