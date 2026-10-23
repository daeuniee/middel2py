from pathlib import Path
import streamlit as st

st.set_page_config(page_title="중2 파이썬 코딩 놀이터", page_icon="🐍", layout="wide")
st.title("🐍 중2 파이썬 코딩 놀이터")
st.caption("코드를 입력하고 실행 결과를 확인해 보세요. 스마트폰 화면으로도 볼 수 있어요!")
st.info("학습 범위: 출력(print), 입력(input), 변수, 선택구조(if~else), 반복(for)")
# HTML/JS is authored only by the teacher and never assembled from student-supplied HTML.
st.iframe(Path(__file__).with_name("playground.html"), height=790)
st.caption("인터넷 연결이 필요합니다. 예제 코드는 각 학생의 브라우저에서 실행되며 서버에 저장되지 않습니다.")
