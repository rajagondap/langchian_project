import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    # Load the iris dataset from sklearn
    iris = load_iris()
    
    # Create a DataFrame for the features and target
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target    
    return df, iris.target_names

df, target_names = load_data()
st.title("Iris Flower Classification")
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])
sepal_length = st.slider("Sepal Length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.slider("Sepal Width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.slider("Petal Length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.slider("Petal Width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(input_data)
prediction_proba = model.predict_proba(input_data)
st.write(f"Predicted Species: {target_names[prediction][0]}")
st.write("Prediction Probabilities:")
st.bar_chart(prediction_proba, use_container_width=True)
st.write("Feature Importance:")
st.bar_chart(model.feature_importances_, use_container_width=True)
st.write("Feature Names:")
st.write(df.columns[:-1])
st.write("Feature Values:")
st.write(input_data[0])
st.write("Model Accuracy:")
accuracy = model.score(df.iloc[:, :-1], df['species'])
st.write(f"{accuracy:.2f}")
st.write("Model Parameters:")
st.write(model.get_params())