# Content-Based Movie Recommender System

A Python-based content-driven movie recommendation system that suggests similar films based on metadata such as descriptions, genres, and cast. The system utilizes natural language processing (NLP) techniques and cosine similarity to provide accurate recommendations.

---

## 🚀 Features

- **Content-Based Filtering**: Recommends movies similar to a given movie based on metadata.
- **TF-IDF Vectorization**: Transforms textual data into numerical vectors for similarity computation.
- **Cosine Similarity**: Measures the cosine of the angle between vectors to determine similarity.
- **Streamlit Interface**: Provides an interactive web interface for users to input movie titles and receive recommendations.

---

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Pandas
- Scikit-learn
- NLTK

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Lokesh-2310/content-based-movie-recommender-system.git
   cd content-based-movie-recommender-system

2. Install dependencies:
    ```bash
    pip install streamlit pandas scikit-learn nltk

3. Download the dataset:
    ```bash
   wget https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

4. Run the file:
   ```bash
   streamlit run app1.py

5. Poject Structure : 
  ```perl
content-based-movie-recommender-system/
├── app1.py                  # Streamlit application
├── Untitled.ipynb           # Jupyter notebook for data preprocessing
├── README.md                # Project documentation
└── tmdb_movie_metadata.csv  # Movie metadata dataset

