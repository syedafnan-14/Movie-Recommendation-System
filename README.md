# Movie-Recommendation-System
Movie Recommendation System
This project is a content-based Movie Recommendation System that suggests movies based on the provided title. Key features include:

- **Dataset Preparation**: Collected and analyzed data through Exploratory Data Analysis (EDA).
- **Text Preprocessing**: Applied steps like removing punctuations, numbers, converting to lowercase, tokenization, stemming, and vectorization using CountVectorizer.
- **Recommendation Engine**: Calculated cosine similarity to identify and recommend similar movies.
- **Streamlit App**: Developed an interactive user interface to showcase the system.
- **Deploymen**t: Hosted on Hugging Face for easy access and demonstration.

## Create a Virtual Environment
```
python -m venv venv
```
Activate the Virtual Environment in Windows
```
venv\Scripts\activate
```

## Install Dependencies
```
pip install -r requirements.txt
```

## Run the Project
```
streamlit run app.py
```
![Project Screenshot](Project_Screenshot.png)
[Project_Demo](https://huggingface.co/spaces/blacksw0rd/Movie)

