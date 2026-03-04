from flask import Blueprint, jsonify, request
import pandas as pd
import pickle

recommendor_bp = Blueprint("recommendor_bp", __name__)

# 🔹 LOAD ENRICHED DATA
movies_df = pd.read_csv("recommendor system/new_df_enriched.csv")
similarity = pickle.load(open("recommendor system/similarities.pkl", "rb"))

# 🔹 Helper: get movie dict from dataframe row
def row_to_movie(row):
    return {
        "movie_id": int(row.movie_id),
        "title": row.title,
        "poster": row.poster,
        "overview": row.overview,
        "release": row.release
    }

# 🔹 HOME: movies by TAG category (5 groups)
@recommendor_bp.route("/api/home")
def home_movies():
    tag_groups = ["action", "love", "comedy", "thriller", "crime"]
    result = {}

    for tag in tag_groups:
        subset = movies_df[movies_df["tags"].str.contains(tag, case=False, na=False)]
        sample = subset.sample(5)

        movies = []
        for _, row in sample.iterrows():
            movies.append(row_to_movie(row))

        result[tag.capitalize()] = movies

    return jsonify(result)

# 🔹 SEARCH + RECOMMEND
@recommendor_bp.route("/api/search")
def search_movies():
    query = request.args.get("q")

    matched = movies_df[movies_df["title"].str.contains(query, case=False, na=False)].head(1)

    if matched.empty:
        return jsonify([])

    index = matched.index[0]

    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)[1:10]

    results = []
    results.append(row_to_movie(matched.iloc[0]))

    for i in distances:
        row = movies_df.iloc[i[0]]
        results.append(row_to_movie(row))

    return jsonify(results)