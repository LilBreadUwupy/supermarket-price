from requests_html import HTMLSession

session = HTMLSession()


def get_central_products():
    url_central = "https://tucentralonline.com/Plaza-Las-Americas-03/tienda/"
    r = session.get(url_central)

    # r.html.find('li.product-col:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(2) > h3:nth-child(1)')

    return r


print(get_central_products())



