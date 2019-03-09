from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

# Sitio y variables
site= "https://www.encuentra24.com/panama-es/bienes-raices-venta-de-propiedades-apartamentos"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
#Parsear el HTML
page = urlopen(req)
page_soup = soup(page,"html.parser")

#La lista de containers
containers = page_soup.find_all("article", {"class":["ann-box-teaser ann-box-teaser-projects feat-super ann-box-teaser-small no-color", "ann-box-teaser ann-box-teaser-property feat-plat ann-box-teaser-small no-color"]})


#Poner en el vaina en excel
filename = "aptoseEncuentra24.csv"
f = open(filename, "w")

headers = "Titulo, Precio, Ubicacion, Espacio\n"

f.write(headers)



# Bucle para iterar en cada una de las vainas
for container in containers:
    titulo = container.find(itemprop="name").text
    precios = container.select(".ann-price")
    for precio in precios:
        precio.text
    ubicaciones = container.find_all("span",{"class":"ann-info-item"})
    for ubicacion in ubicaciones:
        ubicacion.text
    espacio = container.find_all("span",{"class":"value"})
    
    print("Titulo: " + titulo)
    print("Precio: " + precio.text)
    print("Ubicacion: " + ubicacion.text.replace("\n",""))
    print("Espacio: " + espacio[0].text)

    f.write(titulo.replace(","," ") + "," + precio.text.replace(",",".").replace("\n"," ") + "," + ubicacion.text.replace("\n"," ") + "," + espacio[0].text + "\n")

f.close()
    
    
    