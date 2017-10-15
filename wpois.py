import requests, sys
from bs4 import BeautifulSoup

print("""
\t\t\t------------------------------
\t\t\t--==[     Turkz Grup     ]==--
\t\t\t--==[       Ar-Ge        ]==--
\t\t\t--==[       Ruddy        ]==--
\t\t\t------------------------------""")


def tema():
    try:
        site = "https://www.wpthemedetector.com/ad/addir/themes/WPTD2/wptd_main.php"
        veri = {"urljs": wpsite}
        request = requests.post(site, data=veri)
        dosya = BeautifulSoup(request.content, "html.parser")
        gelenveri = dosya.find_all("div",{"class":"theme_name"})
        bilgiler = dosya.find_all("div",{"class":"theme_right_left"})
        sonuc = (gelenveri[0].contents)[len(gelenveri[0].contents)-4]
        bilgiler = bilgiler[0].text
        bilgiler = bilgiler.replace("/n", " ")
        bilgiler = bilgiler.replace("""
""", "")
        bilgiler = bilgiler.replace(""" 													""", "\n")
        bilgiler = bilgiler.replace("												 ", "\n")

        temaadi = sonuc.text

        print(wpsite + " sitesi için\nTema adı:  " + temaadi)
        print(bilgiler + "\n")
    except:
        print(wpsite + " Sitesinde Wordpress teması tespit edilemedi.\n")

def whois():
    try:
        site1 = ("http://www.whoistr.org/whois.html?q=" + wpsite)
        veri1 = {"q": wpsite}
        whoiss = requests.get(site1, data=veri1)
        sonuc1 = BeautifulSoup(whoiss.content, "html.parser")
        whois_veri = sonuc1.find_all("table", {"class": "resulttable"})
        tablo = (whois_veri[0].contents)[len(whois_veri[0].contents)-2]
        tablo = tablo.find_all("tr")
        print("WHOiS BiLGiLERi:")
        for whois_sonuc in tablo:
            whois1 = whois_sonuc.find_all("td")
            whoiss = whois1[0].text + " : " + whois1[1].text
            whoiss = whoiss.replace("\n", " ")
            print(whoiss)
    except:
        print("Üzgünüz, '{}' bulunamadı.".format(wpsite))

try:
    wpsite = sys.argv[2]

    f0 = sys.argv[0]
    f1 = sys.argv[1]
    f2 = sys.argv[2:]

    if len(sys.argv) > 2:
        if f1 == "-t":
            tema()
        elif f1 == "-w":
            whois()
        elif f1 == "-a":
            tema()
            whois()
        else:
            print("Hatalı Kullanım!")
    else:
        print("Hatalı Kullanım!")
except:
    print("""
    Wordpress Tema Sorgulama:
        python wpois.py -t siteadresi.com
    Whois Bilgileri Sorgulama:
        python wpois.py -w siteadresi.com
    Tema ve Whois Bilgileri Sorgulama:
        python wpois.py -a siteadresi.com""")
