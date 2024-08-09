import requests
from bs4 import BeautifulSoup
import re

"""
Faça um programa Python que pesquisa preços do livro “Criação” de Gore
Vidal. O programa deve pesquisar os preços em três diferentes sites (escolhidos por você) e
selecionar o de menor valor em cada site (apenas primeira página). No final, o programa
deve apresentar os valores da compra e os sites de venda. A lista deve ser apresentada por
ordem crescente do valor do produto.
"""

"""
Função para pesquisar um livro em um site específico.

Args:
    url (str): URL da página de busca do site.
    book_title (str): Título do livro a ser pesquisado.

Returns:
    list: Lista de tuplas (preço, link), ou None se nenhum resultado for encontrado.
"""


def search_book(url, book_title):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for error HTTP status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Aqui você precisa adaptar o seletor CSS ou XPath para encontrar os elementos que contêm o preço e o link do
        # livro Por exemplo, para encontrar todos os elementos <div> com a classe "product-price":
        prices = soup.find_all('div', class_='product-price')

        results = []
        for price in prices:
            # Extrai o preço do elemento, removendo caracteres não numéricos
            price_text = price.text.strip()
            price_value = float(re.sub(r'\D', '', price_text))

            # Encontra o link do produto (ajuste o seletor conforme a estrutura do site)
            link = price.find_next('a')['href']

            results.append((price_value, link))

        return results
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar no site {url}: {e}")
        return None


# Lista de sites e suas URLs de busca (substitua pelos URLs reais)
sites = [
    ("Amazon", "https://www.amazon.com.br/s?k=Cria%C3%A7%C3%A3o+Gore+Vidal"),
    ("Submarino", "https://www.submarino.com.br/busca?q=Cria%C3%A7%C3%A3o+Gore+Vidal"),
    # Adicione outros sites aqui
]

book_title = "Criação"
author = "Gore Vidal"

results = []
for site_name, url in sites:
    site_results = search_book(url, book_title)
    if site_results:
        results.extend([(site_name, price, link) for price, link in site_results])

# Ordena os resultados por preço
results.sort(key=lambda x: x[1])

# Imprime os resultados
print("Resultados da pesquisa:")
for site, price, link in results:
    print(f"{site}: R${price:.2f} - {link}")
