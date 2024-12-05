import streamlit as st

st.title("동선 프로그램")

# Kakao 지도 HTML 삽입
def kakao_map(api_key):
    st.write("""
    <script type="text/javascript"
            src="https://dapi.kakao.com/v2/maps/sdk.js?appkey={}"></script>
    <div id="map" style="width:100%;height:400px;"></div>
    <script>
        var container = document.getElementById('map');
        var options = {{
            center: new kakao.maps.LatLng(37.5665, 126.9780), // 서울 시청 좌표
            level: 3 // 확대 레벨
        }};
        var map = new kakao.maps.Map(container, options);
    </script>
    """.format(api_key), unsafe_allow_html=True)

def main():
    st.title("Kakao 지도 API - Streamlit 앱")
    kakao_api_key = st.secrets["KAKAO_API_KEY"]  # secrets.toml에서 API 키 가져오기
    if kakao_api_key:
        kakao_map(kakao_api_key)
    else:
        st.error("Kakao API 키가 필요합니다!")

if __name__ == "__main__":
    main()
