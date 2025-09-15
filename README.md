PS C:\Users\ilona\Documents\MIAGE M2\Docker\TPDocker> docker images
REPOSITORY      TAG       IMAGE ID       CREATED        SIZE
mon-app-flask   latest    6b252d063aa9   23 hours ago   225MB
nginx           latest    33e0bbc7ca9e   3 weeks ago    281MB
hello-world     latest    a0dfb02aac21   3 weeks ago    16.9kB
PS C:\Users\ilona\Documents\MIAGE M2\Docker\TPDocker>Windows PowerShell
Copyright (C) Microsoft Corporation. Tous droits réservés.

Installez la dernière version de PowerShell pour de nouvelles fonctionnalités et améliorations ! https://aka.ms/PSWindows

PS C:\Users\ilona> docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
PS C:\Users\ilona> docker images
REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
hello-world   latest    a0dfb02aac21   3 weeks ago   16.9kB
PS C:\Users\ilona> docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

PS C:\Users\ilona> docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
PS C:\Users\ilona>docker ps -a  
CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
4fa13d036c64   hello-world   "/hello"   2 minutes ago   Exited (0) 2 minutes ago             xenodochial_shtern
PS C:\Users\ilona> docker rm 4fa13d036c64  
4fa13d036c64
PS C:\Users\ilona> docker rmi <ID_image>^C
PS C:\Users\ilona> docker rmi a0dfb02aac21
Untagged: hello-world:latest
Deleted: sha256:a0dfb02aac212703bfcb339d77d47ec32c8706ff250850ecc0e19c8737b18567
PS C:\Users\ilona> docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
8820d4aadbcd: Pull complete
ddc6b36d0e36: Pull complete
baccdd222209: Pull complete
9a80f9a05524: Pull complete
d8ded761e35b: Pull complete
26be9a3603ae: Pull complete
8db204c3cb06: Pull complete
Digest: sha256:33e0bbc7ca9ecf108140af6288c7c9d1ecc77548cbfd3952fd8466a75edefe57
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
PS C:\Users\ilona> docker run -d -p 8080:80 --name mon_nginx nginx
bded39fdd9a830649e14f13471d69ad5d3b46709b5c26a763b3e2738c94e845c
PS C:\Users\ilona> docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                     
NAMES
bded39fdd9a8   nginx     "/docker-entrypoint.…"   15 seconds ago   Up 14 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   mon_nginx
PS C:\Users\ilona>docker stop mon_nginx
mon_nginx
PS C:\Users\ilona> docker rm mon_nginx
mon_nginx
PS C:\Users\ilona> docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        latest    33e0bbc7ca9e   3 weeks ago   281MB
PS C:\Users\ilona> docker pull hello-world 
Using default tag: latest
latest: Pulling from library/hello-world
198f93fd5094: Pull complete
Digest: sha256:a0dfb02aac212703bfcb339d77d47ec32c8706ff250850ecc0e19c8737b18567
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest
PS C:\Users\ilona>^C
PS C:\Users\ilona>cd "C:\Users\ilona\Documents\MIAGE M2\Docker\TPDocker"
PS C:\Users\ilona\Documents\MIAGE M2\Docker\TPDocker> ls


    Répertoire : C:\Users\ilona\Documents\MIAGE M2\Docker\TPDocker


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        04/09/2025     08:43            380 app.py
-a----        04/09/2025     08:53            374 dockerfile
-a----        04/09/2025     08:52             16 requirements.txt


