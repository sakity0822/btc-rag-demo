from typing import Dict

# ダミーのRAG処理（後でLangChain + ベクトル検索に置き換え）
def query_rag(query: str) -> Dict:
    return {
        "answer": "TAS-102が三次治療以降に検討されることがあります。",
        "sources": [
            {
                "title": "Phase II study of TAS-102 in advanced BTC",
                "url": "https://pubmed.ncbi.nlm.nih.gov/123456789/",
                "n": 40,
                "type": "Phase II"
            },
            {
                "title": "Real-world study of third-line BTC therapy",
                "url": "https://pubmed.ncbi.nlm.nih.gov/987654321/",
                "n": 92,
                "type": "Observational"
            }
        ]
    }
