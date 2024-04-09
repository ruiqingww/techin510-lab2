import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Boston Housing",
    page_icon="🏠",
    layout="centered", # centered, wide 
    initial_sidebar_state="auto", 
    menu_items=None
)

st.title("🏠 Boston Housing")

st.markdown("""
## Overview
- This dataset contains information about various houses in Boston through different parameters such as average number of rooms, property tax rate, pupil-teacher ratio by town, etc.

## Features
- **CRIM**: Per capita crime rate.
- **ZN**: Proportion of residential land zoned for lots over 25,000 sq.ft.
- **INDUS**: Proportion of non-retail business acres per town.
- **CHAS**: Charles River dummy variable (1 if tract bounds river; 0 otherwise).
- **NOX**: Nitric oxides concentration (parts per 10 million).
- **RM**: Average number of rooms per dwelling.
- **AGE**: Proportion of owner-occupied units built prior to 1940.
- **DIS**: Weighted distances to five Boston employment centres.
- **RAD**: Index of accessibility to radial highways.
- **TAX**: Full-value property-tax rate per $10,000.
- **PTRATIO**: Pupil-teacher ratio by town.
- **B**: 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town.
- **LSTAT**: Percentage of lower status of the population.
- **MEDV**: Median value of owner-occupied homes in $1000s.

""")

st.divider()

df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv")

with st.sidebar:
    # Input filter options
    medv_slider = st.slider(
        "Median Value of Homes (k)",
        min(df["medv"]),
        max(df["medv"]),
    )
    rm_slider = st.slider(
        "Rooms",
        min(df["rm"]),
        max(df["rm"]),
    )
    dis_slider = st.slider(
        "Weighted Distance to center",
        min(df["dis"]),
        max(df["dis"]),
    )
    rad_slider = st.slider(
        "Accessibility to Radial Highways",
        min(df["rad"]),
        max(df["rad"]),
    )
    nox_slider = st.slider(
        "Nitric Oxides Concentration",
        min(df["nox"]),
        max(df["nox"]),
    )
    chas_filter = st.selectbox(
        "By Charles River or Not",
        df["chas"].unique(),
        index=None
    )
    zn_filter = st.multiselect("Land Zone (multi-choice)", df["zn"].unique())


# Filter data
if zn_filter:
    df = df[df["zn"].isin(zn_filter)]
if chas_filter:
    df = df[df["chas"] == chas_filter]
df = df[df["rm"] > rm_slider]
df = df[df["dis"] > dis_slider]
df = df[df["rad"] > rad_slider]
df = df[df["medv"] > medv_slider]
df = df[df["nox"] > nox_slider]


with st.expander("RAW Data"):
    st.write(df)

fig = px.histogram(
    df, 
    x="crim"
)
st.plotly_chart(fig)

fig2 = px.scatter(
    df, 
    x="medv", 
    y="crim"
)
st.plotly_chart(fig2)

fig3 = px.scatter(
    df, 
    x="medv", 
    y="nox"
)
st.plotly_chart(fig3)