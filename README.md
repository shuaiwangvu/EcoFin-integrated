This repo is for my paper 

## **On the analysis of large integrated knowledge graphs for Economics, Banking, and Finance**

### Integration 
*main.py* is a Python script for the analysis of each individual knowledge graph and the integrated knowledge graph.
More specifically, we study how the triples regarding the 10 relations works during the integration of 11 files from 9 ontologies.
In addition, it exports a plot of the connected components of the skos:exactMatch.

### Connected Components
*main-connected-component.py* is a Python script for the analysis of Strongly Connected Components (SCC) and Weakly Connected Components (WCC) regarding the following relations

 - skos:broader 
 - skos:broadMatch 
 - skos:narrower
 - skos:narrowMatch

### In-/Out-Degree

*main-degree.py* gives an analysis of the in-degree and out-degree of the entities. 

### Transitive relations
*main-transitive.py* examins the transitive relations and print them out. 

Please report errors and comments at shuai.wang@vu.nl. Thank you!

> Written with [StackEdit](https://stackedit.io/).
