import pickle
import pandas as pd
import streamlit as st

# Title
st.title('Anime Recommender System')

# Function for getting names of Recommended Anime.
def recommend(series):
    movie_index = tv_series[tv_series['title'] == series].index[0]
    distances = similarity[movie_index]
    series_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]

    recommend_series = []
        
    for i in series_list:
        series_title = tv_series.iloc[i[0]].title
        recommend_series.append((tv_series.iloc[i[0]].title))

    return recommend_series

series_dict = pickle.load(open('artifacts/anime_series_dict.pkl','rb'))
tv_series = pd.DataFrame(series_dict)

similarity = pickle.load(open('artifacts/anime_series_similarity.pkl','rb'))

selected_series_name = st.selectbox(
'Write your favourite Anime name for recommendations',
tv_series['title'].values)

# Printing the recommended Anime names if press the button below.
if st.button('Recommend'):
    st.title('Recommened Anime Series :-')
    names = recommend(selected_series_name)

    for name in names:
        st.text(name)