import requests
from bs4 import BeautifulSoup

def imprimir_mensaje_secreto(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("No se pudo acceder al documento.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    table_rows = soup.find_all("tr")
    datos = []

    for row in table_rows[1:]:
        cols = row.find_all("td")
        if len(cols) == 3:
            x = int(cols[0].text.strip())
            char = cols[1].text.strip()
            y = int(cols[2].text.strip())
            datos.append((x, y, char))

    if not datos:
        print("No se encontraron datos en la tabla.")
        return

    max_x = max(x for x, y, char in datos)
    max_y = max(y for x, y, char in datos)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]


    for x, y, char in datos:
        grid[y][x] = char

    for row in grid:
        print(''.join(row))

# URL del documento
url = "https://docs.google.com/document/d/e/2PACX-1vSCJGXDu491Y3rRgJPVhtdsY5ivkbQ5FJMDvPyanh2F7HNk2cea9AZIHa1j-RShETAsCxKqqbZ_Vz7J/pub"

imprimir_mensaje_secreto(url)
