import re
link = "https://gamaenlinea.com/ALIMENTOS-FRESCOS/Productos-del-Campo/Huevos/HUEVOS-FRESCOS-EXCELSIOR-GAMA-%28A%29-12-UN/p/10025636"


category= str(re.findall('https://gamaenlinea.com/([A-Z0-9-%]*)/', link))
category = category.replace('[', '').replace("'", "").replace("]", "")
print(type(link))