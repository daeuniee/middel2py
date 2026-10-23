from pathlib import Path
import streamlit as st

st.set_page_config(page_title="중2 파이썬 코딩 놀이터", page_icon="🐍", layout="wide")
st.title("🐍 중2 파이썬 코딩 놀이터")
st.caption("차시별 학습 내용을 확인하고, 직접 코드를 입력해 실행해 보세요.")
st.info("학습 범위: 출력(print), 입력(input), 변수, 선택구조(if~else), 반복(for)")

LESSONS = [
    ("1차시 · 개발 환경", "https://app.notion.com/p/402db0c3a76f81be9303f8f56bdc449f"),
    ("2차시 · 선택 구조", "https://app.notion.com/p/402db0c3a76f813e9d3ffcd59893f722"),
    ("3차시 · 반복 구조", "https://app.notion.com/p/402db0c3a76f811fa28bd8b6cc724b4f"),
    ("4차시 · 미니 앱", "https://app.notion.com/p/402db0c3a76f81549762cf251adfb4ea"),
]

st.subheader("📚 차시별 학습 안내")
cols = st.columns(4)
for col, (label, url) in zip(cols, LESSONS):
    with col:
        st.link_button(label, url, use_container_width=True)

a, b = st.columns(2)
with a:
    st.link_button("📖 4차시 전체 안내서(노션)", "https://held-bangle-320.notion.site/2-4-402db0c3a76f81dfb4d5fdbcfd4e1b2f", use_container_width=True)
with b:
    st.link_button("🧪 Streamlit 공식 Playground 열기", "https://streamlit.io/playground?example=blank", use_container_width=True)

st.divider()
st.subheader("💻 파이썬 코딩 실습")
# 학생 코드는 Streamlit 서버가 아닌 브라우저 실행기에서 처리합니다.
st.iframe(Path(__file__).with_name("playground.html"), height=790)
st.caption("학생이 작성한 코드는 서버에 자동 저장되지 않습니다. 결과물은 별도 제출 방식으로 수집하세요.")
