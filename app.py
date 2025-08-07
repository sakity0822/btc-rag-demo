import streamlit as st
from rag_chain import query_rag

st.title("胆道がん 三次治療以降 RAGデモ")

query = st.text_input("治療について質問してください:")

if query:
    with st.spinner("検索中..."):
        response = query_rag(query)
        st.markdown("### 回答")
        st.write(response["answer"])
        st.markdown("### 出典と信頼性")
        for doc in response["sources"]:
            st.markdown(f"- [{doc['title']}]({doc['url']}) | N={doc['n']} | 種別={doc['type']}")
