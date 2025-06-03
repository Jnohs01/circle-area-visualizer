import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")
st.title("Understanding the Area of a Circle")

# Sidebar explanation
with st.sidebar:
    st.header("Concept Overview")
    st.markdown("""
    The area of a circle is calculated using the formula **A = π·r²** —  
    but *where does that come from*?

    Imagine slicing the circle into thin rings, each 1 unit farther from the center.

    - Each ring has a circumference = **2πr**
    - When you **unwrap** a ring, it becomes a thin rectangle
    - As we stack all the rectangles, the height becomes **r** and total width becomes **π·r**

    Just like a rectangle has area = L × W,  
    the stacked shape has area = **π·r × r = π·r²**

    This is a visual form of integration — slicing and adding up small parts.
    """)

# Slider for resolution
num_rings = st.slider("Number of Rings (resolution)", min_value=1, max_value=100, value=20)

# Compute ring data
radii = np.linspace(0, 1, num_rings + 1)[1:]
width = 1 / num_rings
circumferences = 2 * np.pi * radii

# Layout split: visuals in one column
col1, col2 = st.columns(2)

with col1:
    st.subheader("Concentric Rings (Circle View)")
    fig1, ax1 = plt.subplots(figsize=(4, 4))
    ax1.set_aspect('equal')
    for r in radii:
        circle = plt.Circle((0, 0), r, fill=False, color='blue', linewidth=1)
        ax1.add_artist(circle)
    ax1.set_xlim(-1.1, 1.1)
    ax1.set_ylim(-1.1, 1.1)
    ax1.axis('off')
    st.pyplot(fig1, use_container_width=True)

with col2:
    st.subheader("Unwrapped Rings (Stacked Rectangles)")
    fig2, ax2 = plt.subplots(figsize=(5, 5))
    y_offset = 0
    for c in circumferences[::-1]:  # stack larger ones on bottom
        rect = plt.Rectangle((0, y_offset), c, width, color='orange', ec='black')
        ax2.add_patch(rect)
        y_offset += width
    ax2.set_xlim(0, 2 * np.pi + 1)
    ax2.set_ylim(0, 1.1)
    ax2.set_xlabel("Width ≈ π·r")
    ax2.set_ylabel("Height = r")
    ax2.set_title("Stacked Approximation")
    st.pyplot(fig2, use_container_width=True)

# Final explanatory note
st.markdown("""
---

### Why This Works

If you take many thin rings and unwrap them:

- Their total **width becomes π·r**
- Their total **height is r**

So, **Area = π·r × r = π·r²**

This is the heart of integral calculus — turning a curved shape into small pieces we can understand.
""")
