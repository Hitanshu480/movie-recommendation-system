# 🎬 Movie Recommendation System

This is a **content-based Movie Recommendation System** built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**.  
The application recommends movies based on similarity between movie features and provides an interactive user interface.

🔗 Live App (Streamlit Cloud):  
https://movie-recommendation-system-cvtev8jexy33psstd7w4dp.streamlit.app/

---

## 🚀 Project Overview

The Movie Recommendation System suggests movies similar to a selected movie using **cosine similarity**.  
It helps users discover new movies based on their interests in genre, keywords, cast, and overview.

The system is designed to be simple, fast, and user-friendly.

---

## 🧠 Recommendation Technique Used

- **Content-Based Filtering**
- **Vectorization** using CountVectorizer
- **Similarity Measure**: Cosine Similarity

---

## 📊 Dataset Description

The dataset contains movie-related information such as:

- Movie Title  
- Genres  
- Overview  
- Cast  
- Crew  
- Keywords  

These features are combined to create a similarity matrix used for recommendations.

---

## 🧱 Project Structure

movie-recommendation-system/
│
├── app.py # Streamlit application
├── movies.pkl # Movie metadata
├── similarity.pkl # Cosine similarity matrix
├── requirements.txt # Dependencies
├── README.md # Project documentation

yaml
Copy code

---

## 🖥️ Application Features

- 🎥 Select a movie from the dropdown list
- 🔍 Get top 5 similar movie recommendations
- 🖼️ Movie posters displayed with recommendations
- ⚡ Fast and responsive UI using Streamlit

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the repository
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system

shell
Copy code

### 2️⃣ Install dependencies
pip install -r requirements.txt

graphql
Copy code

### 3️⃣ Run the Streamlit app
streamlit run app.py

yaml
Copy code

---

## ☁️ Deployment

The application is deployed using **Streamlit Cloud**.

Deployment steps:
1. Push the project to GitHub
2. Connect the repository on Streamlit Cloud
3. Select `app.py` as the main file
4. Deploy the application

---

## 🧠 Learning Outcomes

- Data preprocessing and feature engineering
- Text vectorization techniques
- Similarity-based recommendation systems
- Building interactive applications with Streamlit
- Model persistence using Pickle
- GitHub and Streamlit Cloud deployment

---

## 🔮 Future Enhancements

- Add collaborative filtering
- Improve recommendation accuracy
- Add search and filter options
- User login and personalization
- Hybrid recommendation system

---

## 👨‍💻 Author

Hitanshu Sekhar Das  
MCA | Data Analytics & Machine Learning  
GitHub: https://github.com/Hitanshu480  

---

## 📜 License

This project is created for educational and learning purposes only.
