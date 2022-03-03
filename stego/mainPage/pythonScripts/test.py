import os
from remove_line import remove_line_html
from statistics import web_counter_tags
from statistics import web_counter_quotes
from statistics import web_counter_characters
from statistics import web_counter_lines

'''LEO EL HTML Y QUITO UNA LINEA AL AZAR'''
with open(os.getcwd()+"\\responseContent.html") as fd:
    content = fd.read()
html_line_removed=remove_line_html(content)
print(html_line_removed)

'''LISTA DE PAGINAS WEBS A ANALIZAR'''
webpage_list=['https://www.google.com/','https://www.youtube.com/','https://www.facebook.com/','https://twitter.com/','https://www.instagram.com/','http://www.baidu.com/','https://www.wikipedia.org/','https://yandex.ru/','https://es.yahoo.com/','https://www.elmundo.es/','https://www.whatsapp.com/','https://www.netflix.com/es/','https://www.uc3m.es/Inicio','https://vine.co/','https://www.yahoo.co.jp/','https://outlook.live.com/owa/','https://as.com/','https://zoom.us/','https://www.reddit.com/','https://elpais.com/','https://www.office.com/','https://www.spotify.com/es/','https://vk.com/','https://www.hola.com/','https://www.twitch.tv/','https://www.elperiodico.com/es/','https://www.naver.com/','https://www.bing.com/','https://www.roblox.com/','https://duckduckgo.com/','https://www.elespanol.com/','https://mail.ru/','https://www.pinterest.es/','https://www.defensa.gob.es/','https://www.qq.com/','https://news.yahoo.co.jp/','https://www.fandom.com/','https://www.msn.com/es-es/','https://www.google.com.br/','https://www.globo.com/','https://www.ebay.com/','https://www.rtve.es/','https://www.movistar.es/','https://weather.com/es-ES/tiempo/hoy/l/SPXX0050:1:SP?Goto=Redirected','https://ok.ru/','https://ok.ru/','https://www.bbc.com/','https://www.marca.com/','https://www.sport.es/es/','https://www.casadellibro.com/','https://www.w3schools.com/']

'''RECOJO EL NUMERO DE BITS QUE CABEN EN LOS TABS DE CADA PAGINA WEB'''
webpage_number_tags=web_counter_tags(webpage_list)
'''RECOJO EL NUMERO DE BITS QUE CABEN EN LOS QUOTES DE CADA PAGINA WEB'''
webpage_number_quotes=web_counter_quotes(webpage_list)
'''RECOJO EL NUMERO DE CARACTERES QUE HAY EN CADA PAGINA WEB'''
webpage_length=web_counter_characters(webpage_list)
'''RECOJO EL NUMERO DE LINEAS DE CADA UNO DE LOS HTMLS DE LA PAGINA WEB'''
webpage_lines=web_counter_lines(webpage_list)
