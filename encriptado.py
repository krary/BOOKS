
import PyPDF2
from itertools import product
#CREANDO DICCIONARIO
def codigo():
 lista = [str(s) for s in range(10)]
 lista = list(product(lista,repeat=4))
 lista = [''.join(map(str,d)) for d in lista] 
 return lista

def encript():
 reader = PyPDF2.PdfReader("Fluent python.pdf")
 writer = PyPDF2.PdfWriter()
 for m in reader.pages:
  writer.add_page(m)
 writer.encrypt("1234")
 with open("Archivo_Encriptado.pdf",'wb') as file:
  writer.write(file)
 print("Archivo encriptado")





def func():
 lista = codigo()
 lista[600]=("marthasarmi123")
 reader = PyPDF2.PdfReader("Archivo_Encriptado.pdf")
 writer = PyPDF2.PdfWriter()
 
 if reader.is_encrypted:
  for m in lista:
   reader.decrypt(m)
  
  
 for m in reader.pages:
  writer.add_page(m)



 with open("documento_DESENCRIPTADO.pdf",'wb') as file:
  writer.write(file)

func()







 
 