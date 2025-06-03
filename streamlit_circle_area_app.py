import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("Understanding the Area of a Circle")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### Concept Overview")
    st.markdown("""
    The area of a circle is calculated using the formula **A = π·r²**.  
    But where does that come from?

    Imagine slicing the circle into thin rings, each one a bit further from the center.

    - Each **ring** has a circumference = **2πr**
    - When **unwrapped**, it becomes a **rectangle**
    - The width of the rectangle becomes **π·r**, and its height is **r**

    This process — slicing and stacking — is what integration does.

    > Just like counting squares in a rectangle gives Area = L × W,  
    > stacking thin rings gives Area = π × r × r = π·r²
    """)

with col2:
    st.image("images/concentric_rings.png", caption="Circle built with thin concentric rings", use_column_width=True)
    st.image("images/unwrapped_rings.png", caption="Unwrapped rings stacked into a rectangle", use_column_width=True)
