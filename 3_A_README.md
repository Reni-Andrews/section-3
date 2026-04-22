Markdown
# Product Catalogue API (Section 3A)

This is a standalone REST API built using **FastAPI** and **MongoDB** for managing a product catalogue. 

## Features
- **Asynchronous CRUD**: Full Create, Read, and Delete operations using `motor`.
- [cite_start]**Validation**: Strict request/response modeling using **Pydantic**[cite: 114, 126].
- [cite_start]**Security**: **CORS** middleware enabled and **Rate Limiting** (20 requests/minute) applied to the creation endpoint[cite: 120, 121, 128].
- [cite_start]**Auto-Documentation**: Interactive **Swagger UI**[cite: 122, 129].

## Prerequisites
- Python 3.10+
- MongoDB (running locally on port 27017)

## Installation & Setup
1. Clone the repository and navigate to the folder:
   ```bash
   cd product-catalogue-api
Create and activate a virtual environment:

Bash
python -m venv venv
.\venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Create a .env file based on the .env.example template.

Running the Application
Start the server using Uvicorn:

Bash
python -m uvicorn main:app --reload
Testing
Once the server is running, visit the Swagger UI to test the endpoints:
http://localhost:8000/docs
