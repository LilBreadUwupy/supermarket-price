
def get_url(n):
    categories = ["VIVERES", "ALIMENTOS-FRESCOS", "BEBIDAS", "CUIDADO-PERSONAL", "LIMPIEZA", "HOGAR", "MASCOTAS", "OCASIÓN", "CUIDADO-DE-LA-SALUD"]
    categories_num = ["001", "002", "003", "004", "005", "006", "007", "008", "009"]
    for categorie in categories:
        cn = 0
        url = "https://gamaenlinea.com/{}/c/{}?q=%3Arelevance&page={}".format(categorie, categories_num[cn], n)
        cn += 1
        return url 


print(get_url(10))