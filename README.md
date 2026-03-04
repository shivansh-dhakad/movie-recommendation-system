# movie-recommendation-system
A Python-powered movie recommendation web application that suggests similar movies based on text feature similarity from an Indian movie dataset. This project uses NLP techniques like **text preprocessing**, **vectorization**, and **cosine similarity** to compute and display movie recommendations via a Flask web interface.

# Overview

This repository contains a **movie recommendation system** that analyzes movie metadata and descriptions, generates text embeddings, and recommends similar movies using cosine similarity. Users can interact with the system through a web UI built with **Flask**.

# Features

- Simple and responsive Flask web interface  
- Search for movies and get similar movie recommendations  
- Utilizes natural language processing & machine learning techniques  
- Supports only Indian movie dataset with genres, keywords, cast, etc.

# Setup & Installation
1) **Clone the repository**
   ```bash
   git clone https://github.com/shivansh-dhakad/movie-recommendation-system.git
   cd movie-recommendation-system
2) Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate       # macOS / Linux
   venv\Scripts\activate          # windows
3) Install dependencies
    ```bash
    pip install -r requirements.txt
4) Run the Flask app
   ```bash
    python app.py
5) Open your browser and go to:
    ```bash
    http://localhost:5000
# How It Works
The recommendation logic (shown in recommendor.ipynb) broadly does the following:
- **Load dataset:** Reads movie metadata (e.g., title, genres, overview, cast, keywords).
- **Text Cleaning:** Combines relevant text fields into a single ‘tag’ and performs cleaning with the cleantext library & NLTK.
- **Vectorization:** Converts combined tags to numerical vectors using a method like CountVectorizer.
- **Similarity:** Computes cosine similarity between all movie vectors.
- **Recommend:** Based on the searched movie, picks the top similar movies from the similarity matrix.

# Future Enhancements
- Add collaborative filtering to improve recommendations
-  Use TF-IDF or word embeddings for better semantic similarity
-   Add movie poster integration (via API)
-   Enable user input for personalized recommendations

   
