# Content-Based Movie Recommender System (TMDB 5000 Dataset)

## Project Overview
This project builds a content-based recommendation system using the TMDB 5000 movie dataset. It recommends movies similar to a user-input title based on movie metadata such as genres, keywords, cast, director, and overview.

---

## 1. Data Preprocessing and Feature Extraction

- Parsed relevant metadata fields: genres, keywords, top 3 cast members, director, and movie overview.
- Cleaned data by handling missing or empty fields.
- Tokenized and normalized text using lowercasing and stemming.
- Combined features into a single textual "tag" representing movie content.
- Applied TF-IDF vectorization to convert text tags into numerical vectors.
- Used feature weighting to emphasize more important metadata (e.g., cast, genres).

---

## 2. Recommendation System Implementation

- Created a custom Dataset class to load and preprocess movie data efficiently.
- Computed cosine similarity between movie vectors to measure content similarity.
- Implemented a function to retrieve top-N recommendations for any given movie title.
- Accounted for edge cases like missing titles or duplicates.

---

## 3. Similarity Function Performance

- Chose cosine similarity for its effectiveness with sparse TF-IDF vectors.
- Tested different preprocessing approaches (stemming vs lemmatization) to optimize recommendations.
- Adjusted feature weights and inclusion of overview text based on qualitative evaluation of results.
- Achieved relevant recommendations with coherent genre and theme alignment.

---

## 4. Code Readability and Documentation

- Modular code structure with clear separation of preprocessing, vectorization, and recommendation logic.
- Meaningful variable names and inline comments for clarity.
- Documented design decisions, preprocessing choices, and trade-offs.
- Demonstrated strong understanding of content-based filtering principles.

---

## Usage Instructions

1. Load and preprocess the dataset using the custom Dataset class.
2. Vectorize combined tags with TF-IDF.
3. Compute cosine similarity matrix.
4. Input a movie title to get top 10 recommended movies based on content similarity.

---


## 📁 Dataset
TMDB 5000 Movie Dataset https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

