docker build --no-cache -t test .
Building 31.1s
docker images
test        1.72GB

Optimisation: 
- On expose seulement le port 3000
- On utilise une image docker Alpine car elle est plus légère  donc la taille de l'image sera réduite
- Suite à ça on modifie la ligne 6 car on utilise apk comme gestionnaire de paquets par : 
    RUN apk update && apk add --no-cache build-base ca-certificates libc6-compat

- On récupère que les dépendenses avant le npm install et après on COPY 
- On sépare le runner et le builder pour gagner du temps et de la place (en récupérant que les fichiers utiles pour le runner).
- On utilise un user et pas root.

Après optimisation:
docker build --no-cache -t test .
Building 20.2s
docker images
test        253MB

