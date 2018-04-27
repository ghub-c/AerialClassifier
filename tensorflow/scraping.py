from bs4 import BeautifulSoup
import urllib2
import os
import argparse
import sys
import json


def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def main(args):

    parser = argparse.ArgumentParser(description='Descargando imagenes de google')
    parser.add_argument('-s', '--search', default='car', type=str, help='Termino que deseas buscar')
    parser.add_argument('-n', '--num_images', default=10, type=int, help='Numero de imagenes a descargar')
    parser.add_argument('-he', '--height', default=-1, type=int, help='Altura de la imagen')
    parser.add_argument('-w', '--width', default=-1, type=int, help='Ancho de la imagen')
    parser.add_argument('-t', '--type', default='jpg', type=str, help='Formato de la imagen')
    parser.add_argument('-d', '--directory', default='/Users/guillemmunozferran/Desktop', type=str, help='Directorio destino')
    args = parser.parse_args()

    query = args.search
    max_images = args.num_images
    height = args.height
    if args.width == (-1):
        width = height
    else:
        width = str(args.width)
    save_directory = args.directory
<<<<<<< HEAD

=======
    imType = args.type
>>>>>>> e839da11fc573dae44505f733cafcfb1568e45e9
    image_type="Action"
    query= query.split()
    query='+'.join(query)
    if height == -1:
        url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch&tbs=ift:"+imType
    else:
        url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch&tbs=ift:"+imType+",isz:ex,iszw:"+str(width)+",iszh:"+str(height)
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url,header)
    ActualImages=[]# contains the link for Large original images, type of  image
    for a in soup.find_all("div", {"class": "rg_meta"}):
        link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
        ActualImages.append((link, Type))
    for i, (img, Type) in enumerate(ActualImages[0:max_images]):
        try:
            req = urllib2.Request(img, headers={'User-Agent': header})
            raw_img = urllib2.urlopen(req).read()
            if len(Type) == 0:
                f = open(os.path.join(save_directory, "img" + "_" + str(i) + ".jpg"), 'wb')
            else:
               f = open(os.path.join(save_directory, "img" + "_" + str(i) + "." + Type), 'wb')
            '''if Type=="jpg":
                f = open(os.path.join(save_directory, "img" + "_" + str(i) + "." + Type), 'wb')
                f.write(raw_img)
                f.close()'''
            f.write(raw_img)
            f.close()
        except Exception as e:
            print "could not load : " + img
            print e


if __name__ == '__main__':
    from sys import argv

    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()