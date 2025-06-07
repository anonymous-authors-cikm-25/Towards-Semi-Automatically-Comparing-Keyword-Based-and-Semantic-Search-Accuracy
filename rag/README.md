# RAG for Confluence

## Architecture

![](/figures/architecture.png)

## How to use

### Credentials and Models
1. Add your Confluence credentials to ``.env``.
2. Set optionally the embedding model and the LLM you want to use for RAG in ``.env``
3. If you want to employ other embedding models not defined in ``get_embedding_function.py``, add them to the configuration.
4. Install [Ollama](https://ollama.com/download) and start it.
5. Pull and run the model you added to the ``.env`` file (e.g., ``ollama pull llama3.2``, ``ollama run llama3.2``)

### Environment Setup 
6. Create virtual environment: ``python -m venv venv``
7. Activate your environment: ``venv\Scripts\activate`` (i.e., Windows)
8. Install needed requirements: ``pip install -r requirements``

### Fetch and preprocess Confluence data
9. Run ``python confluence_fetcher.py`` to load your Confluence data. At this stage, it is transformed into markdown 
file, also split by sections and subsections (right) and not by fixed chunk_size (left), as shown in following picture.

![](/figures/chunking_strategy.png)

### Data Embedding
10. Run ``python embed_data.py`` to embed (save vector numerical representation) of your Confluence data in the Chroma 
vector database. The data will be saved as title of (sub)section with its content alongside with the link to Confluence
page. This link will be incorporated in the response to enhance its transparency and reliability.

### Ask your RAG Confluence
11. Run ``python rag.py`` after adding your query there.  
