
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="중2 파이썬 코딩 놀이터",
    page_icon="🐍",
    layout="wide"
)

# 오른쪽 상단 제작자 표시
st.markdown(
    """
    <div style="text-align: right;
                color: gray;
                font-size: 13px;">
        제작: 최다은T
    </div>
    """,
    unsafe_allow_html=True
)

st.title("🐍 중2 파이썬 코딩 놀이터")

st.caption(
    "학습자료를 확인하고 직접 코드를 입력해 실행해 보세요."
)

st.info(
    "학습 범위: 출력(print), 입력(input), 변수, "
    "선택구조(if~else), 반복(for)"
)

# 학습자료 및 Streamlit 2단 배치
left, right = st.columns(2, gap="medium")

with left:
    st.subheader("📚 학습자료")
    st.link_button(
        "학습자료 열기",
        "https://held-bangle-320.notion.site/2-4-402db0c3a76f81dfb4d5fdbcfd4e1b2f",
        use_container_width=True
    )

with right:
    st.subheader("💻 Streamlit 열기")
    st.link_button(
        "Streamlit Playground 열기",
        "https://streamlit.io/playground?example=blank",
        use_container_width=True
    )

st.divider()

# 파이썬 코딩 실습
st.subheader("💻 파이썬 코딩 실습")

st.iframe(
    Path(__file__).with_name("playground.html"),
    height=790
)

st.caption(
    "학생이 작성한 코드는 서버에 자동 저장되지 않습니다. "
)

# 오른쪽 하단 제작자 표시
st.divider()

st.markdown(
    """
    <div style="text-align: right;
                color: gray;
                font-size: 12px;
                padding: 8px 0 18px;">
        © 2026 Python Coding Playground · Made by 최다은T
    </div>
    """,
    unsafe_allow_html=True
)
