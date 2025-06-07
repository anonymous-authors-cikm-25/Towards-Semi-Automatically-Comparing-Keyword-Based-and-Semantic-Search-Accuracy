# Performance Evaluation by means of Statistical Tests

This file describes the evaluation of the performance of different IR approaches.
Based on the equivalence classes, both systems under comparison can be recognized.
These equivalence classes are added right before the extension _.csv_ (e.g., 1_3: means the equivalence classes 1,2,3).

## Scoring Criteria

We provide two examples for better understanding and application:

### RAG vs. Confluence 
For each query in both csv files, assign a value of 1, 2 or 3 based on following scoring system. 
Note that lower values indicate better performance.
A checklist was created for each question to ensure consistent and unambiguous scoring for the chat-based search systems.
Please refer to the checklist, to correctly assign the output to its equivalence class.

The confluence search engine (keyword-based) is evaluated based on the position of the relevant result and the associated [Click-Through Rate (CTR)](https://firstpagesage.com/reports/google-click-through-rates-ctrs-by-ranking-position/):
On the other side, the RAG (semantic chat-based) is evaluated based on the completeness of the generated response.
| Equivalence class | Confluence (CTR)  | RAG (via checklist)                                                                                                                                   |
|-------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1               | 1 - 2 (CTR ≈ 60%) | Information is fully complete                                                                                                                         |
| 2               | 3 - 7 (CTR ≈ 35%) | Information is partially complete                                                                                                                     |
| 3                | 8+    (CTR ≈ 5%)  | Information is unavailable                                                                                                                                                      |


### Retrieval of RAG vs Confluence

For each query in both csv files, assign an ordinal value from 1 to 10 based on the position of the relevant result.
Note that lower values indicate better performance. 
Both systems generate list-based outputs. 
For Confluence, each result up to the 10th position gets the equivalence class valued with this position. 
For the Retrieval part of RAG, since only 5 results are generated, the same criteria is applied. If no relevant document is retrieved, then it gets assigned the equivalence class 10.


## Statistical Tests

After assigning the scores, run:

- add the filenames in the python classes defined by: 
  - ``file1 = .....csv`` 
  - ``file2 = .....csv``.
- ``python mann_whitney.py``: to check for statistically significant difference.
- ``python vargha_delaney.py``: to calculate the A12 measure.
