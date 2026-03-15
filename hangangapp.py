import streamlit as st

# 1. 앱 설정 (모바일 최적화 및 제목 설정)
st.set_page_config(page_title="한강맨션 정관 검색", page_icon="📜", layout="wide")

# 2. 정관 데이터 (이미지 내용을 바탕으로 예시 작성 - 실제 내용을 여기에 채워 넣으시면 됩니다)
# 이미지에서 추출한 텍스트를 이런 리스트 형식으로 정리해야 합니다.
statutes_data = [
    {"chapter": "제1장 총칙", "article": "제1조", "title": "명칭", "content": "이 조합은 한강맨션아파트 주택재건축정비사업조합(이하 \"조합\"이라 한다)이라 한다."},
    {"chapter": "제1장 총칙", "article": "제2조", "title": "목적", "content": "본 조합은 도시 및 주거환경정비법에 따라 서울특별시 용산구 이촌동 300-23번지 일대의 주택재건축정비사업을 시행함을 목적으로 한다."},
    {"chapter": "제1장 총칙", "article": "제3조", "title": "사무소", "content": "조합의 주된 사무소는 서울특별시 용산구 이촌로...에 둔다."},
    {"chapter": "제2장 조합원", "article": "제9조", "title": "조합원의 자격", "content": "조합원은 사업시행구역 안의 토지 또는 건축물의 소유자로 하되..."},
    # ... 이미지의 나머지 내용을 이 형식으로 추가 ...
]

# 3. 사이드바 (목차 기능)
st.sidebar.title("📖 목차")
all_chapters = ["전체보기"] + sorted(list(set([d["chapter"] for d in statutes_data])))
selected_chapter = st.sidebar.radio("장 선택", all_chapters)

# 4. 메인 화면 - 검색창
st.title("🏙️ 한강맨션 정관 검색 서비스")
search_term = st.text_input("검색어를 입력하세요 (예: 조합원, 이사, 의결권)", "")

# 5. 필터링 로직
display_data = statutes_data

# 장별 필터링
if selected_chapter != "전체보기":
    display_data = [d for d in display_data if d["chapter"] == selected_chapter]

# 검색어 필터링
if search_term:
    display_data = [d for d in display_data if search_term in d["content"] or search_term in d["title"]]

# 6. 결과 출력 (모바일에서 보기 좋게 Expander 활용)
st.write(f"---")
st.subheader(f"🔍 결과: {len(display_data)}건")

if not display_data:
    st.info("검색 결과가 없습니다. 다른 키워드를 입력해 보세요.")
else:
    for item in display_data:
        # 조항 제목을 클릭하면 내용이 펼쳐지도록 구성
        with st.expander(f"**{item['article']} {item['title']}** ({item['chapter']})"):
            st.markdown(f"**[내용]**")
            st.write(item["content"])