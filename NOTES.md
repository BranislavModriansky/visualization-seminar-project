# PV251 Visualization **Seminar Project**


## References | Used Libraries | Tools

### Python Libraries:
* [Polars](https://docs.pola.rs/)
(versions yes/no?)

## I. Data source

Dataset used in this project: [CatPred-DB](https://huggingface.co/datasets/RosettaCommons/CatPred-DB) 
- Database of _in-vitro_ enzyme kinetic parameters for training, testing and validating enzyme kinetics predictor [CatPred](https://doi.org/10.1038/s41467-025-57215-9)
- Compilation and standardization of BREBDA and SABIO-RK
- Possible use of the database are for training and benchmarking new ml enzyme kinetic predictors, enzyme engineering, metabolic modeling etc.
- Our visualization is useful for exploration of possible candidates for enzyme engineering, by helping identify efficient enzymes, extremophiles or other outliers etc.


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
    2. Only the unique uid_str entries included in the both datasets were retained both in the Kcat and Km DataFrames;
    3. The uid_str values were matched with a newly created uid_int.

5. The result Kcat (2022, 16) and Km (2022, 13) DataFrames were saved as CSVs

## III. Further steps
- Calculating embeddings from enzyme sequences using esm2_t6_8m_ur50d (probably) → basic clustering based on biochemical, biophysical p and evolutionary relationships captured in embeddings through visualization using PCA and UMAP
- Querying Uniprot by uniprot id for enzyme names
- Calculating pI, GRAVY, molecular weight, aromacity based on sequence using biopython protparam → filtering through enzyme properties possible highlighting in PCA/UMAP for cluster characterization 
- segregation of enzymes by EC
- Visualization 

## IV. Possible steps
- chemoinformatics characterisation of substrates:
	- SMILES to name
	- basic properties molecular weight, log P, TPSA, categorization etc.
	- visualize substrate 2d structure
- enzyme charge under assay conditions
- TBA
