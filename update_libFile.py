import pandas as pd

def UpdateLibFile(newBookData):
    full_library = "./fullLibrary.xlsx"
    add = pd.DataFrame(newBookData)
    existing = pd.read_excel(full_library)
    combined = existing._append(add,ignore_index=True)
    if len(combined.drop_duplicates().index) != len(combined.index):
        print(newBookData["Title"][0], " was a duplicate") 
    combined.drop_duplicates().to_excel(full_library, index=False)
    return()

if __name__ == "__main__":
    #Testing
    bookData = {
                'Title':["titre"], 
                'Author':["ecrivain"], 
                'Publishing Date':["date de publication"],
                'Genre':["genre"],
                'Page Count':["numero de page"]
                }
    UpdateLibFile(bookData)