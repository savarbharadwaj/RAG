def generation():
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_community.vectorstores import Chroma
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    import torch as t

    embedding_model = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

    db = Chroma(persist_directory='./db', embedding_function=embedding_model)

    model_name = 'google/flan-t5-base'

    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    tokenizer = AutoTokenizer.from_pretrained('google/flan-t5-base')

    while True:

        query = input("Ask: ")

        docs = db.similarity_search(query,k= 3)

        context = "\n\n".join(d.page_content for d in docs)

        #instruction =

        prompt = f"You are an expert assistant. Use ONLY the provided context to answer the use's question. If the answer is not contained in the context, say - I don't know. Do not hallucinate. Use context to answer the question. \n\n context: {context} \n\n query: {query} \n\n Answer:"

        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        out = model.generate(**inputs, max_new_tokens=200)
        #out = model.generate(tokenizer(prompt, return_tensors="pt").to(model.device), max_new_tokens=100)


        answer = tokenizer.decode(out[0], skip_special_tokens=True)
        print(answer)