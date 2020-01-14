from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template import loader
from django.shortcuts import render, redirect
import requests
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup

#from .models import Product

 



class Producto(object):

    def __init__(self, titulo, precio, envio):
        self.titulo=titulo
        self.precio=precio
        self.envio=envio   


def home(request):
    doc_externo = loader.get_template('home.html')
    documento=doc_externo.render({})
    return HttpResponse(documento) 
    



def scrape (request, palabra_clave, numero):
    session =requests.Session()
    session.headers={"user agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    url="https://listado.mercadolibre.com.co/"+palabra_clave+"#D[A:"+palabra_clave+"]"
    content = session.get(url, verify=False).content 
    soup=BeautifulSoup(content,"html.parser")
    #columns =soup.find_all('div',{'class':'rowItem item highlighted item--stack item--has-row-logo new'})
    productos =soup.find_all('li',{'class':'results-item highlighted article stack'})
    print(len(productos))

    lista = [] 

    for i in productos:
        titulo = i.find_all('span',{'class':'main-title'})[0].text
        precio = i.find_all('span',{'class':'price__fraction'})[0].text
        if i.find_all('p'):
            envio = i.find_all('p')[0].text
        else:
            envio = i.find_all('div',{'class':'item__condition'})[0].text

        print(titulo)
        print(precio)  
        print(envio)
    
        nuevo_producto = Producto(titulo,precio,envio)
        lista.append(nuevo_producto)


    doc_externo = loader.get_template('lista.html')
    documento=doc_externo.render({"tam": numero, "lista":lista})
    return HttpResponse(documento)    
        

