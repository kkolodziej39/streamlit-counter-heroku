# Code from https://docs.streamlit.io/library/advanced-features/session-state

import streamlit as st

st.title('Counter')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write('Count = ', st.session_state.count)


