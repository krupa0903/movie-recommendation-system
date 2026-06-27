# 🎬 Movie Recommendation System
A content-based movie recommendation system built with Python and deployed using Streamlit.

## 📌 About The Project
This system recommends movies similar to the one you select, using
machine learning techniques like vectorization and cosine similarity.
It is trained on the TMDB 5000 Movie Dataset from Kaggle.

## 🚀 Live Demo
[Click here to view the live app](https://movie-magic-krupa.streamlit.app).

## 🧠 How It Works
1. Extracts features from movies (genres, keywords, cast, crew, overview)
2. Combines all features into a single "tags" column
3. Applies stemming to normalize words
4. Vectorizes text using CountVectorizer (Bag of Words)
5. Computes cosine similarity between all movies
6. Recommends top 5 most similar movies

## 🛠️ Built With
- Python
- Pandas & NumPy
- Scikit-learn
- NLTK
- Streamlit
- Jupyter Notebook

## 📦 Dataset
- TMDB 5000 Movies Dataset from Kaggle
- tmdb_5000_movies.csv
- tmdb_5000_credits.csv
## 📁 Project Structure
movie-recommender/

│

├── app.py                  # Streamlit web app

├── recommendation.ipynb    # Model building notebook

├── movies.pkl              # Saved movie data

├── similarity.pkl          # Saved similarity matrix

├── requirements.txt        # Dependencies

├── setup.sh                # Heroku configuration

└── Procfile                # Heroku entry point

## 📊 Machine Learning Pipeline
| Feature Extraction | Genres, Keywords, Cast, Crew |
| Text Preprocessing | Stemming, Lowercasing |
| Vectorization | CountVectorizer (5000 features) |
| Similarity | Cosine Similarity |
| Output | Top 5 recommendations |

## 🤖 AI Assistance

This project was built with guidance from **Claude AI by Anthropic**.

Claude assisted with:
- Step-by-step project planning
- Code writing and explanation
- Debugging and troubleshooting
- Deployment guidance (GitHub + Heroku)
- Real-time photo-based guidance throughout the build

> "I believe in transparency — AI was used as a learning tool
> and mentor throughout this project, not to replace understanding
> but to build it."

## 👩‍💻 Author

Built  with ❤️ by Krupa 
- GitHub: krupa0903
