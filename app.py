import streamlit as st
import googlemaps
from itertools import permutations
import folium
from streamlit_folium import st_folium

# Google Maps API 키 설정
API_KEY = "AIzaSyBwk_avwCbUMdtx_XzII92V_erg1YzJD6Q"
gmaps = googlemaps.Client(key=API_KEY)

def calculate_route(locations):
    """
    주어진 장소들에 대해 최적의 동선을 계산합니다.
    """
    # 모든 장소의 조합에 대해 경로 계산
    min_distance = float('inf')
    best_route = None
    best_route_coordinates = None

    for perm in permutations(locations):
        total_distance = 0
        route_coordinates = []
        for i in range(len(perm) - 1):
            origin = perm[i]
            destination = perm[i + 1]
            
            # Google Maps Distance Matrix API 호출
            directions_result = gmaps.directions(origin, destination)
            if directions_result:
                # 경로의 첫 번째 좌표 추가
                if i == 0:
                    route_coordinates.append(directions_result[0]['legs'][0]['start_location'])
                route_coordinates.append(directions_result[0]['legs'][0]['end_location'])

                # 경로 거리 추가
                total_distance += directions_result[0]['legs'][0]['distance']['value']

        # 최적 경로 업데이트
        if total_distance < min_distance:
            min_distance = total_distance
            best_route = perm
            best_route_coordinates = route_coordinates

    return best_route, min_distance, best_route_coordinates

# Streamlit UI
st.title("부산 여행 동선 최적화")
st.write("방문하고 싶은 부산의 장소를 입력하세요. 예: 광안리 해수욕장, 부경대학교, 해운대")

# 사용자 입력 받기
locations_input = st.text_area("장소들 입력 (콤마로 구분)", "광안리 해수욕장, 부경대학교, 해운대")
locations = [loc.strip() for loc in locations_input.split(",") if loc.strip()]

if st.button("최적 동선 계산"):
    if len(locations) < 2:
        st.error("최소 2개 이상의 장소를 입력해주세요.")
    else:
        with st.spinner("동선을 계산 중입니다..."):
            best_route, min_distance, route_coordinates = calculate_route(locations)

        if best_route:
            st.success(f"최적 경로: {' → '.join(best_route)}")
            st.write(f"총 거리: {min_distance / 1000:.2f} km")

            # Folium 지도 생성
            map_center = [35.1796, 129.0756]  # 부산 중심 좌표
            m = folium.Map(location=map_center, zoom_start=12)

            # 경로 표시
            for i, coord in enumerate(route_coordinates):
                folium.Marker([coord['lat'], coord['lng']], popup=best_route[i]).add_to(m)
                if i > 0:
                    folium.PolyLine([[route_coordinates[i-1]['lat'], route_coordinates[i-1]['lng']],
                                     [coord['lat'], coord['lng']]], color="blue", weight=2).add_to(m)

            # 지도 출력
            st_folium(m, width=700, height=500)
        else:
            st.error("경로를 계산할 수 없습니다. 입력된 장소를 확인해주세요.")
