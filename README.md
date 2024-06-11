# Movie Review Analyzer

This project is a Movie Review Analyzer that uses the IMDB movie review dataset to analyze and predict the sentiments of movie reviews. The project leverages various Python libraries including NumPy, pandas, NLTK, and Streamlit. The Bag of Words technique is employed for vectorization, and the Naive Bayes algorithm, specifically Multinomial Naive Bayes, is used for model training. The model achieves a precision of 0.88. Additionally, a Streamlit app is developed to provide a user interface for predicting the sentiment of new movie reviews.

## Dataset

The IMDB movie review dataset used in this project can be found on Kaggle:
[IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews).

## Libraries Used

- **NumPy**: For numerical operations
- **pandas**: For data manipulation and analysis
- **NLTK (Natural Language Toolkit)**: For text preprocessing
- **Streamlit**: For creating the web app interface

## Project Structure

1. **Data Loading and Preprocessing**
   - Load the dataset using pandas
   - Clean and preprocess the text data using NLTK

2. **EDA**
   - Creating columns based on number of characters and number of words basis.
   - Visualizing features if they are important or not in training of models.

3. **Feature Extraction**
   - Apply the Bag of Words technique for vectorization using `CountVectorizer` from `scikit-learn`

4. **Model Training**
   - Train a Multinomial Naive Bayes model using the preprocessed data
   - Evaluate the model and achieve a precision of 0.88

5. **Streamlit App**
   - Develop a Streamlit app to provide a user interface for predicting the sentiment of new movie reviews

6. **Results**
   - The trained Multinomial Naive Bayes model achieved a precision of 0.88 on the test set. The Streamlit app allows users to input a movie review and get a sentiment prediction (positive or negative).
