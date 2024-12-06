# 터미널에서 실행: streamlit run app.py
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key)

response = client.chat.completions.create(
 model="gpt-4o-mini",
 messages=[
 {"role": "system", "content": "You are a helpful assistant."},
 {"role": "user", "content": "Who won the world series in 2020?"},
 {"role": "user", "content": "Where was it played?"}
 ] 
)
print(response.choices[0].message.content)
