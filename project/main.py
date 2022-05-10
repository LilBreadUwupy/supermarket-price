from requests_html import HTMLSession
import re 

session = HTMLSession()
url = "https://gamaenlinea.com/ALIMENTOS-FRESCOS/L%C3%A1cteos/Mantequilla-Margarina/MARGARINA-CON-SAL-NELLY-500-GR/p/10003343"
r = session.get(url)

def get_excelsior_gamma_name():
    # Url = ""
    
    product = r.html.find(".name", first=True).text
    product = product.lower()
    product = re.split('id[a-z0-9]*', product)[0]

    return product


def get_excelsior_gamma_price():
    # url = ""

    price = r.html.find(".from-price-value", first=True).text
    price = re.split('Total Ref.[0-9.]*', price)[1]

    return price


def main():
    price = get_excelsior_gamma_price()
    product_name = get_excelsior_gamma_name()
    print(f"{product_name}: ${price}")


main()
