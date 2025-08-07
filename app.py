import streamlit as st
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

# --- APIキーの設定（環境変数で管理推奨） ---
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    st.error("OpenAI APIキーが設定されていません。")
    st.stop()

# --- UI構成 ---
st.title("胆道がん 三次治療以降 RAG支援チャット")
st.write("PubMedの最新論文からAIが治療の選択肢を提示し、信頼性レベルも表示します。")

# --- ステージ選択（選択式 UI） ---
stage = st.selectbox("治療ステージを選択してください：", ["3次治療", "4次治療", "その他レアケース"])

# --- ユーザー入力（チャット形式） ---
user_input = st.text_input("気になる症状や条件を入力してください（例：肝転移がある場合）")

# --- ベクトルDBの読み込み（事前構築） ---
persist_directory = "chroma_db"  # あなたのベクトルDBのディレクトリに合わせて変更
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

# --- RAGによる応答生成 ---
llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectordb.as_retriever()
)

# --- 回答表示 ---
if user_input:
    with st.spinner("PubMed論文から最適な情報を検索中..."):
        response = qa_chain.run(user_input)

    st.subheader("💬 回答（AI）")
    st.write(response)

    # （オプション）信頼性スコア例：
    st.subheader("📊 信頼性レベル（例）")
    st.markdown("- 引用論文数：8件\n- 対象症例：合計N=752\n- 試験デザイン：3件 RCT, 5件 observational")

    # （オプション）出典例：
    st.subheader("📚 主な参考文献（例）")
    st.markdown("- Tanaka et al. 2024, J Clin Oncol\n- Suzuki et al. 2023, Lancet Oncol")


