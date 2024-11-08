# PDF Processing, Embeddings Generation, and Parameter Optimization for LLMs

This project provides an infrastructure for analyzing PDF documents, enabling automated file integration and embedding generation using FAISS and Ollama. Beyond its primary function of answering questions based on document content, this project is designed to facilitate testing and fine-tuning of various system parameters to optimize performance and accuracy in information retrieval.

### Project Objectives
1. **Configuration Variable Optimization**: The system enables experimentation with adjustable parameters, such as the number of chunks, model selection, chunk size, and other settings that may be added in the future. This allows for identifying the most efficient configuration for each use case.
2. **Comparison of Embedding Models**: The project is structured to support testing and comparison of different embedding models for document analysis, with compatibility for Ollama embeddings.
3. **Comparison of LLM Models**: The project also focuses on creating a flexible environment for testing various Language Learning Models (LLMs), including compatibility with Ollama.

### Use Cases
This system is ideal for users who need to:
- **Explore parameter configurations** to enhance efficiency in information search and retrieval.
- **Compare different language models** and chunking methods in a controlled environment to identify the best combination for each document type or query.
- **Automate document analysis** with precision, speed, and scalability, allowing for parameter adjustments to achieve optimized results.

## Future Updates

1. **Integration with OpenAI API for LLMs and Embeddings**: 
   - Future versions will support direct integration with OpenAI’s API, enabling users to leverage OpenAI’s advanced LLMs for question-answering tasks and high-quality embeddings for document analysis.

2. **Chunking Levels Guide**
   To further improve chunking and information retrieval across various document types, the project will incorporate a structured guide with five levels of text splitting, inspired by [this tutorial](https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/main/tutorials/LevelsOfTextSplitting/5_Levels_Of_Text_Splitting.ipynb).

   Users will be able to experiment with these chunking levels to determine the most effective method for their specific use cases:

   - **Level 1: Character Splitting** - Simple, static chunks based on a fixed character count.
   - **Level 2: Recursive Character Text Splitting** - Dynamic, recursive chunking that uses separators to form contextually coherent chunks.
   - **Level 3: Document-Specific Splitting** - Customized chunking methods tailored to specific document types, such as PDFs, Python files, and Markdown.
   - **Level 4: Semantic Splitting** - Embedding-based chunking that ensures chunks retain semantic meaning, enhancing model understanding.
   - **Level 5: Agentic Splitting** - An advanced, experimental agent-based approach for chunking, particularly suitable when token costs are low or negligible.

   Each level offers unique advantages, enabling users to balance model performance, token usage, and retrieval accuracy by selecting the most effective chunking strategy for their needs.

## Getting Started

To run this project, follow these steps:

### 1. Basic Setup
First, ensure that all necessary dependencies are installed. If you have a `requirements.txt` file, you can install dependencies with:

```bash
pip install -r requirements.txt
```

### 2. Directory Setup

Create a directory named db where all PDF files that need to be converted into embeddings should be placed.


###  3. Environment Variables Configuration

```bash
export FOLDER_NAME_FILES=db
export FOLDER_NAME_EMBEDDINGS=embeddings-4chunks-400chunksize-25overlap
export EMBEDDING_MODEL=nomic-embed-text
export NUMBER_CHUNKS=4
export CHUNK_SIZE=400
export chunk_overlap=25
export MODEL_LLM=llama3.2
export NAME_FILE_OUTPUT=4chunks-400chunksize-25overlap
```

###  4. Generate Embeddings
This will save embeddings in the specified folder based on the configured chunk size, overlap, and embedding model.

```bash
python save_embeddings.py
```


###  5. Generate Responses

Once embeddings are saved, you can generate responses by running:
```bash
python generate.py
```

This script will read the embeddings and output answers based on the MODEL_LLM specified.
