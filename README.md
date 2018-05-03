# SODA501_Project
## Code for SODA 501 Project - GOP state press releases

### 1. Scraping State Party Press Releases

This repository contains code to scrape press releases from state GOP party websites from 2013-2018 (when available). The scripts are written in Python and rely heavily on BeautifulSoup and Selenium. The scripts produce .txt files with the following format:
<br />

  *Press Release Title* <br />
  *Press Release Date*  <br />
  *Press Release Contents*
 <br />
 
 The files are written in UTF-8 encoding. It should be noted that running these scripts at different times will produce slightly different data. This occurs because the script specifies pages to scrape from, and which pages press releases are located will change as more press releases are added.
 
These output .txt files are then used as input for the second step in the pipeline, extracting names and organizations.
 
 
 ### 2. Named Entity Recognizer (NER)
 
 We utilize Stanford NER, a Java implementation of a Named Entity Recognizer. Per the Stanford NLP Group website: "Named Entity Recognition (NER) labels sequences of words in a text which are the names of things, such as person and company names, or gene and protein names. It comes with well-engineered feature extractors for Named Entity Recognition, and many options for defining feature extractors." For more information regarding this implementation, please visit https://nlp.stanford.edu/software/CRF-NER.html.
 
The scripts output .JSON files with data on names, entities, and geo-locations embedded in the press releases. These data are then utilized in the third step in our pipeline, social network analysis.
 
 
 ### 3. Entity-based Co-Occurence Network Analysis
 
 With the named entities derived from our Java script, we treat these entities as nodes. Individual party press releases are edges connecting names to each other. For example, if a party press release contains the entities "Donald Trump" and "Roy Moore", that press release is an edge linking the nodes "Donald Trump" and "Roy Moore". A network analysis-based approach allows us to quantitatively analyze who and what the parties are talking, and how these entities are linked in party activist language. All network analysis is implemented in the R script.
 
These scripts utilize the .JSON files from step two in our pipeline. We build a co-occurence matrix for names and organizations, separately. We then visualize the network produced from these matrices. Lastly, we conduct various community detection algorithms calculated from the co-occurence matrices.
