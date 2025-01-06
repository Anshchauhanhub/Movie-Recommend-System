import streamlit as st
import pickle as pkl
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=142745e2ff113800c1c8bc6f4e8a53bc&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

movies_dict = pkl.load(open('movies_dict.pkl', 'rb'))
df = pd.DataFrame(movies_dict)

df = df.fillna({'tags': ''})

cv = CountVectorizer(max_features=5000, stop_words='english')
vectorized_data = cv.fit_transform(df['tags'])

similarity = cosine_similarity(vectorized_data.toarray())

def recommend(movie, num_recommendations=10):
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:num_recommendations + 1]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = df.iloc[i[0]]['movie_id']
        recommended_movies.append(df.iloc[i[0]]['title'])
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

st.title('🎬 Movie Recommender System ')

option = st.radio('Choose an option:', ['Search for a movie', 'Select a movie from the list'])

if option == 'Search for a movie':
    search_term = st.text_input('Search for a movie:')
    if search_term:
        search_results = df[df['title'].str.contains(search_term, case=False, na=False)]
        if not search_results.empty:
            selected_movie = st.selectbox('Select a movie from search results:', search_results['title'].values)
        else:
            st.write("No movies found with that title.")
            selected_movie = None
    else:
        selected_movie = None

elif option == 'Select a movie from the list':
    selected_movie = st.selectbox('Select a movie from the list:', df['title'])

num_recommendations = st.sidebar.slider('Number of recommendations:', 1, 10)

if selected_movie and st.button('Recommend'):
    recommended_movies, recommended_movies_posters = recommend(selected_movie, num_recommendations)
    st.write(f"Top {num_recommendations} movies similar to **{selected_movie}** are:")
    for movie, poster in zip(recommended_movies, recommended_movies_posters):
        st.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: center; border: 1px solid #ccc; border-radius: 10px; padding: 10px; margin: 10px; width: 300px;">
                <img src="{poster}" style="width: 100%; border-radius: 10px;" />
                <h3 style="text-align: center;">{movie}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
