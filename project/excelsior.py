from requests_html import HTMLSession

session = HTMLSession()

url = "https://gamaenlinea.com/VIVERES/c/001?q=%3Arelevance&page=0"

r = session.get(url)

print(r.html.links)

