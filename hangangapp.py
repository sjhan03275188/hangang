import streamlit as st
from hangangdata import STATUTES  # 데이터 파일 연결

# 1. 앱 페이지 설정 (브라우저 탭 이름 및 아이콘)
st.set_page_config(page_title="한강맨션 정관 검색", page_icon="📜", layout="wide")

# 2. 사이드바 - 목차 기능
st.sidebar.title("📖 목차")

# 데이터에서 '장' 목록만 추출하여 중복 제거 후 정렬
chapters_set = set()
for d in STATUTES:
    chapters_set.add(d["chapter"])
all_chapters = ["전체보기"] + sorted(list(chapters_set))

selected_chapter = st.sidebar.radio("장 선택", all_chapters)

# 3. 메인 화면 상단 - 제목 및 개정 이력
st.title("🏙️ 한강맨션 정관 검색 서비스")

# --- 정관 제·개정 이력 (접이식 메뉴로 가독성 확보) ---
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

# 4. 검색창
search_term = st.text_input("🔍 검색어를 입력하세요", placeholder="예: 조합원, 총회, 분양, 이사", help="조항 제목이나 내용에 포함된 단어를 입력하세요.")

# 5. 데이터 필터링 로직
display_data = STATUTES

# '장' 필터링
if selected_chapter != "전체보기":
    display_data = [d for d in display_data if d["chapter"] == selected_chapter]

# '검색어' 필터링
if search_term:
    display_data = [d for d in display_data if search_term in d["content"] or search_term in d["title"]]

# 6. 결과 출력
st.write("---")
st.subheader(f"🔍 검색 결과: {len(display_data)}건")

if not display_data:
    st.info("검색 결과가 없습니다. 검색어를 확인하거나 다른 단어로 시도해 보세요.")
else:
    for item in display_data:
        # 아코디언 형태로 모바일에서 깔끔하게 노출
        with st.expander(f"**{item['article']} {item['title']}** ({item['chapter']})"):
            st.markdown(f"**[내용]**")
            # 텍스트 내 줄바꿈(\n)을 반영하여 출력
            st.write(item["content"])

# 하단 정보
st.markdown("---")
st.caption("본 서비스는 한강맨션아파트 주택재건축정비사업조합의 정관 원본 데이터를 바탕으로 제공됩니다.")
