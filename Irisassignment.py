import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from PIL import Image

st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = pd.read_csv('https://raw.githubusercontent.com/alyeasofea/FinalAssignment/main/IRIS.csv')
iris_col = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
X = iris[iris_col]
Y = iris.species

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(pd.DataFrame({'Species': ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],}))


st.subheader('Prediction')
#st.write(iris.target_names[prediction])
st.write(pd.DataFrame({'Iris species':[prediction],}))


st.subheader('Prediction Probability')
st.write(prediction_proba)

st.write("##")
st.write("##")

image = Image.open('setosa.jpg')
st.image(image, width=150)
st.write("Learn more about : [Iris-setosa](https://en.wikipedia.org/wiki/Iris_setosa)")

st.write("##")
image = Image.open('versicolor.jpg')
st.image(image, width=140)
st.write("Learn more about : [Iris-versicolor](https://en.wikipedia.org/wiki/Iris_versicolor)")

st.write("##")
image = Image.open('virginica.jpg')
st.image(image, width=140)
st.write("Learn more about : [Iris-virginica](https://en.wikipedia.org/wiki/Iris_virginica)")
