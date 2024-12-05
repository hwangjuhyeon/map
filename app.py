import streamlit as st

st.title("동선 프로그램")

# HTML과 JavaScript를 삽입하여 Kakao 지도 표시
KAKAO_API_KEY = "dd5a7e1db353ceee0ef645b2cb146dac"

st.components.v1.html(render_kakao_map(), height=500)
