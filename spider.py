import  requests

def get_url():
    while True:
        url = input("Mettre une url valide: ")
        if url.startswith("http://") or url.startswith("https://"):
            return url
        else:
            print("Url invalide, url valide commence par http/https")

def main():
    url = get_url() 
    response = requests.get(url) #permet de faire une requete http de l'url

    if response.status_code == 200: #200 est le code d'état pour dire que c'est fonctionnel et que le site est pas down
        print("Fichier en création... veuillez patientez environ 2min45 :)")
        with open("data.txt", "w", encoding="utf-8") as i:      #création du fichier pour ecrire toute la data dedans
            i.write(response.text)
        print("c'est bon fichier crée data.txt avec toutes les infos dedans")
    else:
        print(f"Erreur pas pu obetnir la data de l'url, code d'état: ", response.status_code)

if __name__ == "__main__":
    main()