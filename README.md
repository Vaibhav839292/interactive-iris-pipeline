# 🚀 Interactive Iris Machine Learning Pipeline

An end-to-end Machine Learning pipeline featuring multi-model benchmarking, interactive visualizations, and production-ready model serialization (`.pkl`). This project is fully deployed on the cloud for real-time interactive predictions.

🔗 **Live Deployment Link:** [Click Here to View Live App](https://interactive-iris-pipeline-ndwpqtdzs4q2eut7fjufyk.streamlit.app/)

---

## 🌟 Key Highlights

* **Dynamic Data Analytics:** Integrated interactive visualizations showcasing data distribution and morphology.
* **Animated Feature Importance:** Step-by-step dynamic rendering of features that impact the model's predictions.
* **Multi-Model Benchmarking:** Evaluated multiple classifiers (including Decision Trees, Random Forest, etc.) to find the most optimal model.
* **Production Deployment:** Serialized the best-performing model using `joblib` and created a web dashboard using Streamlit for instant inference.

---

## 🛠️ Tech Stack & Libraries

* **Language:** Python
* **Environment:** Kaggle Notebooks
* **Framework:** Streamlit (for Cloud Deployment)
* **Core Libraries:** `scikit-learn`, `joblib`, `numpy`, `pandas`, `matplotlib`, `seaborn`

---

## 📂 Project Structure

```text
├── iris pipeline.ipynb          # Core Kaggle notebook with EDA, training & benchmarking
├── iris_production_model (1).pkl # Serialized production-ready trained model artifact
├── app.py                      # Streamlit web application server script
├── requirements.txt            # Project dependencies for cloud hosting
└── README.md                   # Project documentation and live links
