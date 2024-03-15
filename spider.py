import  requests
import  os
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


def get_url():
    while True:
        url = input("Mettre une url valide: ")
        if url.startswith("http://") or url.startswith("https://"):
            return url
        else:
            print("Url invalide, url valide commence par http/https")

def get_img(url, path):
    try:
        response = requests.get(url)
        content_type = response.headers.get('content-type', '')
        if content_type.startswith('image/jpeg') or \
           content_type.startswith('image/jpg') or \
           content_type.startswith('image/png') or \
           content_type.startswith('image/bmp') or \
           content_type.startswith('image/gif'):
            filename = os.path.basename(urlparse(url).path)
            with open(os.path.join(path, filename), 'wb') as f:
                f.write(response.content)
            print(f"Image enregistrée: {filename}")
        else:
            print(f"L'URL {url} n'a pas d'images.")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de l'image à partir de l'URL {url}: {str(e)}")


def main():
    url = get_url() 
    response = requests.get(url) 

    if response.status_code == 200: 
        print("Fichier en création... veuillez patientez")
        image_dir = "images"
        os.makedirs(image_dir, exist_ok=True)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url:
                img_url = urljoin(url, img_url)
                get_img(img_url, image_dir)
    else:
        print(f"Erreur pas pu obtenir la data de l'url, code d'état: {response.status_code}")

if __name__ == "__main__":
    main()