import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")

st.sidebar.title("Circle Area Visualizer")
num_rings = st.sidebar.slider("Number of Rings", min_value=5, max_value=100, value=20, step=1)

st.sidebar.markdown("""
### Concept Overview

We slice the circle into **thin rings**.
- Each ring becomes a **narrow rectangle** when unwrapped.
- Stacking these rectangles gives us a full shape with:
  - Height = radius
  - Width = π·radius
- So, **Area = π·r²** — just like adding up all the tiny pieces.

This is the essence of **integration**.
""")

radius = 1
radii = np.linspace(0, radius, num_rings + 1)

# Plotting the concentric rings
fig1, ax1 = plt.subplots(figsize=(4, 4))
for i in range(num_rings):
    circle = plt.Circle((0, 0), radii[i+1], color='blue', alpha=0.2)
    ax1.add_artist(circle)
ax1.set_xlim(-radius, radius)
ax1.set_ylim(-radius, radius)
ax1.set_aspect('equal')
ax1.axis('off')
st.markdown("### Circle composed of concentric rings:")
st.pyplot(fig1, use_container_width=False)

# Plotting the unwrapped rectangles
fig2, ax2 = plt.subplots(figsize=(4, 4))
for i in range(num_rings):
    r_mid = (radii[i] + radii[i+1]) / 2
    height = radii[i+1] - radii[i]
    width = 2 * np.pi * r_mid
    ax2.barh(y=r_mid, width=width, height=height, left=0, color='orange', edgecolor='black', alpha=0.6)
ax2.set_xlabel("Unwrapped Width (π·r)")
ax2.set_ylabel("Distance from Center (r)")
ax2.set_title("Unwrapped Rings → Rectangles")
ax2.set_xlim(0, 2 * np.pi * radius)
ax2.set_ylim(0, radius)
st.markdown("### Those rings unwrapped into stacked rectangles:")
st.pyplot(fig2, use_container_width=False)
