import streamlit as st


st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.write("# Welcome to SUDOKN! 👋")
st.sidebar.header("Home")
st.markdown(
    """
    SUDOKN is an open-source app framework built specifically for
    Manufacturing service capability discovery.
    **👈 Select a demo from the sidebar** to see some examples
    of what SUDOKN can do!
    ### Want to learn more?
    - Check out [ASU SUDOKN Project](https://projects.engineering.asu.edu/sudokn/)
    - Ask a question to Dr Farhad Ameri (farhad.ameri@asu.edu)
    ### Read about the NSF Sponsored Proto-OKN projects
    - Read about the multiple Open Knowledge Graphs [Proto-OKN](https://www.proto-okn.net/)
    - Explore other OKN projects [Proto-OKN projects](https://www.proto-okn.net/projects/)
"""
)