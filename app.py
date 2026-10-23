
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="중2 파이썬 코딩 놀이터",
    page_icon="🐍",
    layout="wide"
)

st.title("🐍 중2 파이썬 코딩 놀이터")

st.caption("학습자료를 확인하고 직접 코드를 입력해 실행해 보세요.")

st.info(
    "학습 범위: 출력(print), 입력(input), 변수, "
    "선택구조(if~else), 반복(for)"
)

# 학습자료
st.subheader("📚 학습자료")
st.link_button(
    "노션 학습자료 열기",
    "https://held-bangle-320.notion.site/2-4-402db0c3a76f81dfb4d5fdbcfd4e1b2f",
    use_container_width=True
)

# Streamlit 열기
st.subheader("💻 Streamlit 열기")
st.link_button(
    "Streamlit Playground 열기",
    "https://streamlit.io/playground?example=blank",
    use_container_width=True
)

st.divider()

# 파이썬 실습
st.subheader("📝 파이썬 코딩 실습")
st.iframe(
    Path(__file__).with_name("playground.html"),
    height=790
)

st.caption(
    "학생이 작성한 코드는 서버에 자동 저장되지 않습니다. "
    "결과물은 별도로 제출하세요."
)
