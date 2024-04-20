import streamlit as st
import pickle
import pandas as pd

#Function for recommending 5 most similar Movies
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    dist=similarity[movie_index]
    movie_list=sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies    

#Import Final DataFrame 
movies_dict=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_dict)

#importing Directors name list
director_namaes=pickle.load(open('director_name.pkl','rb'))

#Function to show top 5 movies of same director
def recom2(director):
    director_list=director_namaes[director_namaes[0]==director].index[:5]
    recommend_director=[ ]

    for i in director_list:
        recommend_director.append(movies.iloc[i].title)
    return recommend_director    

#importing model Wich will find top 5 simlilar movies
similarity=pickle.load(open('simi.pkl','rb'))

#title of webpage
st.title('Movie Recommender System')

#recommendation on the basis of MOVIE NAME or DIRECTOR NAME
movie_or_director=st.selectbox(
    " Recommendation on the basis of MOVIE NAME or DIRECTOR NAME ",
    ('Movie','Director'))

if movie_or_director=='Movie':
    select_movie_name=st.selectbox(
        " Select Movie Name ",
        movies['title'].values)
elif movie_or_director =='Director':
    select_director_name=st.selectbox(
        " Select Director name ",
        director_namaes[0].values)
    


#to show results
if st.button("Recommend"):
    if movie_or_director =='Movie':
        recommendations= recommend(select_movie_name)
        for i in recommendations:
            st.write(i)
    elif movie_or_director == 'Director':
        reco=recom2(select_director_name)    
        for i in reco:
            st.write(i)    