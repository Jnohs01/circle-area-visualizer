import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")
st.title("Understanding the Area of a Circle")

# Sidebar explanation
st.sidebar.markdown("### Concept Overview")
st.sidebar.markdown("""
The area of a circle is calculated using the formula **A = π·r²**.  
But where does that come from?

- Imagine slicing the circle into **thin rings**, each one a bit further from the center.  
- Each ring has **circumference = 2πr**  
- When **unwrapped**, it becomes a rectangle.  
- The **width** of the rectangle becomes **π·r**, and its **height** is **r**.

This process — slicing and stacking — is what **integration** does.

Just like counting squares in a rectangle gives **Area = L × W**,  
stacking thin rings gives **Area = π × r × r = π·r²**
""")

# Slider for resolution
num_rings = st.slider("Number of Rings (resolution)", min_value=1, max_value=100, value=20)

def draw_concentric_rings(num_rings):
    fig, ax = plt.subplots(figsize=(4, 4))
    for i in range(num_rings):
        r = (i + 1) / num_rings
        circle = plt.Circle((0, 0), r, color='skyblue', fill=False, linewidth=1)
        ax.add_patch(circle)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig

def draw_unwrapped_rings(num_rings):
    fig, ax = plt.subplots(figsize=(5, 2))
    for i in range(num_rings):
        r = (i + 1) / num_rings
        height = 1 / num_rings
        width = 2 * np.pi * r / 2  # Scaled down to fit
        ax.add_patch(plt.Rectangle((0, i * height), width, height, edgecolor='orange', facecolor='none', lw=1))
    ax.set_xlim(0, np.pi)  # Keep this tighter
    ax.set_ylim(0, 1)
    ax.set_aspect('auto')
    ax.axis('off')
    return fig

# Layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 1. Circle Sliced into Concentric Rings")
    st.pyplot(draw_concentric_rings(num_rings))

with col2:
    st.markdown("#### 2. Rings Unwrapped and Stacked as Rectangles")
    st.pyplot(draw_unwrapped_rings(num_rings))

# Optional footer
st.markdown("---")
st.markdown(f"With {num_rings} ring{'s' if num_rings > 1 else ''}, the approximation becomes clearer: "
            f"the unwrapped shape becomes a near-rectangle, whose area approaches π·r² as resolution increases.")
