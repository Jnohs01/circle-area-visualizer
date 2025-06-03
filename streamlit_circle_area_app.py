import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title and description
st.title("Visualizing the Area of a Circle")
st.write("""
This app visualizes the idea that the **area of a circle** can be understood by layering concentric rings.
Each ring represents 1 unit of radius—**a unit of measurement**, not physical thickness.
Unwrapping those rings forms a triangle-like shape with height `r` and base `πr`, giving area `πr²`.
""")

# User input: radius slider
radius = st.slider("Choose radius of the circle", 1, 20, 10)

# Create the figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.axis('off')

# Draw concentric circles (rings)
for r in range(1, radius + 1):
    circle = plt.Circle((0, 0), r, fill=False, color='blue', linewidth=1.5)
    ax.add_patch(circle)

# Annotate radius
ax.plot(0, 0, 'ro')  # center point
ax.text(radius + 0.5, 0, f'r = {radius}', fontsize=12)

# Set plot limits
ax.set_xlim(-radius - 2, radius + 2)
ax.set_ylim(-radius - 2, radius + 2)

# Display the figure
st.pyplot(fig)

# Explanation section
with st.expander("📘 See how this leads to the formula A = πr²"):
    st.markdown(f"""
    - Each **ring** is one unit of distance from the center—think of it as the resolution of your measuring device.
    - The outer ring is **longer** than the inner one—its length is roughly the **circumference** at that radius.
    - If you “unwrap” each ring and stack them, you form a shape similar to a triangle with:
        - **Base ≈ πr** (the average of all circumferences),
        - **Height = r** (total number of rings).
    - So, the area is **base × height = πr × r = πr²**.

    This visual is a *tautology*—a self-reinforcing truth built directly from the logic of the geometry.
    """)


