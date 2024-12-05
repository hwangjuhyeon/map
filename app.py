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
    st.title("Kakao 지도 API - 사용자 입력 버전")
    
    # 사용자로부터 API 키 입력받기
    kakao_api_key = st.text_input("Kakao API 키를 입력하세요")
    
    if kakao_api_key:
        st.success("API 키가 입력되었습니다. 지도를 생성합니다.")
        kakao_map(kakao_api_key)
    else:
        st.warning("API 키를 입력해야 지도가 표시됩니다.")

if __name__ == "__main__":
    main()
