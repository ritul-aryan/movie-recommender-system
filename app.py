import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# --- 1. Load the Data & Calculate Similarity ---
# We load the dictionary and convert it back to a DataFrame
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# We load the TF-IDF vectors and calculate similarity on the fly (saves 100MB+ of storage!)
vectors = pickle.load(open('vectors.pkl', 'rb'))
similarity = cosine_similarity(vectors)

# --- 2. Recommendation Logic ---
def recommend(movie):
    # Find the index of the movie
    movie_index = movies[movies['title'] == movie].index[0]

    # Grab similarity scores
    distances = similarity[movie_index]

    # Sort and get top 5 recommendations
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# --- 3. Streamlit Web Interface ---
st.title('🎬 Movie Recommender System')
st.write("Find your next favorite movie based on plot, genres, and cast!")

# Create a dropdown menu with all movie titles
selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown',
    movies['title'].values
)

# Create a button to trigger the recommendation
if st.button('Recommend'):
    with st.spinner('Finding the best matches...'):
        recommendations = recommend(selected_movie_name)

        st.subheader("Top 5 Recommendations:")
        for i, movie in enumerate(recommendations, 1):
            st.write(f"**{i}.** {movie}")