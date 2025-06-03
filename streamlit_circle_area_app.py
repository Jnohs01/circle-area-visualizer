import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Configure layout
st.set_page_config(layout="wide")

# Sidebar Explanation
with st.sidebar:
    st.header("🧠 Visual Logic: Area of a Circle")
    st.markdown("""
    #### Why this works

    We're not memorizing formulas — we're building them.

    1. We slice the circle into thin **concentric rings**.
    2. Each ring, when unwrapped, becomes a **thin rectangle**.
    3. Stack these rectangles — they form a **triangle**.
    
    - Triangle base: π·r  
    - Triangle height: r  
    - Triangle area: ½·base·height = **π·r²**

    This is integration: summing small slices to find total area.
    """)

# Scrollable container
with st.container():
    st.title("🔵 Area of a Circle — Built From Rings")

    # --- Plot 1: Concentric Rings ---
    st.subheader("Step 1: Concentric Rings Inside a Circle")
    fig1, ax1 = plt.subplots(figsize=(5, 5))
    ax1.set_aspect('equal')
    r_max = 5
    num_rings = 50
    radii = np.linspace(0, r_max, num_rings)

    for r in radii:
        circle = plt.Circle((0, 0), r, fill=False, color='blue', linewidth=0.6)
        ax1.add_artist(circle)

    ax1.set_xlim(-r_max - 1, r_max + 1)
    ax1.set_ylim(-r_max - 1, r_max + 1)
    ax1.axis('off')
    st.pyplot(fig1)

    # --- Plot 2: Unwrapped Rectangles ---
    st.subheader("Step 2: Unwrapped Rings = Stacked Rectangles")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    for i, r in enumerate(radii):
        width = 2 * np.pi * r
        rect = plt.Rectangle((0, i), width, 1, facecolor='lightblue', edgecolor='blue')
        ax2.add_patch(rect)

    ax2.set_xlim(0, 2 * np.pi * r_max)
    ax2.set_ylim(0, num_rings)
    ax2.set_xlabel("Unwrapped Circumference")
    ax2.set_ylabel("Radial Step")
    ax2.set_title("Unwrapped Rings Form a Right Triangle")
    st.pyplot(fig2)
