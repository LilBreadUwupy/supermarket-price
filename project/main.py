from requests_html import HTMLSession
import urllib.request
from bs4 import BeautifulSoup

session = HTMLSession()


def get_central_products():
    url_central = urllib.request.urlopen('https://gamaenlinea.com/ALIMENTOS-FRESCOS/L%C3%A1cteos/Mantequilla-Margarina/MARGARINA-CON-SAL-NELLY-500-GR/p/10003343').read().decode()
    #r = session.get(url_central)

    #r.html.find("html body.page-productDetails.pageType-ProductPage.template-pages-product-productLayout2Page.smartedit-page-uid-productDetails.language-es main div div.product-details.page-title div.name", first = True).text

    soup = BeautifulSoup(url_central, features="lxml")
    div = soup.find('class="name"')
    print(div)

get_central_products()


