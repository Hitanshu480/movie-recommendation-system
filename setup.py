from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="movie-recommendation",
    version="0.0.1",
    author="Hitanshu Sekhar Das",
    author_email="hitanshusekhar480@gmail.com", 
    description="A content-based movie recommendation system using NLP and Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "nltk",
        "streamlit"
    ],
    python_requires=">=3.8",
)
