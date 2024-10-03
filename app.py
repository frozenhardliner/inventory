import streamlit as st
from streamlit.components.v1 import html
import base64
import os
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)
# Helper function to load images as base64
def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load images as base64 encoded strings
icon1_base64 = get_image_as_base64("static/app/icon1.png")
icon2_base64 = get_image_as_base64("static/app/icon2.png")
icon3_base64 = get_image_as_base64("static/app/icon3.png")
icon4_base64 = get_image_as_base64("static/app/icon4.png")
icon5_base64 = get_image_as_base64("static/app/icon5.png")
icon6_base64 = get_image_as_base64("static/app/icon6.png")
# Path to the CSS file
css_path = os.path.join(os.getcwd(), 'static','app.css')

# Load the CSS file
with open(css_path) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# HTML code to create the grid layout with base64 encoded images
html_code = f"""
<div class="grid-container">
    <a href="/register" class="grid-item" target="_self">
        <img src="data:image/png;base64,{icon1_base64}" class="icon" alt="Регистрация нового товара">
        <p class="text">Регистрация нового товара</p>
    </a>
    <a href="/move" class="grid-item" target="_self">
        <img src="data:image/png;base64,{icon2_base64}" class="icon" alt="Перемещение товара">
        <p class="text">Перемещение товара</p>
    </a>
    <a href="/scan" class="grid-item" target="_self">
        <img src="data:image/png;base64,{icon3_base64}" class="icon" alt="Сканирование товара">
        <p class="text">Сканирование товара</p>
    </a>
    <a href="/inventory" class="grid-item" target="_self">
        <img src="data:image/png;base64,{icon4_base64}" class="icon" alt="Инвентаризация склада">
        <p class="text">Инвентаризация склада</p>
    </a>
    <a href="/registry" class="grid-item" target="_self">
        <img src="data:image/png;base64,{icon5_base64}" class="icon" alt="Реестр товаров">
        <p class="text">Реестр товаров</p>
    </a>
    <a href="/writeoff" class="grid-item" target="_self">
        <img src="data:image/png;base64,{icon6_base64}" class="icon" alt="Списание товара">
        <p class="text">Списание товара</p>
    </a>
</div>
"""

# Display the HTML in Streamlit
st.write(html_code, unsafe_allow_html=True)