PS C:\Users\ilona\Documents\MIAGE M2\Docker\TPDocker>docker build -t mon-app-flask .
>>
[+] Building 23.2s (11/11) FINISHED                                                                     docker:desktop-linux
 => [internal] load build definition from dockerfile                                                                    0.0s
 => => transferring dockerfile: 413B                                                                                    0.0s 
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                      3.8s 
 => [auth] library/python:pull token for registry-1.docker.io                                                           0.0s
 => [internal] load .dockerignore                                                                                       0.0s
 => => transferring context: 2B                                                                                         0.0s 
 => [internal] load build context                                                                                       0.0s 
 => => transferring context: 476B                                                                                       0.0s 
 => [1/5] FROM docker.io/library/python:3.9-slim@sha256:914169c7c8398b1b90c0b0ff921c8027445e39d7c25dc440337e56ce0f256  13.8s 
 => => resolve docker.io/library/python:3.9-slim@sha256:914169c7c8398b1b90c0b0ff921c8027445e39d7c25dc440337e56ce0f2566  0.0s
 => => sha256:b38cfd2e2711273a72ab8dcb95595250743106ae0ca013c3dcf8598f84d5dfce 249B / 249B                              0.5s 
 => => sha256:0f291c091a119dcb47f14c42ef78b6b3d8122caa7abc118407b6f5627c54725f 13.32MB / 13.32MB                        3.1s 
 => => sha256:3cd5add3ba3330f959ed1b27096bfb25e2f29a4cf327009d69855a903036f3af 1.27MB / 1.27MB                          1.2s 
 => => sha256:9a6263cdeaa5d408640880103ee36920ef814974ca8e2674412ad6460e8968c9 30.14MB / 30.14MB                       12.1s 
 => => extracting sha256:9a6263cdeaa5d408640880103ee36920ef814974ca8e2674412ad6460e8968c9                               1.0s 
 => => extracting sha256:3cd5add3ba3330f959ed1b27096bfb25e2f29a4cf327009d69855a903036f3af                               0.1s 
 => => extracting sha256:0f291c091a119dcb47f14c42ef78b6b3d8122caa7abc118407b6f5627c54725f                               0.5s 
 => => extracting sha256:b38cfd2e2711273a72ab8dcb95595250743106ae0ca013c3dcf8598f84d5dfce                               0.0s 
 => [2/5] WORKDIR /app                                                                                                  0.2s 
 => [3/5] COPY requirements.txt .                                                                                       0.0s 
 => [4/5] RUN pip install -r requirements.txt                                                                           4.3s 
 => [5/5] COPY app.py .                                                                                                 0.1s 
 => exporting to image                                                                                                  0.8s 
 => => exporting layers                                                                                                 0.4s 
 => => exporting manifest sha256:9b8556dca14eb3fff21583a6f1913f09a483ea3cc195ea6c1321717ccffcd7fe                       0.0s 
 => => exporting config sha256:d934e9c56c51902b7ab0aa1058c11b481ec4e93d627c779be4549d25c109ea50                         0.0s 
 => => exporting attestation manifest sha256:70375b77e841de30b0f3efbaaf578e313d6096ed3a75d2eec9e42536738bd6c3           0.0s 
 => => exporting manifest list sha256:6b252d063aa91fd6115b9e07cd1342038dd4a9922a2a02fe1670a6c874de0e72                  0.0s 
 => => naming to docker.io/library/mon-app-flask:latest                                                                 0.0s 
 => => unpacking to docker.io/library/mon-app-flask:latest                                                              0.3s 
PS C:\Users\ilona\Documents\MIAGE M2\Docker\TPDocker> docker images
>>
REPOSITORY      TAG       IMAGE ID       CREATED          SIZE
mon-app-flask   latest    6b252d063aa9   15 seconds ago   225MB
nginx           latest    33e0bbc7ca9e   3 weeks ago      281MB
hello-world     latest    a0dfb02aac21   3 weeks ago      16.9kB
PS C:\Users\ilona\Documents\MIAGE M2\Docker\TPDocker> docker run -p 5000:5000 mon-app-flask
>>
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 109-526-401
172.17.0.1 - - [04/Sep/2025 06:56:51] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [04/Sep/2025 06:56:51] "GET /favicon.ico HTTP/1.1" 404 -
172.17.0.1 - - [04/Sep/2025 06:57:10] "GET /test HTTP/1.1" 404 -
172.17.0.1 - - [05/Sep/2025 06:13:23] "GET / HTTP/1.1" 200 -
PS C:\Users\ilona\Documents\MIAGE M2\Docker\TPDocker> docker imageq
docker: unknown command: docker imageq

Run 'docker --help' for more information
PS C:\Users\ilona\Documents\MIAGE M2\Docker\TPDocker> docker images
REPOSITORY      TAG       IMAGE ID       CREATED        SIZE
mon-app-flask   latest    6b252d063aa9   23 hours ago   225MB
nginx           latest    33e0bbc7ca9e   3 weeks ago    281MB
hello-world     latest    a0dfb02aac21   3 weeks ago    16.9kB
PS C:\Users\ilona\Documents\MIAGE M2\Docker\TPDocker># TpDocker
