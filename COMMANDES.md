    1  docker version
    2  git clone https://github.com/Legeni07/devops_keyce.git
    3  sudo docker ps
    4  docker version
    5  sudo docker ps
    6  tree /home/etobe/devops_keyce -L 2
    7  find /home/etobe/devops_keyce -type f -name "*.md" | sort
    8  cat "/home/etobe/devops_keyce/TP docker/TP Docker.md"
    9  bash /home/etobe/devops_keyce/TP_docker_automation.sh
   10  chmod +x /home/etobe/devops_keyce/TP_docker_automation.sh
   11  bash /home/etobe/devops_keyce/TP_docker_automation.sh
   12  chmod +x TP_docker_automation.sh
   13  bash TP_docker_automation.sh
   14  chmod +x TP_docker_automation.sh
   15  ./TP_docker_automation.sh
   16  docker compose up -d
   17  docker pull jenkins/jenkins:lts
   18  cd ~/tp2_webapp
   19  # On supprime tout ce qui est raté et on clone ton projet
   20  rm -rf *
   21  git clone https://github.com/Legeni07/legeni_webapp.git
   22  cat <<EOF > Dockerfile
   23  FROM nginx:latest
   24  # On copie le contenu de ton dossier cloné vers le dossier web de Nginx
   25  COPY legeni_webapp /usr/share/nginx/html
   26  EXPOSE 80
   27  EOF
   28  docker build -t legeni-webapp:v1 .
   29  docker run -d -p 8081:80 --name mon-legeni-site legeni-webapp:v1
   30  # Créer le réseau
   31  docker network create reseau_keyce
   32  # Créer le volume persistant
   33  docker volume create volume_partage
   34  # Lancer B3_jour
   35  docker run -itd --name B3_jour --network reseau_keyce -v volume_partage:/data ubuntu
   36  # Lancer B3_soir
   37  docker run -itd --name B3_soir --network reseau_keyce -v volume_partage:/data ubuntu
   38  docker exec B3_jour sh -c "echo 'Rapport du matin : Tout est OK' > /data/rapport.txt"
   39  cd legeni_webapp
   40  npm install
   41  # ou
   42  yarn install
   43  cd ..
   44  cd legeni_webapp
   45  git clone https://github.com/Legeni07/legeni_webapp.git
   46  cd legeni_webapp
   47  npm install
   48  # ou
   49  yarn install
   50  sudo yarn install
   51  pip install -r requirements.txt
   52  sudo apt install python3-pip
   53  git clone https://github.com/Legeni07/devops_keyce.git
   54  cd devops_keyce
   55  curl -fsSL https://get.docker.com -o get-docker.sh
   56  sudo sh get-docker.sh --version 20.10.13
   57  sudo usermod -aG docker $USER
   58  sudo systemctl start docker
   59  sudo systemctl enable docker
   60  sudo curl -SL "https://github.com/docker/compose/releases/download/v2.23.3/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose
   61  sudo chmod +x /usr/local/bin/docker-compose
   62  docker-compose -v
   63  sudo curl -SL "https://github.com/docker/compose/releases/download/v2.23.3/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose
   64  sudo chmod 666 /var/run/docker.sock
   65  docker exec -it -u root jenkins-install-jenkins-1 bash -c "apt-get update && apt-get install -y docker.io git && usermod -aG docker jenkins"
   66  cd ~/devops_keyce/jenkins-install
   67  docker compose up -d
   68  docker ps
   69  docker exec -it -u root jenkins-install-jenkins-1 bash -c "apt-get update && apt-get install -y docker.io git && usermod -aG docker jenkins"
   70  sudo chmod 666 /var/run/docker.sock
   71  nano ~/devops_keyce/start_lab.sh
   72  chmod +x ~/devops_keyce/start_lab.sh
   73  ./devops_keyce/start_lab.sh
   74  # Créer B3_jour
   75  docker run -itd --name B3_jour ubuntu
   76  # Créer B3_soir
   77  docker run -itd --name B3_soir ubuntu
   78  docker network create -d bridge mon_reseau
   79  docker network connect mon_reseau B3_jour
   80  docker network connect mon_reseau B3_soir
   81  docker network inspect mon_reseau
   82  docker volume create mon_volume_temporaire
   83  docker rm -f B3_jour B3_soir
   84  docker run -d --name B3_jour --network mon_reseau -v mon_volume_temporaire:/tmp ubuntu sleep infinity
   85  docker run -d --name B3_soir --network mon_reseau -v mon_volume_temporaire:/tmp ubuntu sleep infinity
   86  docker exec B3_jour sh -c "echo 'Bonjour depuis le jour' > /tmp/fichier.txt"
   87  docker exec B3_soir cat /tmp/fichier.txt
   88  docker volume create mon_volume_persistant
   89  docker rm -f B3_jour B3_soir
   90  docker run -d --name B3_jour -v mon_volume_persistant:/mnt ubuntu sleep infinity
   91  docker run -d --name B3_soir -v mon_volume_persistant:/mnt ubuntu sleep infinity
   92  docker exec B3_jour sh -c "echo 'Cette donnée doit survivre' > /mnt/sauvegarde.txt"
   93  docker stop B3_jour B3_soir
   94  docker rm B3_jour B3_soir
   95  docker volume ls
   96  docker run --rm -v mon_volume_persistant:/verif ubuntu cat /verif/sauvegarde.txt
   97  docker volume rm mon_volume_temporaire
   98  docker volume rm mon_volume_persistant
   99  docker network rm mon_reseau
  100  script -a ~/mon_journal_devops.log
  101  wsl lsmod | grep tun
  102  sudo modprobe tun
  103  sudo apt install wsl
  104  lsmod | grep tun
  105  sudo modprobe tun
  106  history > COMMANDES.md
