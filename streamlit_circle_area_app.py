import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")

# Left column: Explanation
with st.sidebar:
    st.header("Why This Works")
    st.markdown("""
    We are exploring the area of a circle by breaking it down into **rings**.

    Each ring is 1 unit thicker than the last — it's like using a ruler to measure the circle in layers.

    Now, imagine you **unwrap** each ring. It turns into a thin rectangle!

    The **height** of each rectangle = 1 unit of radial thickness.  
    The **width** = the **circumference** at that radius = 2πr

    If we stack all these rectangles from the center outward, we create a **triangle-like shape**.

    When we let the number of rings grow toward infinity:
    - The **base** becomes π·r (half the circumference)
    - The **height** becomes r

    So the total area = base × height = π·r × r = π·r²

    This is the **essence of integration** — summing many infinitely small parts.
    """)

# Right column: Visuals
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Circle with Concentric Rings")
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_aspect('equal')
    num_rings = 20
    for r in range(1, num_rings + 1):
        circle = plt.Circle((0, 0), r, fill=False, color='blue', linewidth=0.8)
        ax.add_artist(circle)
    ax.set_xlim(-num_rings - 1, num_rings + 1)
    ax.set_ylim(-num_rings - 1, num_rings + 1)
    ax.axis('off')
    st.pyplot(fig)

with col2:
    st.subheader("Unwrapped and Stacked Rings")
    fig2, ax2 = plt.subplots(figsize=(5, 5))
    for r in range(1, num_rings + 1):
        width = 2 * np.pi * r
        ax2.add_patch(plt.Rectangle((0, r), width, 1, edgecolor='green', facecolor='lightgreen'))
    ax2.set_xlim(0, 2 * np.pi * num_rings + 5)
    ax2.set_ylim(0, num_rings + 2)
    ax2.set_xlabel("Unwrapped Circumference (2πr)")
    ax2.set_ylabel("Radius (r)")
    ax2.set_title("Stacked Thin Rectangles")
    st.pyplot(fig2)
