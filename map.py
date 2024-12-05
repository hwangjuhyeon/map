import streamlit as st
import pydeck as pdk

# Define a layer to display on the map
layer = pdk.Layer(
    'ScatterplotLayer',
    data=df, # your dataframe
    get_position='[lon, lat]',
    get_color='[200, 30, 0, 160]',
    get_radius=200,
)

# Render a map with the defined layer
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[layer],
    api_keys={'mapbox': 'your_mapbox_api_key', 'google_maps': 'your_google_maps_api_key'},
))
