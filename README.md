# Towards-Semi-Automatically-Comparing-Keyword-Based-and-Semantic-Search-Accuracy
In this repository we provide supplementary material for our paper Towards Semi-Automatically Comparing Keyword-Based and Semantic Search Accuracy.


## Evaluation

We provide the anonymized queries with their assignment to the respective equivalence classes. We did the comparison between RAG and Confluence and also between the retrieval component of RAG and Confluence.
For each one, we provide the equivalence classes assumed with the case company.
An extract of used queries and checklists are provided as PDF files, once in original (German) as well as translated to English using DeepL. 
These demonstrate on how a checklist can be created to ensure fair and unbiased assignment of outputs to equivalence classes.
The directory contains also a README file with deeper details and two python classes to run the Mann-Whitney U-Test and calculate the Vargha-Delaney A12 statistic.

## RAG

Here, we provide the code of our RAG application that fetches the data from confluence automatically and processes it to embeddings.
Please refer to the README file to configure it and grant access to Confluence with your credentials. 

## Figures

This directory contains two figures relevant to the implementation of RAG, namely what architecture we used and how we chunked the data before embedding it. 
