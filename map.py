import streamlit as st
import openai
from itertools import permutations

# Streamlit 앱 제목
st.title("부산 여행 동선 최적화")

# OpenAI API 키 입력받기
api_key = st.text_input("OpenAI API 키를 입력하세요:", type="password")
if api_key:
    openai.api_key = api_key
    st.success("API 키가 설정되었습니다.")

# 관광지 입력받기
st.header("부산 관광지 목록")
spots = st.text_area("방문할 관광지를 한 줄에 하나씩 입력하세요 (2개 이상):")
spots_list = [spot.strip() for spot in spots.split("\n") if spot.strip()]

if len(spots_list) < 2:
    st.warning("최소 2개의 관광지를 입력하세요.")
else:
    if st.button("동선 최적화 요청"):
        # OpenAI API 호출을 통한 동선 최적화 요청
        with st.spinner("동선을 최적화하는 중..."):
            try:
                prompt = (
                    f"부산에 있는 다음 관광지를 방문할 최적의 동선을 짜주세요: {', '.join(spots_list)}. "
                    "동선은 방문 순서와 간단한 설명으로 제공해주세요."
                )

                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "너는 여행 계획 전문가야."},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.7,
                )

                # OpenAI의 응답을 출력
                plan = response.choices[0].message['content']
                st.success("동선 최적화 완료!")
                st.markdown(f"**최적화된 동선:**\n\n{plan}")
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")

