import streamlit as st


st.title("Gordon Growth Model and Extensions")


st.write(r"""
Defining dividend growth as:
         """)


st.latex(r"""
g(t) = \frac{D(t+1)}{D(t)} - 1
""")

st.write(r"""So that $D(t+1) = D(t)(1 + g(t))$ and $D(t+2) = D(t)(1 + g(t))(1 + g(t+1))$. Then the price becomes:""")

st.latex(r"""
         \begin{aligned}
p(t) = D(t) \sum_{i=0}^{\infty} \mathbb{E}_{(t)} \left[ \frac{(1 + g(t))(1 + g(t+1)) \cdots (1 + g(t+i-1))}{\prod_{j=0}^{i-1}(1 + k_e(t+j))} \right] \\
            = D(t) \sum_{i=0}^{\infty} \mathbb{E}_{(t)} \left[ \prod_{j=0}^{i} \frac{(1 + g(t+j))}{(1 + k_e(t+j))} \right]
         \end{aligned}
""")

st.write(r"""
         Assuming a constant dividend growth rate $g(t+j) = g$ and a constant discounting factor $k_e(t+j) = k_e$, we can simplify the price to:""")

st.latex(r"""
p(t) = D(t) \sum_{i=0}^{\infty} \left( \frac{(1 + g)^{i}}{(1 + k_e)^{i}} \right)
""")

st.write(r"""This is a geometric series that converges if $k_e > g$ and can be summed up to give:""")

st.latex(r"""
p^G(t) = \frac{D(t)(1 + g)}{k_e - g}
""")

st.write(r"""or:""")

st.latex(r"""
p^G(t) = \frac{D(t+1)}{k_e - g}
""")