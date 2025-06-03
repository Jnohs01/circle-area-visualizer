import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")
st.title("Understanding the Area of a Circle")

# Commentary area
with st.sidebar:
    st.markdown("### Concept Overview")
    st.markdown("""
    The area of a circle is calculated using the formula $A = \\pi \\cdot r^2$.
    
    But where does that come from?
    
    - Imagine slicing the circle into thin rings, each a bit further from the center.
    - Each ring has a circumference = $2\\pi r$
    - When unwrapped, it becomes a rectangle.
    - The width of the rectangle becomes $\\pi r$, and its height is $r$.
    - This slicing and stacking process is what **integration** does.
    
    Just like counting squares in a rectangle gives Area = L × W,  
    stacking thin rings gives Area = $\\pi \\cdot r \\cdot r = \\pi r^2$.
    """)

# Slider to control number of rings
num_rings = st.slider("Number of rings (resolution)", min_value=1, max_value=100, value=20)

# --------- Circle with Concentric Rings ---------
fig_circle, ax1 = plt.subplots(figsize=(4, 4))
for i in range(num_rings):
    radius = (i + 1) / num_rings
    ring = plt.Circle((0, 0), radius=radius, fill=False, edgecolor='blue')
    ax1.add_patch(ring)
ax1.set_aspect('equal')
ax1.set_xlim(-1.1, 1.1)
ax1.set_ylim(-1.1, 1.1)
ax1.axis('off')

# --------- Unwrapped into Stacked Rectangles ---------
fig_rect, ax2 = plt.subplots(figsize=(6, 3))
total_height = 1.0
height = total_height / num_rings
for i in range(num_rings):
    r = (i + 0.5) / num_rings
    width = 2 * np.pi * r / num_rings
    ax2.add_patch(plt.Rectangle((0, i * height), width, height, fill=False, edgecolor='green'))
ax2.set_xlim(0, 2 * np.pi)
ax2.set_ylim(0, 1)
ax2.set_aspect('auto')
ax2.axis('off')

# Layout: Show both visuals vertically
st.pyplot(fig_circle)
st.pyplot(fig_rect)
