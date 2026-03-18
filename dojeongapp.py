import streamlit as st
from dojeongdata import LAW_DATA

# 앱 설정
st.set_page_config(page_title="도정법(도시정비법) 검색기", page_icon="⚖️", layout="wide")

# 사이드바 목차
st.sidebar.title("📑 법률 목차")
chapters = sorted(list(set(d["chapter"] for d in LAW_DATA)))
selected_chapter = st.sidebar.selectbox("장(Chapter) 선택", ["전체보기"] + chapters)

# 메인 화면
st.title("⚖️ 도시 및 주거환경정비법 검색")
st.info("대한민국 법제처의 최신 도정법 데이터를 바탕으로 제공됩니다.")

# 검색창
search_query = st.text_input("🔍 찾으시는 법률 키워드를 입력하세요", placeholder="예: 재건축, 조합원, 현금청산, 대의원회")

# 필터링 로직
display_data = LAW_DATA
if selected_chapter != "전체보기":
    display_data = [d for d in display_data if d["chapter"] == selected_chapter]

if search_query:
    display_data = [d for d in display_data if search_query in d["content"] or search_query in d["title"]]

# 결과 출력
st.subheader(f"📂 검색 결과: {len(display_data)}건")

for item in display_data:
    with st.expander(f"**{item['article']} {item['title']}**"):
        st.markdown(f"**[{item['chapter']}]**")
        st.write(item["content"])

st.markdown("---")
st.caption("본 앱은 June님이 한강맨션 재건축 이사로서 신속한 법률 확인을 위해 제작되었습니다.")
