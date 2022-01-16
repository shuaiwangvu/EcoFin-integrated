This repo is for my paper 

## **On the analysis of large integrated knowledge graphs for Economics, Banking, and Finance**

### Abstract
Knowledge graphs are being used for the detection of money laundering, insurance fraud, and other suspicious activities. Some recent work demonstrated how knowledge graphs are being used to study the impact of the COVID-19 outbreak on the economy. The fact that knowledge graphs are being used in more and more interdisciplinary problems calls for a reliable source of interdis- ciplinary knowledge. In this paper, we study the integration of knowledge graphs in the domains of economics, banking, and finance. Our integrated knowledge graph has over 620k enti- ties and 1.8 million triples. By performing statistical and graph- theoretical analysis, we demonstrate how the integration results in more entities with richer information. Its quality was examined by analyzing the subgraphs of the identity links and (pseudo- )transitive relations. Finally, we study the sources of error, and their refinement and discuss how the use of our integrated graph may lead to greater sophistication and better accuracy.

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

### Paper
https://github.com/shuaiwangvu/EcoFin-integrated/blob/main/EcoFinKG_paper.pdf

Please report errors and comments at shuai.wang@vu.nl. Thank you!

> Written with [StackEdit](https://stackedit.io/).
