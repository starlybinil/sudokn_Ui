import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from urllib.error import URLError
import plotly.express as px
from streamlit_extras.grid import grid
from controls import SERVICE_TYPES as services

st.set_page_config(page_title="SUDOKN Query", page_icon="📊", layout="wide")

st.markdown("# SUDOKN Demo")
st.sidebar.header("SUDOKN Query")

def get_SUDOKN_data():
    AWS_BUCKET_URL = "./data/NAICS 332.csv"
    df = pd.read_csv(AWS_BUCKET_URL)
    return df.set_index("GlobalID")


col1, col2 = st.columns([1,2])

try:
    df = get_SUDOKN_data()
    col1.markdown("##### Region Selection")
    sxt = col1.text_area('Search within results', height=50, placeholder="Type keywords of interest")

    country = col1.multiselect("Choose Country", ["United States of America", "Canada", "Mexico"], ["United States of America"])

    states = col1.multiselect(
        "Choose State", list(df.loc[:,'STATE'].unique()), ["MN"]
    )

    col1.multiselect('Service Capabilities?', services)
    col1.slider ("Year Founded", 1850, 2024, 2010, step=5)
    
    st.divider()
    with st.expander("Additional Selection Filters"):
        my_grid = grid(1,5,1,5,1,8, vertical_align="bottom")
        my_grid.caption("Business Type")
        smb = my_grid.checkbox("Small Business/Disadvantaged")
        wom = my_grid.checkbox("Woman Owned")
        mino = my_grid.checkbox("Minority Owned")
        hub = my_grid.checkbox("HubZone")
        vet = my_grid.checkbox("Veteran Owned")

        my_grid.caption("Company Type")
        my_grid.checkbox("Product Manufacturer")
        my_grid.checkbox("Custom Job Manufacturer")
        my_grid.checkbox("Product Distributor")
        my_grid.checkbox("Services Company")
        my_grid.checkbox("Manufacturing Systems Integrator")

        my_grid.caption("Industry Sector")
        my_grid.checkbox("Aerospace/Defense")
        my_grid.checkbox("Medical")
        my_grid.checkbox("Automotive")
        my_grid.checkbox("Microelectronics")
        my_grid.checkbox("Agricultural/Food")
        my_grid.checkbox("Consumer")
        my_grid.checkbox("Heavy Manufacturing")
        my_grid.checkbox("Construction")

    if not states:
        st.error("Please select at least one state.")
    else:
        data = df.loc[(df["COUNTRY"]=="United States of America") 
                      & (df["STATE"].isin(states))

                     ]
        st.write("### Available Manufacturers", data.sort_index())

except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )

def display_map(location_data:pd.DataFrame):

    fig = px.scatter_mapbox(location_data, lat="LATITUDE", lon="LONGITUDE", zoom=3, 
                            hover_name='NAME', hover_data=['PRODUCT', 'WEB'])

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

col2.subheader('Company Location Map')
px_map = display_map(data)
col2.plotly_chart(px_map, use_container_width=True)

