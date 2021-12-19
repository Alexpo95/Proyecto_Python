import os
import sys
import shutil
import time


ruta_descargas = "/Users/alexpo/Downloads/"

ext_texto = [".pdf", ".txt", ".doc", ".docx", ".xlsx", ".xltx"]
ext_foto = [".png", ".jpg", ".jpeg", ".gif"]
ext_ejecutable = [".dmg"]
ext_libros = [".epub", ".mobi"]


extensiones = {
    "texto" : {"directorio" :"Texto/", "extension":[".pdf", ".txt", ".doc", ".docx", ".xlsx", ".xltx"]},
    "foto" : {"directorio" :"Fotos/", "extension":[".png", ".jpg", ".jpeg", ".gif"]},
    "ejecutable" : {"directorio" :"Ejecutables/", "extension":[".dmg"]},
    "libros" : {"directorio" :"Libros/", "extension":[".epub", ".mobi"]}
}


def ordenar_nueva(archivo, extension):
    ruta_origen = f"{ruta_descargas}{archivo}{extension}"
    renombrado = False 

    for key, value in extensiones.items():
        if renombrado: 
            break

        if extension in value["extension"]:
            renombrado = True
            ruta_destino = f'{ruta_descargas}{value["directorio"]}{archivo}{extension}'
            shutil.move(ruta_origen, ruta_destino)
        
    if not renombrado:
        if extension != "":
            ruta_destino = f'{ruta_descargas}Otros/{archivo}{extension}'
            shutil.move(ruta_origen,ruta_destino)

def ordenar(archivo, ext):

    renombrado = False

    for i in ext_texto:
        if ext == i:
            renombrado = True
            shutil.move(ruta_descargas + archivo + ext, 
            ruta_descargas + "Texto/" + archivo + ext)
    for i in ext_foto:
        if ext == i:
            renombrado = True
            shutil.move(ruta_descargas + archivo + ext,
                        ruta_descargas + "Fotos/" + archivo + ext)
    for i in ext_ejecutable:
        renombrado = True
        if ext == i:
            renombrado = True
            shutil.move(ruta_descargas + archivo + ext,
                        ruta_descargas + "Ejecutables/" + archivo + ext)
    for i in ext_libros:
        if ext == i:
            renombrado = True
            shutil.move(ruta_descargas + archivo + ext,
                        ruta_descargas + "Libros/" + archivo + ext)
    if not renombrado: 
        if ext != "":
            shutil.move(ruta_descargas + archivo + ext,
                        ruta_descargas + "Otros/" + archivo + ext)

    
    
def main():
    for archivo in os.listdir(ruta_descargas):
        nombre_archivo, ext = os.path.splitext(archivo)
        ordenar_nueva(nombre_archivo,ext)

main()
