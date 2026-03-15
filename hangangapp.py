import streamlit as st
from hangangdata import STATUTES

# 1. 앱 설정
st.set_page_config(page_title="한강맨션 정관 검색", page_icon="📜", layout="wide")

# 2. 사이드바
st.sidebar.title("📖 목차")
chapters_set = set(d["chapter"] for d in STATUTES)
all_chapters = ["전체보기"] + sorted(list(chapters_set))
selected_chapter = st.sidebar.radio("장 선택", all_chapters)

# 3. 메인 화면
st.title("🏙️ 한강맨션 정관 검색 서비스")

with st.expander("📜 정관 제·개정 이력 확인"):
    st.markdown("""
    * **제 정 :** 2017. 04. 22.
    * **1차 개정 :** 2017. 09. 23.
    * **2차 개정 :** 2019. 03. 31.
    * **3차 개정 :** 2019. 12. 14.
    * **4차 개정 :** 2020. 06. 27.
    * **5차 개정 :** 2020. 11. 28.
    * **6차 개정 :** 2022. 01. 22.
    * **7차 개정 :** 2022. 09. 30.
    * **8차 개정 :** 2023. 03. 31.
    * **9차 개정 :** 2023. 09. 14.
    * **10차 개정 :** 2025. 12. 00. (현재 최신 전문)
    """)

search_term = st.text_input("🔍 검색어를 입력하세요", placeholder="예: 조합원, 총회, 분양")

display_data = STATUTES
if selected_chapter != "전체보기":
    display_data = [d for d in display_data if d["chapter"] == selected_chapter]
if search_term:
    display_data = [d for d in display_data if search_term in d["content"] or search_term in d["title"]]

st.write("---")
st.subheader(f"🔍 결과: {len(display_data)}건")

if not display_data:
    st.info("검색 결과가 없습니다.")
else:
    for item in display_data:
        with st.expander(f"**{item['article']} {item['title']}** ({item['chapter']})"):
            st.markdown(f"**[내용]**")
            st.write(item["content"])

st.markdown("---")
st.caption("본 서비스는 한강맨션아파트 주택재건축정비사업조합 정관 원본을 바탕으로 합니다.")
