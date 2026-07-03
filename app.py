import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load('iris_production_model (1).pkl') 

st.set_page_config(page_title="Iris Pipeline Dashboard", page_icon="🚀", layout="centered")
st.title("🚀 Interactive Iris ML Pipeline")
st.markdown("---")
st.markdown("### Real-time Inference Dashboard")

st.sidebar.header("🔧 Input Features")
sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.1, step=0.1)
sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.5, step=0.1)
petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.4, step=0.1)
petal_width = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2, step=0.1)

features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

if st.button("🔮 Run Pipeline Inference"):
    prediction = model.predict(features)
    species = prediction[0]
    
    st.markdown("### 📊 Pipeline Output:")
    if "setosa" in species.lower():
        st.success(f"🌸 **Predicted Species: {species}**")
    elif "versicolor" in species.lower():
        st.warning(f"🌻 **Predicted Species: {species}**")
    else:
        st.info(f"🌺 **Predicted Species: {species}**")
