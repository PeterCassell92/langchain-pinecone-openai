# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LangChain tutorial/experimentation project focused on learning and demonstrating LangChain capabilities with OpenAI models and Pinecone vector storage.

## Development Commands

### Setup
```bash
# Install dependencies (use Python 3.12)
pip install -r requirements.txt

# Set environment variables in .env file:
# OPENAI_API_KEY=your_key_here
# PINECONE_API_KEY=your_key_here
```

### Running Code
```bash
# Main script (uses deprecated API)
python3 main.py

# Jupyter notebook with working examples
jupyter notebook notebooks/langchain-13-min.ipynb
```

## Code Architecture

### Key Components

**LangChain Integration Pattern**: The codebase demonstrates modern LangChain patterns using:
- `langchain_openai.ChatOpenAI` for LLM interactions (not the deprecated `langchain.llms.OpenAI`)
- `langchain_core.messages` for structured chat messages
- `langchain_core.prompts.PromptTemplate` for prompt engineering
- `langchain_core.runnables` for chaining operations
- `langchain_pinecone.PineconeVectorStore` for vector storage

**Vector Storage Architecture**: 
- Uses OpenAI embeddings (`text-embedding-3-small` with 512 dimensions) 
- Integrates with Pinecone for vector similarity search
- Text splitting via `TokenTextSplitter` for token-aware chunking

**Agent Framework**:
- Demonstrates ReAct agents with tools (Python REPL, file management, shell)
- Uses LangChain Hub for prompt templates (`hwchase17/react`)

## Important Notes

- **main.py** contains deprecated LangChain API usage (`langchain.llms.OpenAI`) - refer to the Jupyter notebook for modern patterns
- The notebook demonstrates proper chain composition, prompt chaining, and vector search workflows
- When working with Pinecone, ensure index dimensions match embedding dimensions (512)
- Agent examples show both simple (Python-only) and complex (file/shell access) tool configurations