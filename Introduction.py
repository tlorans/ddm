import streamlit as st

st.title("Dividend Discount Model: from Deterministic to Stochastic Models")


st.write(r"""Stock valuation is one of the basic aspects of financial markets. 
         Discussion about the fair price of a stock, or its overpricing and underpricing, have always been of paramount importance to investors. 
         Williams (1938) was the first to recognise that market prices and fundamental values are "separate and distinct things not to be confused".
         In his work, he states that an asset's intrinsic long-term value is the present value of all future cash flows, i.e. dividends and future selling price.
         """)

st.write(r"""Let $P(t)$ be the random variable giving the fundamental value of a stock at time $t \in \mathbb{N}$. Let $D(t)$ be the dividend at time $t \in \mathbb{N}$,
         also assumed to be a random variable, and denote by $k_e(t)$ the required rate of return on the stock at time $t$. 
         If we buy a stock a time $t$ and plan to sell it at time $t+1$, the price $p(t) := \mathbb{E}_{(t)}[P(t+1)]$ that we pay is the expected value 
         of the stock price at time $t+1$ plus the cash flows distributed by the company, all discounted at an appropriate measure of risk $k_e(t)$:
         """)

st.latex(r"""
p(t) = \mathbb{E}_{(t)} \left[ \frac{D(t+1) + P(t+1)}{1 + k_e(t)} \right]
""")

st.write(r"""If we buy and hold the stock indefinitely, and assuming:""")

st.latex(r"""
\lim_{i \to \infty} \mathbb{E}_{(t)}[\frac{P(t+i)}{\prod_{j=0}^{i}(1 + k_e(t+j))}] = 0
""")

st.write(r"""then the price we pay is the expected value of all future cash flows in the form of dividends,""")

st.latex(r"""
p(t) = \sum_{i=1}^{\infty} \mathbb{E}_{(t)} \left[ \frac{D(t+i)}{\prod_{j=0}^{i-1}(1 + k_e(t+j))} \right]
""")

st.write(r"""To solve this equation, we have to identify two inputs, namely future dividends and the required measure of risk. 
         When estimating future dividends, because of the impossibility of making predictions through to infinity, many models make assumptions 
         about the dividend growth. The basic Gordon model (Gordon, 1962) is based on a constant dividend growth rate, while multistage models are advanced by 
         Brooks and Helms (1990) and Barsky and De Long (1993) to better describe the dividend growth series. 
         """)

st.write(r"""We will focus on how the various models make assumptions about the dividend process, with a particular attention to the Markov chain based models.""")