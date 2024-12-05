import streamlit as st
import googlemaps
from itertools import permutations
import numpy as np

# Google Maps API 키
API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
gmaps = googlemaps.Client(key=API_KEY)

# Streamlit UI
st.title("부산 여행 동선 최적화 프로그램")
st.write("부산에 방문할 장소를 입력하고 최적의 동선을 확인하세요!")

# 입력받은 관광지 목록
places_input = st.text_area("방문할 장소를 입력하세요 (쉼표로 구분):", "해운대, 광안리, 자갈치 시장, 태종대")
places = [place.strip() for place in places_input.split(",") if place.strip()]

if len(places) < 2:
    st.warning("최소 2개 이상의 장소를 입력해주세요.")
else:
    st.success(f"입력된 장소: {places}")

# 장소 이름 -> GPS 좌표 변환
def get_coordinates(place):
    try:
        geocode_result = gmaps.geocode(place)
        location = geocode_result[0]["geometry"]["location"]
        return location["lat"], location["lng"]
    except Exception as e:
        st.error(f"Error fetching coordinates for {place}: {e}")
        return None, None

# 입력된 장소들의 좌표 가져오기
coordinates = []
for place in places:
    lat, lng = get_coordinates(place)
    if lat is not None and lng is not None:
        coordinates.append((place, lat, lng))

if not coordinates:
    st.error("좌표 정보를 가져오지 못했습니다. 장소를 다시 확인해주세요.")
else:
    st.write("장소 좌표:")
    for place, lat, lng in coordinates:
        st.write(f"{place}: ({lat}, {lng})")

# 장소 간 거리 계산
def calculate_distance_matrix(coords):
    origins = [(lat, lng) for _, lat, lng in coords]
    destinations = origins
    distance_matrix = gmaps.distance_matrix(origins, destinations, mode="driving")
    distances = []
    for row in distance_matrix["rows"]:
        distances.append([elem["distance"]["value"] for elem in row["elements"]])
    return np.array(distances)

# 거리 행렬 계산
distance_matrix = calculate_distance_matrix(coordinates)
st.write("거리 행렬 (단위: 미터):")
st.write(distance_matrix)

# 최적 경로 계산
def find_optimal_route(coords, distance_matrix):
    n = len(coords)
    min_distance = float("inf")
    optimal_route = []
    for perm in permutations(range(n)):
        distance = sum(distance_matrix[perm[i], perm[i + 1]] for i in range(n - 1))
        if distance < min_distance:
            min_distance = distance
            optimal_route = perm
    return optimal_route, min_distance

route, min_distance = find_optimal_route(coordinates, distance_matrix)
optimal_places = [coordinates[i][0] for i in route]

st.write("최적 경로:")
st.write(" ➡️ ".join(optimal_places))
st.write(f"총 거리: {min_distance / 1000:.2f} km")

# 경로 시각화
def get_directions(route_coords):
    waypoints = [f"{lat},{lng}" for _, lat, lng in route_coords[1:-1]]
    directions_result = gmaps.directions(
        origin=f"{route_coords[0][1]},{route_coords[0][2]}",
        destination=f"{route_coords[-1][1]},{route_coords[-1][2]}",
        waypoints=waypoints,
        mode="driving",
    )
    return directions_result

directions = get_directions([coordinates[i] for i in route])
st.write("경로 세부 정보:")
st.json(directions[0])
