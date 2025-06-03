import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")

# Sidebar explanation
with st.sidebar:
    st.markdown("## Understanding the Area of a Circle")
    st.markdown("""
**Where does A = π·r² come from?**

Imagine slicing a circle into **thin rings**.

Each ring has:
- Circumference = 2πr
- Tiny thickness = dr

Unwrapping a ring gives a thin **rectangle**.

Stacking all rings from center to edge forms a triangle-like shape:
- Height = r
- Base = πr

So:  
**Area = base × height = πr × r = π·r²**

This is what **integration** does — it adds up infinitely thin slices.
""")

# Slider
num_rings = st.slider("Number of rings (resolution)", 1, 100, 30)
radius = 1
ring_thickness = radius / num_rings

# Concentric circle visualization
fig1, ax1 = plt.subplots(figsize=(4, 4))
ax1.set_aspect('equal')
for i in range(num_rings):
    r = ring_thickness * (i + 1)
    circle = plt.Circle((0, 0), r, fill=False, color='blue', linewidth=0.8)
    ax1.add_patch(circle)
ax1.set_xlim(-radius - 0.1, radius + 0.1)
ax1.set_ylim(-radius - 0.1, radius + 0.1)
ax1.axis('off')
st.pyplot(fig1)

# Unwrapped rings as stacked rectangles
fig2, ax2 = plt.subplots(figsize=(6, 2.5))
for i in range(num_rings):
    r1 = ring_thickness * i
    r2 = ring_thickness * (i + 1)
    avg_r = (r1 + r2) / 2
    width = 2 * np.pi * avg_r
    height = ring_thickness
    ax2.add_patch(plt.Rectangle((0, i * ring_thickness), width, height, fill=False, edgecolor='green', linewidth=0.8))
ax2.set_xlim(0, 2 * np.pi * radius)
ax2.set_ylim(0, radius)
ax2.set_title("Stacked Unwrapped Rings")
ax2.set_xlabel("Width ~ 2πr")
ax2.set_ylabel("Height = r")
ax2.grid(False)
st.pyplot(fig2)
