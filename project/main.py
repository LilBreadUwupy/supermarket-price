from requests_html import HTMLSession

session = HTMLSession()


def get_excelsior_gamma_data():
    url = "https://gamaenlinea.com/ALIMENTOS-FRESCOS/L%C3%A1cteos/Mantequilla-Margarina/MARGARINA-CON-SAL-NELLY-500-GR/p/10003343"

    r = session.get(url)
    product = r.html.find(".name", first=True).text
    
    return product

get_excelsior_gamma_data()


