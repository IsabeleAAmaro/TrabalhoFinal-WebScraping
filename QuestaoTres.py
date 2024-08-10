import re
import requests
from bs4 import BeautifulSoup


def search_book(url, book_title, site_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    selectors = {
        "Livraria da Travessa": {
            "price": "#gridBusca_ctl00_a_lblPreco"
        },
        "Estante Virtual": {
            "price": ".product-item__text"
        },
        "Sebo Virtual Da Rô": {
            "price": ".js-price-display.price.item-price"
        }
    }

    price_selector = selectors[site_name]["price"]

    results = []
    for result in soup.select(price_selector):
        price_text = result.text.strip()
        price_value = float(re.sub(r'\D', '', price_text))
        results.append((site_name, price_value))

    return results


def main():
    titulo_livro = "Criação"
    autor_primeiro_nome = "Gore"
    autor_segundo_nome = "Vidal"

    sites = [
        ("Sebo Virtual Da Rô", "https://www.sebovirtualdaro.com.br/search/?q=gore+vidal+criacao"),
        ("Estante Virtual", "https://www.estantevirtual.com.br/busca?nsCat=Natural&q=gore%20vidal%criacao"),
        ("Livraria da Travessa", "https://www.travessa.com.br/Busca.aspx?d=1&bt=gore%20vidal%20criacao&cta=00&codtipoartigoexplosao=1")]

    results = []
    for site_name, base_url in sites:
        site_results = search_book(base_url, titulo_livro, site_name)
        results.extend(site_results)

    results.sort(key=lambda x: x[1])

    print("Resultados da pesquisa:")
    for site, price in results:
        print(f"{site}: R${price:.1f}")


if __name__ == "__main__":
    main()
