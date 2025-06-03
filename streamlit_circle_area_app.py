import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Circle Area Visualizer", layout="centered")
st.title("Visualizing the Area of a Circle")
st.markdown("Each ring acts like a thin rectangle. Let's unwrap it!")

# Slider for number of rings (resolution)
n_rings = st.slider("Number of rings", min_value=3, max_value=100, value=20)

radius = 1
dr = radius / n_rings
radii = np.linspace(0, radius, n_rings, endpoint=False)
areas = []

# Setup plot: circle with rings
fig1, ax1 = plt.subplots(figsize=(4, 4))
ax1.set_aspect("equal")
for r in radii:
    circle = plt.Circle((0, 0), r + dr, fill=False, color='blue', alpha=0.6)
    ax1.add_artist(circle)
    areas.append(2 * np.pi * r * dr)

ax1.set_xlim(-1.1, 1.1)
ax1.set_ylim(-1.1, 1.1)
ax1.set_title("Circle made of thin rings", fontsize=10)
ax1.axis("off")

# Wrap in container with max width
with st.container():
    st.markdown("<div style='max-width: 500px; margin: auto;'>", unsafe_allow_html=True)
    st.pyplot(fig1)
    st.markdown("</div>", unsafe_allow_html=True)

# Setup plot: unwrapped into rectangles
fig2, ax2 = plt.subplots(figsize=(4, 3))
for i, r in enumerate(radii):
    w = 2 * np.pi * r
    ax2.barh(i, width=w, height=1, left=0, color='green', alpha=0.5)

ax2.set_title("Unwrapped: Stacked rectangles (each ring)", fontsize=10)
ax2.set_xlabel("Width = Circumference of ring")
ax2.set_ylabel("Each bar = 1 ring thick")
ax2.invert_yaxis()  # top ring at top
ax2.tick_params(labelsize=8)

with st.container():
    st.markdown("<div style='max-width: 600px; margin: auto;'>", unsafe_allow_html=True)
    st.pyplot(fig2)
    st.markdown("</div>", unsafe_allow_html=True)

# Final explanation
st.markdown("""
---
### Why this works

If you stack these skinny rectangles and let the number grow toward infinity:

- The total width becomes **π·r**
- The total height becomes **r**

So, the **area of a circle = π·r²**

This is the essence of integration — adding infinitely thin pieces!
""")
