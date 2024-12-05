import streamlit as st

st.title("동선 프로그램")

# HTML과 JavaScript를 삽입하여 Kakao 지도 표시
KAKAO_API_KEY = "dd5a7e1db353ceee0ef645b2cb146dac"

def render_kakao_map():
    kakao_map_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://dapi.kakao.com/v2/maps/sdk.js?appkey={KAKAO_API_KEY}"></script>
        <style>#map {{width: 100%; height: 500px;}}</style>
    </head>
    <body>
        <div id="map"></div>
        <script>
            var mapContainer = document.getElementById('map');
            var mapOption = {{
                center: new kakao.maps.LatLng(37.5665, 126.9780), 
                level: 3
            }};
            var map = new kakao.maps.Map(mapContainer, mapOption);
        </script>
    </body>
    </html>
    """
    return kakao_map_html

st.title("Kakao Map Integration")
st.components.v1.html(render_kakao_map(), height=500)
