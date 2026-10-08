from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

documents = [
    "犬が公園を走っています。",
    "子犬が外で遊んでいます。",
    "今日の株価が上昇しました。",
]

embeddings = model.encode(documents)

for text, vector in zip(documents, embeddings):
    print(f"文章: {text}")
    print(f"ベクトルの次元数: {len(vector)}")
    print(f"先頭５個:{vector[:5]}")
    print("-" * 30)
    