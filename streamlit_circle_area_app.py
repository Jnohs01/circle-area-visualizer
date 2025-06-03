import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set wide layout
st.set_page_config(layout="wide", page_title="Visualizing the Area of a Circle")

# Left-hand explanation panel
with st.sidebar:
    st.title("📘 Why This Works")
    st.markdown("""
    ### The Circle and Its Secret

    A circle isn’t just round—it’s a collection of **infinitely many rings**, each one unit farther from the center.

    Imagine each ring as a **thin strip** — like peeling an onion layer by layer.

    Now, unwrap those rings.

    They become **skinny rectangles**, where:
    - Height = 1 unit (our measurement resolution)
    - Width = the **circumference at that radius** (≈ 2π·r)

    If we **stack** all these skinny rectangles, the result is:
    - A total width = **π·r**
    - A total height = **r**

    That’s why:
    > **Area = π·r²**

    This is integration — adding up an infinite number of tiny measurable parts.
    """)

# Right-hand interactive display
st.title("📐 Visualizing the Area of a Circle with Stacked Rings")

# Radius input
r = st.slider("Adjust Radius", min_value=1, max_value=20, value=10)
theta = np.linspace(0, 2 * np.pi, 100)

# Visualizing stacked rectangles
fig, ax = plt.subplots(figsize=(10, 6))
for i in range(1, r + 1):
    x = i * np.pi  # approximated width of the "unwrapped" ring
    rect = plt.Rectangle((0, i - 1), x, 1, edgecolor='black', facecolor='skyblue', alpha=0.7)
    ax.add_patch(rect)
    ax.text(x + 0.3, i - 0.5, f"r={i}", verticalalignment='center')

ax.set_xlim(0, r * np.pi + 5)
ax.set_ylim(0, r)
ax.set_xlabel("Width ≈ π·r")
ax.set_ylabel("Height = r")
ax.set_title("Unwrapping Circle Rings into Rectangles")
ax.set_aspect('auto')

st.pyplot(fig)
