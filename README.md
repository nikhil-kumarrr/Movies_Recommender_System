# Movie Recommendation System

## Introduction

Movie recommendation systems are one of the most widely used
applications of Machine Learning today. From Netflix to Amazon Prime,
recommendation engines play a crucial role in improving user experience
and engagement.\
In this project, I built a **Content-Based Movie Recommendation System**
using the TMDB 5000 Movie Dataset. The system processes movie metadata
like genres, cast, crew, keywords, and overviews, then uses **Natural
Language Processing (NLP)** techniques to generate recommendations based
on movie similarity.\
By leveraging **Count Vectorization** and **Cosine Similarity**, this
project demonstrates how to create an efficient recommendation pipeline
that can suggest the most relevant movies based on a user's input.

------------------------------------------------------------------------

## Features

-   Clean data preprocessing (genres, cast, crew, keywords)
-   Tag creation by combining key features
-   Vectorization using `CountVectorizer`
-   Similarity calculation with `cosine_similarity`
-   Recommendation function to get top 5 movies

------------------------------------------------------------------------

## Dataset

Dataset used: **TMDB 5000 Movies Dataset**\
Available on
Kaggle : https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

------------------------------------------------------------------------

## Conclusion

This project highlights how machine learning can transform raw data into
meaningful insights for personalized recommendations.\
While this is a basic content-based model, it lays a strong foundation
for building more advanced systems like **hybrid recommenders** that
combine collaborative filtering and deep learning approaches.
