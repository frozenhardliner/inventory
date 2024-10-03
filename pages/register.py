import streamlit as st
import base64
import os
from streamlit_extras.stylable_container import stylable_container
# Helper function to load images as base64
def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load images as base64 encoded strings
icon1_base64 = get_image_as_base64("static/register/layout1.png")
icon2_base64 = get_image_as_base64("static/register/layout2.png")
icon3_base64 = get_image_as_base64("static/register/layout3.png")
icon4_base64 = get_image_as_base64("static/register/layout4.png")
icon5_base64 = get_image_as_base64("static/register/icon.png")
# Path to the CSS file
css_path = os.path.join(os.getcwd(), 'static', 'register.css')

# Load the CSS file
with open(css_path) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Breadcrumb navigation
st.markdown(f"""
<div class="breadcrumb">
    <a href="/" class="breadcrumb-link" target="_self">
        <div class="breadcrumb-home">
            <img src="data:image/png;base64,{icon5_base64}" class="breadcrumb-icon" alt="Главная"> Главная
        </div>
    </a> 
    <span class="breadcrumb-current">Регистрация нового товара</span>
</div>
""", unsafe_allow_html=True)
st.markdown("<hr class='divider'>", unsafe_allow_html=True)
# Title or instruction
st.markdown("<h2 class='instruction-title'>Выберите количество страниц и ориентацию документа</h2>", unsafe_allow_html=True)

# Radio button options
options = {
    "1 страница Портретная": f"<img src='data:image/png;base64,{icon1_base64}' alt='A4 Portrait'>",
    "1 страница Альбомная": f"<img src='data:image/png;base64,{icon2_base64}' alt='A4 Landscape'>",
    "2 страницы Портретные": f"<div class='stacked-images'><img src='data:image/png;base64,{icon3_base64}' alt='Two Portrait'><img src='data:image/png;base64,{icon3_base64}' alt='Two Portrait'></div>",
    "2 страницы Альбомные": f"<div class='stacked-images'><img src='data:image/png;base64,{icon4_base64}' alt='Two Landscape'><img src='data:image/png;base64,{icon4_base64}' alt='Two Landscape'></div>"
}
col1,col2,col3 = st.columns(3)
# Create a radio button for selection
selected_option = col1.radio(
    "Выберите ориентацию",
    options.keys(),
    index=0
)

# Display the selected card and image
html_code = f"""

<div class="card-image">
    {options[selected_option]}
</div>

"""
with col2:
    # Display the card layout
    st.write(html_code, unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Custom styling for all Streamlit buttons */
    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        font-size: 16px;
        cursor: pointer;
        transition-duration: 0.4s;
    }

    /* Hover effect for buttons */
    div.stButton > button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }

    /* Disabled button style */
    div.stButton > button:disabled {
        background-color: #EAEAEA;
        color: #999999;
        border: none;
        cursor: not-allowed;
    }
    </style>
""", unsafe_allow_html=True)

if selected_option:
    # Button is enabled and styled
    if st.button("Начать сканирование"):
        st.success(f"Started scanning for {selected_option}!")
else:
    # Button is disabled using key
    st.button("Начать сканирование", disabled=True)