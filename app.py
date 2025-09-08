import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Deserción Universitaria", page_icon="🎓", layout="wide")
st.title("🎓 Sistema de Alerta Temprana para Deserción Estudiantil")
st.markdown("Este sistema simula una predicción de riesgo académico basada en variables clave del estudiante.")

# Sidebar para entrada de datos
st.sidebar.header("📋 Información del Estudiante")

curricular_2nd_approved = st.sidebar.slider("Materias 2º semestre aprobadas", 0, 10, 5)
academic_efficiency = st.sidebar.slider("Eficiencia académica (%)", 0, 100, 75)
tuition_fees_up_to_date = st.sidebar.selectbox("Matrícula al día", ["Sí", "No"])
curricular_2nd_enrolled = st.sidebar.slider("Materias 2º semestre inscritas", 0, 10, 6)
curricular_2nd_evaluations = st.sidebar.slider("Evaluaciones 2º semestre", 0, 20, 10)
educational_special_needs = st.sidebar.selectbox("Necesidades educativas especiales", ["Sí", "No"])
academic_load = st.sidebar.slider("Carga académica (ECTS)", 0, 60, 30)
scholarship_holder = st.sidebar.selectbox("Becado", ["Sí", "No"])
curricular_1st_approved = st.sidebar.slider("Materias 1º semestre aprobadas", 0, 10, 4)
curricular_1st_credited = st.sidebar.slider("Materias 1º semestre convalidadas", 0, 10, 2)

# Botón para predecir
if st.sidebar.button("🔍 Predecir Riesgo"):
    # Simulación de puntuación de riesgo
    score = (
        (10 - curricular_2nd_approved) * 0.2 +
        (1 - academic_efficiency / 100) * 0.3 +
        (0 if tuition_fees_up_to_date == "Sí" else 0.1) +
        (educational_special_needs == "Sí") * 0.1 +
        (0 if scholarship_holder == "Sí" else 0.1)
    )

    # Clasificación de riesgo
    if score > 0.5:
        risk_level = "🚨 Alto Riesgo"
    elif score > 0.3:
        risk_level = "⚠️ Riesgo Medio"
    else:
        risk_level = "✅ Bajo Riesgo"

    confidence = 1 - score
    st.subheader("📊 Resultados de la Predicción")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Nivel de Riesgo", risk_level)
    with col2:
        st.metric("Confianza", f"{confidence*100:.1f}%")
    with col3:
        st.metric("Score de Riesgo", f"{score*100:.1f}/100")

    st.progress(score, text=f"Nivel de riesgo: {risk_level}")

    st.subheader("📈 Impacto de Factores")
    impact_data = {
        "Materias 2º semestre aprobadas": (10 - curricular_2nd_approved) * 0.2,
        "Eficiencia académica": (1 - academic_efficiency / 100) * 0.3,
        "Matrícula al día": 0 if tuition_fees_up_to_date == "Sí" else 0.1,
        "Necesidades especiales": 0.1 if educational_special_needs == "Sí" else 0,
        "Beca": 0 if scholarship_holder == "Sí" else 0.1
    }

    chart_df = pd.DataFrame({
        "Factor": list(impact_data.keys()),
        "Impacto": list(impact_data.values())
    })

    st.bar_chart(chart_df.set_index("Factor"))

    st.subheader("📋 Detalles del Estudiante")
    st.write(f"• Materias aprobadas (2º): {curricular_2nd_approved}")
    st.write(f"• Eficiencia académica: {academic_efficiency}%")
    st.write(f"• Matrícula al día: {tuition_fees_up_to_date}")
    st.write(f"• Necesidades especiales: {educational_special_needs}")
    st.write(f"• Becado: {scholarship_holder}")

else:
    st.info("👈 Introduce los datos en la barra lateral y pulsa 'Predecir Riesgo'.")
