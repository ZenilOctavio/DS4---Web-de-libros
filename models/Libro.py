class Libro:

    id:str
    file_name:str
    url:str
    book_name:str
    author_name:str
    volume:str
    category:str

    def __init__(self, id:str , file_name:str, url:str, book_name:str, author_name:str, volume:str, category:str):
            self.id = id
            self.file_name = file_name
            self.url = url
            self.book_name = book_name
            self.author_name = author_name
            self.volume = volume
            self.category = category
    

