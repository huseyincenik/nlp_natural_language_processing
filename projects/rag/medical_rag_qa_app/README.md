# Medical RAG QA App
![image](https://github.com/user-attachments/assets/7fa08bc9-af1a-4155-98c6-1e0b3db5a0c6)

## Overview

The **Medical RAG QA App** is a web-based application designed for medical question answering. It utilizes the Meditron 7B LLM (Large Language Model), Qdrant Vector Database, and PubMedBERT Embedding Model to provide accurate and relevant responses to medical queries. 

## Features

- **Large Language Model**: Utilizes Meditron 7B LLM for generating contextually relevant answers.
- **Vector Database**: Uses Qdrant for efficient retrieval of related documents.
- **Embeddings**: Employs PubMedBERT for high-quality text embeddings.
- **Web Interface**: Built with FastAPI and Jinja2 for a user-friendly web interface.

## Architecture

1. **Medtron 7B LLM**: This model generates answers based on the context provided.
2. **Qdrant Vector Database**: Stores and retrieves vectorized representations of medical documents.
3. **PubMedBERT Embeddings**: Converts text into embeddings for similarity searches.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker (optional but recommended for containerized deployment)

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/huseyincenik/data_science.git
    cd Projects/rag/medical_rag_qa_app
    ```

2. **Install dependencies**

    Create a virtual environment and install the required packages:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Set up environment variables**

    Create a `.env` file and add necessary configurations:

    ```env
    QDRANT_URL=http://localhost:6333
    ```

### Running the Application

1. **Start Qdrant Vector Database**

    Ensure Qdrant is running. You can use Docker to set up Qdrant:

    ```bash
    docker run -d -p 6333:6333 qdrant/qdrant
    ```

2. **Run the FastAPI Application**

    Start the FastAPI server:

    ```bash
    uvicorn rag:app
    ```

### Docker Deployment

1. **Build the Docker Image**

    ```bash
    docker build -t medical-rag-qa-app .
    ```

2. **Run the Docker Container**

    ```bash
    docker run -d -p 80:8000 medical-rag-qa-app
    ```

### Usage

1. **Access the Web Interface**

    Navigate to `http://localhost:8000/` in your web browser.

2. **Ask Medical Questions**

    Use the web interface to submit medical queries and receive answers.

### API Endpoints

- **GET /**: Renders the main page.
- **POST /get_response**: Submits a query and receives a response.


### Acknowledgements

- **Meditron 7B**: Provided by TheBloke on Hugging Face.
- **Qdrant**: Vector database for efficient document retrieval.
- **PubMedBERT**: Embedding model for text similarity.

### Contact

For any questions or issues, please contact [huseyinceniik@gmail.com](mailto:huseyinceniik@gmail.com).

