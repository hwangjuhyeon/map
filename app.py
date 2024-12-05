import streamlit as st
import googlemaps  # Google Maps API
import numpy as np
from itertools import permutations

# Google Maps API 키 설정
gmaps = googlemaps.Client(key='YOUR_GOOGLE_MAPS_API_KEY')

# 사용자로부터 관광지 입력 받기
st.title('Busan Travel Route Optimizer')
places = st.text_area("Enter places you want to visit (comma separated):")
places = places.split(',')

# 입력된 장소들의 위치 정보 가져오기
locations = []
for place in places:
    geocode_result = gmaps.geocode(place.strip())
    if geocode_result:
        lat_lng = geocode_result[0]['geometry']['location']
        locations.append((place.strip(), lat_lng['lat'], lat_lng['lng']))

# 최적 경로 계산 (간단한 brute-force 방식)
def calculate_optimal_route(locations):
    # 장소 간의 거리 계산 (단순히 구글 맵 API의 거리 행렬을 이용)
    distance_matrix = []
    for loc1 in locations:
        row = []
        for loc2 in locations:
            if loc1 == loc2:
                row.append(0)
            else:
                distance = gmaps.distance_matrix((loc1[1], loc1[2]), (loc2[1], loc2[2]))
                row.append(distance['rows'][0]['elements'][0]['distance']['value'])  # 거리 (미터 단위)
        distance_matrix.append(row)

    # 가능한 경로의 모든 경우에 대해 거리 합산
    min_distance = float('inf')
    optimal_route = None
    for perm in permutations(locations):
        total_distance = 0
        for i in range(len(perm) - 1):
            total_distance += distance_matrix[locations.index(perm[i])][locations.index(perm[i+1])]
        if total_distance < min_distance:
            min_distance = total_distance
            optimal_route = perm
    
    return optimal_route

# 최적 경로 출력
optimal_route = calculate_optimal_route(locations)

# 최적 경로 지도에 표시
st.write("Optimal Route:", [place[0] for place in optimal_route])

# 지도 표시
map_center = [optimal_route[0][1], optimal_route[0][2]]
st.map([{'lat': loc[1], 'lon': loc[2]} for loc in optimal_route], zoom=12)
