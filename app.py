import random
import streamlit as st

# Importamos tu base de datos de preguntas
from datos_codigo import preguntas_lista

# Configuración de la página web
st.set_page_config(
    page_title="Preguntador PCP", page_icon="📚", layout="centered"
)

# Estilo visual limpio y moderno
st.markdown(
    """
    <style>
        .stButton button {
            width: 100%;
            border-radius: 8px;
            font-weight: bold;
            padding: 10px;
        }
        .pregunta-box {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Título de la app
st.title("📚 Preguntador de Teoría - PCP")
st.markdown(f"*Total de preguntas en la base: {len(preguntas_lista)}*")
st.divider()

# Control de estado
if "current_q" not in st.session_state:
  st.session_state.current_q = None
if "show_ans" not in st.session_state:
  st.session_state.show_ans = False


def nueva_pregunta():
  st.session_state.current_q = random.choice(preguntas_lista)
  st.session_state.show_ans = False


def mostrar_respuesta():
  st.session_state.show_ans = True


# Botones principales en dos columnas
col1, col2 = st.columns(2)
with col1:
  st.button(
      "🔄 Siguiente Pregunta",
      on_click=nueva_pregunta,
      type="primary",
      use_container_width=True,
  )

with col2:
  if st.session_state.current_q is not None:
    st.button(
        "👁️ Mostrar Respuesta",
        on_click=mostrar_respuesta,
        use_container_width=True,
    )
  else:
    st.button(
        "👁️ Mostrar Respuesta", disabled=True, use_container_width=True
    )

st.write("")

# Mostrar la pregunta actual si existe
if st.session_state.current_q is not None:
  q = st.session_state.current_q
  num = q.get("N°", "")
  tema = q.get("Tema", "")
  pregunta = q.get("Pregunta", "")
  respuesta = q.get("Respuesta", "")

  # Caja visual para la pregunta
  st.markdown(
      f"""
    <div class="pregunta-box">
        <p style="color: #555; font-size: 14px; margin-bottom: 5px;"><b>Tema:</b> [{num}] {tema}</p>
        <h3 style="color: #222; margin-top: 0;">{pregunta}</h3>
    </div>
    """,
      unsafe_allow_html=True,
  )

  # Mostrar la respuesta usando componentes nativos seguros para textos largos
  if st.session_state.show_ans:
    with st.container(border=True):
      st.markdown("#### 💡 Respuesta:")
      st.write(respuesta)
  else:
    st.info(
        "💡 Respuesta oculta. Haz clic en 'Mostrar Respuesta' cuando estés listo."
    )
else:
  st.info(
      '👋 ¡Bienvenido! Haz clic en el botón **"Siguiente Pregunta"** para'
      " comenzar a estudiar."
  )