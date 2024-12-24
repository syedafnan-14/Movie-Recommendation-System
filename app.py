import pandas as pd
import joblib
import streamlit as st
import requests

def recommend_movies(movie):

    idx = df[df['title'] == movie].index[0]
    similar_movies = similarity_matrix[idx]
    
    titles = []
    posters = []
    
    for film in similar_movies[1:9]:  
        url = f"https://www.omdbapi.com/?i={df['imdb_id'][film]}&apikey=8c4102bb"  
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            titles.append(data["Title"])
            posters.append(data["Poster"]) 
    
    
    
    index = 0
    for _ in range(2): 
        columns = st.columns(4)
        for col in columns:  
            if index < len(titles):
                if posters[index] != 'N/A':
                    col.image(posters[index])  
                    col.write(titles[index])
                else:
                    col.write(titles[index])
                index += 1
                
                    
    

st.title("Movie Recommendation System")

similarity_matrix = joblib.load("similarity_matrix.pkl")
df = pd.read_csv("movies.csv")

movie = st.selectbox("Select a Movie",df["title"])

if st.button("Search"):
    recommend_movies(movie)

