import streamlit as st
from data import STATUTES  # 핵심! data.py 파일에서 전체 정관 데이터를 불러옵니다.

# 1. 앱 설정
st.set_page_config(page_title="한강맨션 정관 검색", page_icon="📜", layout="wide")

# 2. 사이드바 (목차 기능)
st.sidebar.title("📖 목차")

# 데이터(STATUTES)에서 '장' 목록만 뽑아서 중복 제거 후 정렬
chapters_set = set()
for d in STATUTES:
    chapters_set.add(d["chapter"])
all_chapters = ["전체보기"] + sorted(list(chapters_set))

selected_chapter = st.sidebar.radio("장 선택", all_chapters)

# 3. 메인 화면 - 검색창
st.title("🏙️ 한강맨션 정관 검색 서비스")
search_term = st.text_input("검색어를 입력하세요 (예: 조합원, 총회, 분양)", "")

# 4. 필터링 로직
display_data = STATUTES

# 장별 필터링
if selected_chapter != "전체보기":
    display_data = [d for d in display_data if d["chapter"] == selected_chapter]

# 검색어 필터링
if search_term:
    display_data = [d for d in display_data if search_term in d["content"] or search_term in d["title"]]

# 5. 결과 출력
st.write(f"---")
st.subheader(f"🔍 결과: {len(display_data)}건")

if not display_data:
    st.info("검색 결과가 없습니다. 다른 키워드를 입력해 보세요.")
else:
    for item in display_data:
        with st.expander(f"**{item['article']} {item['title']}** ({item['chapter']})"):
            st.markdown(f"**[내용]**")
            st.write(item["content"])
