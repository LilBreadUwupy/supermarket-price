from requests_html import HTMLSession


session = HTMLSession()


def get_planzuares_products():
    url_planzuares = "https://tucentralonline.com/Plaza-Las-Americas-03/tienda/"
    r = session.get(url_planzuares)

    # r.html.find('li.product-col:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(2) > h3:nth-child(1)')

    return r


print(get_planzuares_products())



