
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

st.set_page_config(layout="wide")
st.title("Understanding the Area of a Circle Visually")
st.write("""
This visual explanation shows how the area of a circle (A = πr²) can be understood 
by breaking it into thin concentric rings and unwrapping them into rectangles. 
Each ring is like a slice of the circle with increasing circumference. 
When unwrapped, they form a triangle-like or rectangular shape with a height of r and base of 2πr.
""")
st.write("Try adjusting the number of rings to see how the approximation improves.")

# Input parameters
num_rings = st.slider("Number of Rings", 1, 200, 30)
r_max = 5
ring_thickness = r_max / num_rings

# Set up figure
fig, ax = plt.subplots(figsize=(4, 3))
ax.set_xlim(-1, r_max * np.pi + 1)
ax.set_ylim(-r_max - 1, r_max + 1)
ax.set_aspect('equal')
ax.axis('off')

# Draw the "unwrapped" rings
for i in range(num_rings):
    r_outer = (i + 1) * ring_thickness
    wedge = Wedge(center=((i + 0.5) * ring_thickness * np.pi, 0),
                  r=r_outer,
                  theta1=0,
                  theta2=360,
                  width=ring_thickness,
                  color='skyblue',
                  alpha=0.7)
    ax.add_patch(wedge)

st.pyplot(fig)
