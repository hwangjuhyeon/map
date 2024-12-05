import streamlit as st

st.title("동선 프로그램")

# Kakao 지도 API 키
KAKAO_API_KEY = "dd5a7e1db353ceee0ef645b2cb146dac"

import requests

searching = '합정 스타벅스'
url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)
headers = {
    "Authorization": "KakaoAK dd5a7e1db353ceee0ef645b2cb146dac"
}
places = requests.get(url, headers = headers).json()['documents']
places
