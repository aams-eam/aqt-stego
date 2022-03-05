from counter_bytes_tags2 import contadortags
from counter_bytes_tags2 import contadorcomillas
from attPosition import total_capacity as count_total_att
from attPosition import max_bits_line as max_bits_att_line
import requests
from requests.exceptions import ConnectionError
import html
import pandas as pd
import matplotlib.pyplot as plt
import re

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


def find_tags_line (input):

    matches = re.findall(r'<(.*?)>', input)
    return matches


def web_counter_att(htmlresponse):


    num = 0 # total num of attributes
    
    # expand tags in one line to multiple lines
    tags = []
    for line in htmlresponse.splitlines():
        tags += find_tags_line(line)

    # count bits in attributes base on the expanded lines
    for t in tags:
        complete = "<"+t+">"
        num += max_bits_att_line(complete)

    return num

def web_counter_tags(elem):
	'''print(elem)'''
	html = urlopen(elem)
	html_read=html.readlines()
	tags=0
	for line in html_read:
		tags+=contadortags(line)
		'''print(tags)'''
	return tags

def web_counter_quotes(elem):
	'''print(elem)'''
	html = urlopen(elem)
	html_read=html.readlines()
	quotes=0
	for line in html_read:
		quotes+=contadorcomillas(line)
		'''print(tags)'''
	return quotes

def web_counter_characters(elem):
	'''print(elem)'''
	html = urlopen(elem)
	html_read=html.readlines()
	size=0
	for line in html_read:
		characters=list(line)
		size+=len(characters)
		'''print(size)'''
	return size

def web_counter_lines(elem):
	'''print(elem)'''
	html = urlopen(elem)
	html_read=html.readlines()
	lines=0
	for line in html_read:
		lines+=1
		'''print(lines)'''
	return lines



def test():
    webpage_list=['https://www.google.com/','https://www.youtube.com/','https://www.facebook.com/']#,'https://twitter.com/','https://www.instagram.com/','http://www.baidu.com/','https://www.wikipedia.org/','https://yandex.ru/','https://es.yahoo.com/','https://www.elmundo.es/','https://www.whatsapp.com/','https://www.netflix.com/es/','https://www.uc3m.es/Inicio','https://vine.co/','https://www.yahoo.co.jp/','https://outlook.live.com/owa/','https://as.com/','https://zoom.us/','https://www.reddit.com/','https://elpais.com/','https://www.office.com/','https://www.spotify.com/es/','https://vk.com/','https://www.hola.com/','https://www.twitch.tv/','https://www.elperiodico.com/es/','https://www.naver.com/','https://www.bing.com/','https://www.roblox.com/','https://duckduckgo.com/','https://www.elespanol.com/','https://mail.ru/','https://www.pinterest.es/','https://www.defensa.gob.es/','https://www.qq.com/','https://news.yahoo.co.jp/','https://www.fandom.com/','https://www.msn.com/es-es/','https://www.google.com.br/','https://www.globo.com/','https://www.ebay.com/','https://www.rtve.es/','https://www.movistar.es/','https://weather.com/es-ES/tiempo/hoy/l/SPXX0050:1:SP?Goto=Redirected','https://ok.ru/','https://ok.ru/','https://www.bbc.com/','https://www.marca.com/','https://www.sport.es/es/','https://www.casadellibro.com/','https://www.w3schools.com/']
    x = web_counter_att(webpage_list)
    print(x)



def main():

    try:

        df = pd.read_csv("50topStatistics.csv")

    except FileNotFoundError as e:

        print("50topStatistics.csv does not exist, creating...")

        webpage_list=['https://www.google.com/','https://www.youtube.com/','https://www.facebook.com/']#,'https://twitter.com/','https://www.instagram.com/','http://www.baidu.com/','https://www.wikipedia.org/','https://yandex.ru/','https://es.yahoo.com/','https://www.elmundo.es/','https://www.whatsapp.com/','https://www.netflix.com/es/','https://www.uc3m.es/Inicio','https://vine.co/','https://www.yahoo.co.jp/','https://outlook.live.com/owa/','https://as.com/','https://zoom.us/','https://www.reddit.com/','https://elpais.com/','https://www.office.com/','https://www.spotify.com/es/','https://vk.com/','https://www.hola.com/','https://www.twitch.tv/','https://www.elperiodico.com/es/','https://www.naver.com/','https://www.bing.com/','https://www.roblox.com/','https://duckduckgo.com/','https://www.elespanol.com/','https://mail.ru/','https://www.pinterest.es/','https://www.defensa.gob.es/','https://www.qq.com/','https://news.yahoo.co.jp/','https://www.fandom.com/','https://www.msn.com/es-es/','https://www.google.com.br/','https://www.globo.com/','https://www.ebay.com/','https://www.rtve.es/','https://www.movistar.es/','https://weather.com/es-ES/tiempo/hoy/l/SPXX0050:1:SP?Goto=Redirected','https://ok.ru/','https://ok.ru/','https://www.bbc.com/','https://www.marca.com/','https://www.sport.es/es/','https://www.casadellibro.com/','https://www.w3schools.com/']


        # MODIFICAR IVAN
        lines = []
        characters = []
        att_cap = []
        quotes_cap = []
        tag_cap = []

        for elem in webpage_list:

            # hacer peticion html

            # calcular estadística solo de ese html
            print("COUNTING...")
            lines.append(web_counter_lines(elem))
            print("lines counted")
            characters.append(web_counter_characters(elem))
            print("characters counted")
            att_cap.append(web_counter_att(elem))
            print("attributes counted")
            quotes_cap.append(web_counter_quotes(elem))
            print("quotes counted")
            tag_cap.append(web_counter_tags(elem))
            print("tags counted")

            print(characters)
            print(lines)
            print(quotes_cap)
            print(tag_cap)
        # MODIFICAR IVAN

        df = pd.DataFrame({"page": webpage_list,"characters": characters,"lines": lines, "att_cap": att_cap, "quotes_cap": quotes_cap, "tag_cap": tag_cap})
        df.to_csv("50topStatistics.csv", index=False)

        df = pd.read_csv("50topStatistics.csv")



    df['totalbits'] = df['characters']*8
    df['att_percentage'] = 100*(df['att_cap']/df['totalbits'])
    df['quotes_percentage'] = 100*(df['quotes_cap']/df['totalbits'])
    df['tag_percentage'] = 100*(df['tag_cap']/df['totalbits'])

    # sort df by totalbits ascending
    df.sort_values('totalbits', ascending=True, inplace=True)
    df.reset_index(drop=True, inplace=True)
    print(df[['totalbits', 'att_percentage', 'quotes_percentage', 'tag_percentage']].head())


    plt.plot(df.index.to_list(), df.att_percentage.to_list(), label="att encoding")
    plt.plot(df.index.to_list(), df.quotes_percentage.to_list(), label="quote encoding")
    plt.plot(df.index.to_list(), df.tag_percentage.to_list(), label="tag encoding")
    plt.xlabel("Webpage index")
    plt.ylabel("encoding capacity over total capacity (%)")
    plt.title("Average capacity of encoding in top 50 visited pages")
    plt.legend()
    plt.grid()
    plt.show()




if __name__ == '__main__':
    main()
    # test()
