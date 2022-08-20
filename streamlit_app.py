from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

img = Image.open("wynum_02@2x.png")
st.set_page_config(page_title="Wynum App", page_icon=img)

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
    """

st.markdown(hide_menu_style, unsafe_allow_html=True)

"""
# Welcome to Wynum!

"""

import plotly.graph_objects as go

def create_trace(zoo_name,giraffes,orangutans,monkeys):
    trace = go.Bar(
    y=['giraffes', 'orangutans', 'monkeys'],
    x=[giraffes, orangutans, monkeys],
    name=zoo_name,
    orientation='h',
    marker=dict(
        # color='rgba(246, 78, 139, 0.6)',
        line=dict(color='black', width=3)
        )
    )
    return trace

zoo = st.multiselect('Select Zoo Name', ['SF', 'MI', 'IL'])
g = st.number_input(f'Number of giraffes', 0, 100)
o = st.number_input(f'Number of orangutans', 0, 100)
m = st.number_input(f'Number of monkeys', 0, 100)

fig = go.Figure()

for z in zoo:
    fig.add_trace(create_trace(z,g,o,m))


fig.update_layout(barmode='stack')

st.plotly_chart(fig, use_container_width=True)

