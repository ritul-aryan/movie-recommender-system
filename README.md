# Content-Based Movie Recommender System 🎬

A machine learning-powered web application that recommends movies based on user selection. Built using a content-based filtering approach, the system analyzes movie metadata (genres, keywords, cast, and crew) from the TMDB 5000 dataset to find and suggest similar films.

## 🌟 Key Features
* **Content-Based Filtering:** Utilizes natural language processing to extract and vectorize tags from movie plots and metadata.
* **Cosine Similarity Search:** Calculates the mathematical distance between movie vectors to return the top 5 closest matches instantly.
* **Fast Inference:** Pre-computed similarity vectors are serialized (pickled) during offline training, allowing the Streamlit frontend to load and recommend movies with zero latency.
* **Interactive UI:** Clean, responsive web interface built entirely in Python using Streamlit.

## 🛠️ Tech Stack
* **Frontend & Routing:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-learn (Text Vectorization & Cosine Similarity)
* **Serialization:** Pickle

## 📁 Project Structure
* `app.py` - Main Streamlit application and UI logic.
* `Movie_Recommendation.ipynb` - Jupyter Notebook containing data cleaning, feature engineering, and model training.
* `movie_dict.pkl` - Serialized dictionary of movie titles and IDs.
* `vectors.pkl` - Pre-computed similarity matrix.
* `tmdb_5000_movies.csv` & `tmdb_5000_credits.csv` - Raw dataset files (Linked/Excluded from repo due to size).

## 🚀 Getting Started

### Prerequisites
* Python 3.8+

### Installation & Setup

1. **Clone the repository:**
   git clone https://github.com/ritul-aryan/movie-recommender-system.git
   cd movie-recommender-system

2. **Install dependencies:**
   pip install streamlit pandas numpy scikit-learn

3. **Run the application:**
   streamlit run app.py
