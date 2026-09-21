import streamlit as st
import random

# Lista de preguntas y respuestas
questions = [
    {
        "question": "¿Qué es Machine Learning?",
        "options": ["Un tipo de cocina", "Un campo de la IA", "Un lenguaje de programación", "Un sistema operativo"],
        "answer": "Un campo de la IA"
    },
    {
        "question": "¿Cuál de estos es aprendizaje supervisado?",
        "options": ["Regresión lineal", "K-means", "Apriori", "PCA"],
        "answer": "Regresión lineal"
    },
    {
        "question": "¿Cuál de estos es aprendizaje no supervisado?",
        "options": ["Árboles de decisión", "K-means", "Regresión logística", "Random Forest"],
        "answer": "K-means"
    },
    {
        "question": "¿Qué significa 'overfitting'?",
        "options": ["Modelo generaliza bien", "Modelo se ajusta demasiado a los datos de entrenamiento", "Modelo no aprende nada", "Modelo siempre predice lo mismo"],
        "answer": "Modelo se ajusta demasiado a los datos de entrenamiento"
    },
    {
        "question": "¿Cuál es un ejemplo de clasificación?",
        "options": ["Predecir precio de una casa", "Predecir si un correo es spam", "Predecir temperatura", "Predecir altura"],
        "answer": "Predecir si un correo es spam"
    },
    {
        "question": "¿Qué técnica se usa para reducir dimensiones?",
        "options": ["PCA", "Random Forest", "Regresión lineal", "Naive Bayes"],
        "answer": "PCA"
    },
    {
        "question": "¿Qué algoritmo se basa en árboles?",
        "options": ["Random Forest", "K-means", "PCA", "SVM"],
        "answer": "Random Forest"
    },
    {
        "question": "¿Cuál es un ejemplo de regresión?",
        "options": ["Predecir precio de una casa", "Clasificar imágenes", "Detectar spam", "Agrupar clientes"],
        "answer": "Predecir precio de una casa"
    },
    {
        "question": "¿Qué es un dataset de entrenamiento?",
        "options": ["Datos para probar el modelo", "Datos para entrenar el modelo", "Datos irrelevantes", "Datos de validación"],
        "answer": "Datos para entrenar el modelo"
    },
    {
        "question": "¿Qué mide la métrica 'accuracy'?",
        "options": ["Proporción de predicciones correctas", "Tiempo de entrenamiento", "Cantidad de datos", "Número de variables"],
        "answer": "Proporción de predicciones correctas"
    }
]

st.title("🧠 Quiz de Machine Learning (Nivel Básico)")

# Seleccionar 5 preguntas aleatorias
selected_questions = random.sample(questions, 5)

user_answers = []
score = 0

# Mostrar preguntas
for i, q in enumerate(selected_questions):
    st.subheader(f"Pregunta {i+1}: {q['question']}")
    answer = st.radio("Selecciona una opción:", q["options"], key=i)
    user_answers.append((q, answer))

# Botón para enviar respuestas
if st.button("Enviar respuestas"):
    correct = 0
    for q, ans in user_answers:
        if ans == q["answer"]:
            correct += 1

    st.write(f"Tu puntaje: {correct}/{len(selected_questions)}")

    if correct == len(selected_questions):
        st.success("¡Excelente! Todas correctas 🎉")
        st.balloons()  # Animación de celebración
    else:
        st.warning("Sigue practicando, ¡vas muy bien!")


# Seleccionar 5 preguntas

