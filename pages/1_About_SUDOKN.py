import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="About SUDOKN", page_icon="📊", layout="wide")

col1, col2, col3 = st.columns([1,2,1])
col1.markdown("# SUDOKN Help")
st.sidebar.header("About SUDOKN")
