import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")
st.title("Understanding the Area of a Circle Visually")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Visual Explanation")
    st.markdown("""
    This visualization helps you **see** why the area of a circle is \( \pi r^2 \).

    1. The circle is divided into **concentric rings** — each representing a unit of distance from the center.
    2. These rings can be imagined as **thin strips**.
    3. When we **unwrap** and **stack** these strips (like slicing an orange and lining up the peels),
       they form a shape close to a rectangle.
    4. The **height** of this rectangle becomes the radius \( r \), and the **width** becomes half the circumference \( \pi r \).

    So the area becomes:

    \[ \text{Area} = \pi r \times r = \pi r^2 \]

    This is the intuition behind **integration** — summing infinitely small pieces to get a whole.
    """)

with col2:
    st.subheader("Concentric Rings and Stacked Representation")

    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Left: Concentric circles
    ax1 = axs[0]
    ax1.set_aspect('equal')
    r = 1
    rings = 20
    for i in range(1, rings + 1):
        circle = plt.Circle((0, 0), r * i / rings, color='lightblue', fill=False)
        ax1.add_patch(circle)
    ax1.set_xlim(-1.1, 1.1)
    ax1.set_ylim(-1.1, 1.1)
    ax1.set_title("Concentric Rings")
    ax1.axis('off')

    # Right: Unwrapped and stacked rectangles
    ax2 = axs[1]
    for i in range(rings):
        width = 2 * np.pi * (r * i / rings)
        ax2.barh(i, width, height=1, color='lightgreen', edgecolor='black')
    ax2.set_title("Stacked Ring Strips")
    ax2.set_xlabel("Approx. Unwrapped Length")
    ax2.set_ylabel("Ring Index")

    st.pyplot(fig)

