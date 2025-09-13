def embed_and_store(chunks):
    # from sentence_transformers import SentenceTransformer
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_community.vectorstores import Chroma

    embedding_model = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

    db = Chroma.from_texts(chunks, embedding = embedding_model, persist_directory='./db')
    db.persist()
    print("embedding done")

    #query = "What is the university name?"
    #results = db.similarity_search(query, k=4)
    #for r in results:
    #    print(r.page_content[:300])