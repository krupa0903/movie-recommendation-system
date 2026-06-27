import streamlit as st
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movies
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Generate similarity on the fly
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)

# Recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]
    recommended = []
    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)
    return recommended

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", page_icon="🎬")
st.title('🎬 Movie Recommendation System')
st.markdown("Select a movie and get 5 similar recommendations!")

selected_movie = st.selectbox(
    'Choose a movie you like:',
    movies['title'].values
)

if st.button('🍿 Recommend'):
    recommendations = recommend(selected_movie)
    st.subheader("You might also enjoy:")
    for i, movie in enumerate(recommendations, 1):
        st.success(f"{i}. {movie}")
