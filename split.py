def split_loaded_docs(loaded_docs):
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    for i in loaded_docs:
        split_config = RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=50)
        splitted_docs = split_config.split_text(i)
        return splitted_docs