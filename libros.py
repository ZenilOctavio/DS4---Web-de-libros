from models.Libro import Libro

def read_file(file_path:str) -> list[str]:
    lines = ''
    with open(file_path, 'r',encoding='utf-8') as csv:
        lines = csv.readlines()
    
    return lines

def get_libros(lines:list[str]) -> list[Libro]:
    lista:list[str] = []
    for line in lines:
        fields = line.split(',')
        libro = Libro(fields[0],fields[1],fields[2],fields[3],fields[4],fields[5],fields[6])
        lista.append(libro)
    return lista

def get_lista_libros(file_path):
    return get_libros(read_file(file_path))

def check(lineas:list[str]):
    lista:list[int] = []
    for linea in lineas:
        lista.append(len(linea.split(',')))
    
    print(lista)

if __name__ == '__main__':
    lines = read_file('./booklist2000.csv')
    check(lines)

    # print(libros)