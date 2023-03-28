from flask import Flask,render_template,request,redirect,url_for
import libros



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/por_titulo')
def porTitulo():
    lista = libros.get_lista_libros('./booklist2000.csv')
    lista = sorted(lista,key=lambda x:x.book_name)
    return render_template('por_titulo.html',lista=lista)

if __name__ == '__main__':
    print('helomundo')
    app.run(debug=True)     