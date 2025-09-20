# LangChain Learning Tutorial

A hands-on tutorial for learning LangChain fundamentals through practical examples with OpenAI models and Pinecone vector storage.

## What You'll Learn

- 🤖 Basic LLM interactions with OpenAI models
- 🔗 Prompt chaining and template composition
- 📊 Vector embeddings and similarity search with Pinecone
- 🛠️ Building ReAct agents with various tools
- 📝 Text splitting strategies for RAG applications

## Prerequisites

- Python 3.10+ (tested with 3.12)
- OpenAI API key
- Pinecone API key (free tier works)
- Basic Python knowledge

## Quick Start with UV

[UV](https://github.com/astral-sh/uv) is a fast Python package manager that makes environment setup simple.

### 1. Install UV (if not already installed)

```bash
# On Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Set up the project

```bash
# Clone the repository
git clone https://github.com/rabbitmetrics/langchain-13-min.git
cd langchain-13-min

# Create a virtual environment with Python 3.12
uv venv --python 3.12

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

### 3. Configure API Keys

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_openai_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
```

### 4. Set up Pinecone Index

1. Go to [Pinecone Console](https://app.pinecone.io/)
2. Create a new index with these settings:
   - Name: `langchain-test-index`
   - Dimensions: `512`
   - Metric: `cosine`
   - Cloud: Any available region

### 5. Launch Jupyter Notebook

```bash
# Start Jupyter
jupyter notebook

# Navigate to notebooks/langchain-13-min.ipynb
```

## Notebook Learning Path

The Jupyter notebook is structured as a progressive learning journey:

### Part 1: Basic LLM Interaction
- Simple text generation with ChatOpenAI
- Understanding message types (System, Human, AI)
- Temperature and model selection

### Part 2: Prompt Engineering
- Creating prompt templates
- Variable substitution
- Chaining prompts with the pipe operator (`|`)

### Part 3: Advanced Prompt Chaining
- Sequential prompt execution
- Preserving context between prompts
- Using RunnableLambda for transformations

### Part 4: Text Processing
- RecursiveCharacterTextSplitter for simple chunking
- TokenTextSplitter for token-aware splitting
- Understanding chunk overlap

### Part 5: Vector Embeddings
- Creating embeddings with OpenAI
- Storing vectors in Pinecone
- Performing similarity searches

### Part 6: Building Agents
- Simple Python REPL agent
- Multi-tool agents with file system access
- Understanding the ReAct pattern

## Running Individual Examples

### Basic script (uses legacy API - educational purposes only)
```bash
python main.py
```

### Interactive notebook exploration
```bash
# Run cells sequentially in Jupyter
# Each section builds on the previous one
```

## Common Issues & Solutions

### Issue: "No module named 'langchain'"
```bash
# Ensure you're in the virtual environment
uv pip install langchain-core langchain-openai
```

### Issue: Pinecone connection errors
- Verify your index name matches `langchain-test-index`
- Check that dimensions are set to `512`
- Ensure your API key is valid

### Issue: OpenAI rate limits
- Add delays between API calls
- Use `gpt-3.5-turbo` instead of `gpt-4` for testing
- Consider using a lower temperature (0.3) for consistent results

## Key Concepts Demonstrated

1. **Modern LangChain Patterns**: The notebook uses current best practices, avoiding deprecated APIs
2. **Prompt Chaining**: Learn how to compose complex workflows from simple prompts
3. **Vector Search**: Understand how embeddings enable semantic search
4. **Agent Systems**: Build autonomous agents that can use tools and make decisions

## Learning Tips

1. **Run cells one by one**: Understand each output before proceeding
2. **Modify examples**: Change prompts and observe different outputs
3. **Check variable states**: Use `print()` statements to inspect intermediate results
4. **Experiment with parameters**: Try different models, temperatures, and chunk sizes

## Next Steps

After completing this tutorial, explore:
- Building a full RAG application
- Creating custom tools for agents
- Implementing memory in conversational chains
- Fine-tuning embeddings for your domain

## Resources

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [OpenAI API Reference](https://platform.openai.com/docs)
- [Pinecone Documentation](https://docs.pinecone.io/)
- [UV Package Manager](https://github.com/astral-sh/uv)

## Contributing

Feel free to open issues or submit PRs with improvements to the examples!

## License

MIT