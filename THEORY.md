# THEORY 

## $k_{cat}$
- turnover number/catalytic constant 
- number of molecules of substrate transformed by single enzyme/single active site per unit of time given complete saturation and ideal conditions
- given hard to achieve/confirm conditions (total purity of enzyme, saturation etc.) experimental determination is noisy/unreliable
- units: $s^{-1}$ $(min^{-1})$
## $K_M$
- Michaelis constant 
- "affinity of enzyme for substrate"
- formal definition: _substrate concentration at which an enzyme-catalyzed reaction proceeds at half of its maximum velocity_
- ↓ $K_M$ high affinity enzyme bounds substrate well (the enzyme reaches half-maximal speed at lower substrate levels)
- ↑ $K_M$ low affinity weaker binding 
- units: molarity 

## $k_{cat}$/$K_M$
- specificity constant/kinetic efficiency
- efficiency of substrate conversion by enzyme 
- units: $s^{-1}M^{-1}$ 

## EC 
- enzyme classes four digit system identifying unique enzymes (example 1.1.1.1 alcohol dehydrogenase)
- type of reaction . subclass type of donor bond etc . sub-subclass specific cofactor electron acceptor etc . specific enzyme
- 7 main classes:
	- EC 1 oxidoreductases
	- EC 2 transferases
	- EC 3 hydrolases
	- EC 4 lyases 
	- EC 5 isomerases 
	- EC 6 ligases
	- EC 7 translocases 
## Embeddings
- converting enzyme sequence into a vector
- vector space of the embeddings captures structural, evolutionary relationships biophysical/biochemical properties of proteins
- similar proteins are closer in this space than less similar proteins irrespective of their sequential similarity 
- vector (embedding) represents position of said protein in this vector space allowing for performing algebraic operations to compare proteins etc. or used as one of strategies for ML biochemistry tools/predictors 

## esm2_t6_8m_ur50d
- Evolutionary scale model
- output vector with 320 dimentions 
- mostly capturing biochem/phys properties and evolutionary relations bit more than structural similarity 
## $pI$
- isoelectric point
- $pH$ at which molecule carries no charge 
- molecules at $pH$ around $pI$ tend to how lower solubility 
- $pH$ < $pI$ positive charge 
- $pH$ > $pI$ negative charge

## GRAVY
- grand average hydropathy
- average hydropathy score of a protein across all its amino acid residues using the Kyte–Doolittle hydropathy scale (idk TBA)
- negative GRAVY hydrophilic positive GRAVY hydrophobic (higher likelihood of membrane bound enzyme)

## Aromaticity
- relative frequency of aromatic residues phenylalanine, tyrosine, tryptophan
- important for folding and structural interactions 
- scale 0-1
- 0,07-0,11 globular proteins 
- possible relation to thermal stability and clefts, pockets and transmembrane interaction 

## PCA 
- principal component analysis
- deterministic linear dimensional reduction 
- reduces high number of dimensions into new dimension capturing maximum variance/spread of data in the data (primary components)
- simple, fast, good for global linear relationships between groups, deterministic (always same output)
- fails to capture non-linear or complex relationships and struggles with overlaps
## UMAP
- uniform manifold approximation and projection
- non-linear dimensional reduction optimized for 2D layout 
- uses k-nearest neigbours in the original high dimensional space remain neighbors in 2D
- non-deterministic requiring hyperparameter optimization good intra-cluster distances, but relative cluster positions tend to be skewed 

## Possible other 
### Chemoinformatics
TBA




