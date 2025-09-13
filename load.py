
def fetch_files(path):
    from os import listdir
    files = []
    for i in listdir(path):
        if i != ".DS_Store":
            files.append(i)
    return files

def load_files(path,files):
    from langchain_community.document_loaders import PyPDFLoader

    loaded_files = []
    for file in files:
        full_file_path = path + "/" + file
        print(full_file_path)
        loader = PyPDFLoader(full_file_path)
        loaded_files = loader.load()
    return list(map(str,loaded_files))