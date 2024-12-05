import streamlit as st
from streamlit.components.v1 import html

st.title("동선 프로그램")

# Kakao 지도 렌더링 함수
def kakao_map(api_key):
    # HTML 코드와 JavaScript 코드
    map_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <script type="text/javascript" src="https://dapi.kakao.com/v2/maps/sdk.js?appkey={api_key}"></script>
        <style>
            #map {{
                width: 100%;
                height: 400px;
            }}
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script>
            var container = document.getElementById('map');
            var options = {{
                center: new kakao.maps.LatLng(37.5665, 126.9780), // 서울 시청 좌표
                level: 3 // 확대 레벨
            }};
            var map = new kakao.maps.Map(container, options);
        </script>
    </body>
    </html>
    """
    # Streamlit에서 HTML을 삽입
    html(map_html, height=450, width=700)

def main():
    st.title("Kakao 지도 API - Streamlit 연동")
    
    # 사용자로부터 API 키 입력받기
    kakao_api_key = st.text_input("Kakao API 키를 입력하세요")
    
    if kakao_api_key:
        st.success("API 키가 입력되었습니다. 지도를 생성합니다.")
        kakao_map(kakao_api_key)  # 입력된 API 키로 지도 생성
    else:
        st.warning("API 키를 입력해야 지도가 표시됩니다.")

if __name__ == "__main__":
    main()
