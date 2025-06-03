import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set vertical layout and left sidebar
st.set_page_config(layout="wide")

# Sidebar explanation
with st.sidebar:
    st.header("Understanding Area of a Circle")
    st.markdown("""
    ### Why This Visualization Works

    We begin by slicing the circle into **concentric rings** — each one is a small unit further from the center.

    Each ring has a **circumference** of `2πr`.  
    When you “unwrap” one ring, it becomes a thin rectangle:

    - **Width** = `2πr` (its length around)
    - **Height** = `1` unit (our measurement resolution)

    Stacking these rectangles forms a right triangle as rings approach infinitesimal thickness.

    - **Base** = π·r
    - **Height** = r

    So the **area of the circle** becomes:

    **Area = ½ × base × height = ½ × π·r × r = π·r²**

    This is what **integration** means: summing up infinitely many small parts.
    """)

# Title
st.title("Visualizing π·r² — Area of a Circle from First Principles")

# Concentric rings
fig1, ax1 = plt.subplots(figsize=(6, 6))
ax1.set_aspect('equal')
r_max = 5
num_rings = 50
radii = np.linspace(0, r_max, num_rings)

for r in radii:
    circle = plt.Circle((0, 0), r, fill=False, color='blue', linewidth=0.8)
    ax1.add_artist(circle)

ax1.set_xlim(-r_max - 1, r_max + 1)
ax1.set_ylim(-r_max - 1, r_max + 1)
ax1.axis('off')
st.pyplot(fig1)

# Unwrapped rectangles
fig2, ax2 = plt.subplots(figsize=(6, 6))
for i, r in enumerate(radii):
    width = 2 * np.pi * r
    rect = plt.Rectangle((0, i), width, 1, facecolor='lightblue', edgecolor='blue')
    ax2.add_patch(rect)

ax2.set_xlim(0, 2 * np.pi * r_max)
ax2.set_ylim(0, num_rings)
ax2.set_xlabel("Unwrapped Circumference")
ax2.set_ylabel("Radial Step")
ax2.set_title("Unwrapped Rings Forming a Triangle")
st.pyplot(fig2)
