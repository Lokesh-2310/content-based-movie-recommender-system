import streamlit as st
import pickle
import pandas as pd
import requests
import time

st.set_page_config(layout='wide')


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(str(movie_id))
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    if poster_path!=None:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    else:
        return None



movies=pickle.load(open("movies_dict.pkl",'rb'))
movies=pd.DataFrame(movies)

similarity=pickle.load(open("similarity.pkl",'rb'))


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

st.title("Movies Recommender System :film_projector:")


movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown :arrow_down_small:",
    movie_list
)

if st.button('Show Recommendation :rocket:'):
    image_url="https://propertywiselaunceston.com.au/wp-content/themes/property-wise/images/no-image@2x.png"

    with st.spinner('Fetching details...'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        time.sleep(3)
        st.subheader("Top 10 recommended movies for you :heart_eyes:!")
        counter=0
        for i in range(4):
            col1, col2, col3 = st.columns(3)
            with col1:
                image = recommended_movie_posters[counter]
                counter=counter+1
                if image == None:
                    st.image(image_url, caption='Not available')
                else:
                    st.image(image)
                st.text(recommended_movie_names[0])
                if counter==10:
                    break

            with col2:
                image = recommended_movie_posters[counter]
                counter=counter+1
                if image == None:
                    st.image(image_url)
                else:
                    st.image(image)
                st.text(recommended_movie_names[1])

            with col3:
                image = recommended_movie_posters[counter]
                counter=counter+1
                if image == None:
                    st.image(caption='Not available')
                else:
                    st.image(image)
                st.text(recommended_movie_names[2])

            st.divider()