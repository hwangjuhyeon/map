import streamlit as st

st.title("동선 프로그램")

# Kakao 지도 API 키
KAKAO_API_KEY = "dd5a7e1db353ceee0ef645b2cb146dac"

def render_kakao_map():
    kakao_map_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <script src="https://dapi.kakao.com/v2/maps/sdk.js?appkey={KAKAO_API_KEY}"></script>
        <style>
            #map {{
                width: 100%;
                height: 500px;
            }}
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script>
            var mapContainer = document.getElementById('map');
            var mapOption = {{
                center: new kakao.maps.LatLng(37.5665, 126.9780), // 중심좌표
                level: 3 // 확대 레벨
            }};
            var map = new kakao.maps.Map(mapContainer, mapOption); // 지도 생성
        </script>
    </body>
    </html>
    """
    return kakao_map_html

# Streamlit 앱
st.title("Kakao Map Integration")
st.components.v1.html(render_kakao_map(), height=500)
