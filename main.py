def main():
    import load, split, embed
    import generation as gen
    print("Starting main")
    #Set folder path for documents to insert into vector database
    path = "/Users/savarbharadwaj/PycharmProjects/RAG/data"

    #Calling function to fetch files in folder
    files = load.fetch_files(path)
    print("files are :" , files)

    #Loading the files fetched into Python
    loaded_files = load.load_files(path,files)

    #Creating Chunks of files
    chunks = split.split_loaded_docs(loaded_files)

    #Loading into the database
    embed.embed_and_store(chunks)

    #Calling LLM
    gen.generation()




if __name__ == "__main__":
    print("Calling main")
    main()
