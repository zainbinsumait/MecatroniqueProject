# Mecatronique Project
  
  

  
  

# Semestre 7, UE Mécatronique 2, intitulé Mécatronique :

  

### Projet : Tutoriel pour suivi de ligne par un robot wifibot

  

![](https://lh6.googleusercontent.com/BNNYtXb__yJdJhemwoB6LgUrfZvLq9xkpYZRT8oD8H45G2SvtTZDtjaAhvf5rHVvFLagCS1kGmAWJ02pQyh1IC7XZJr40shrV8HJhnydkgGOOhHXY5H2gZhf6zcIrj-rWCS3garW)

  

# Introduction : #

  

Notre équipe est composée d’étudiants de 4ème année ESIREM parcours robotique & instrumentation. 

Ces étudiants sont :

* Bin Sumait Zain 
* Dumas Maxime
* Fourneret Lucas
* Ibral Marwan
* Novo Lucas
* Riffard Alexandre
    

***Ce projet est supervisé par Monsieur KORTLI Y***

Notre objectif est la détection et le suivi de ligne par le robot wifibot grâce à une carte NVIDIA Jetson Nano et une caméra.

Nous utiliserons pour réaliser ce projet le middleware R.O.S melodic. Nous avons sur notre carte NVIDIA Jetson Nano Ubuntu 18.04.6 LTS.

Liste du matériel nécessaire au projet :

* Robot wifibot
* Carte NVIDIA Jetson Nano developer kit Ubuntu 18.04.6 LTS (/!\ Pas de WIFI/Bluetooth)
* Caméra/Webcam
* Support de carte et de caméra imprimé en 3D
* Moniteur 
* Clavier
* Câble série
* Piste avec marquages pour effectuer la détection de lignes
    


## Table des matières 

1. Connexion de la carte NVIDIA Jetson Nano au réseau	
2. Mise à jour de la carte NVIDIA Jetson Nano 	
3. Installation de R.O.S melodic	
4. Test de la caméra	
5. Connexion au robot	
6. Test du robot	
7. Téléopération au clavier	
8. Capture d’images	
9. Détection de lignes	




## 1.  Connexion de la carte NVIDIA Jetson Nano au réseau 



-   Brancher sur la carte NVIDIA Jetson Nano un moniteur, un clavier et une souris.
    
-   Brancher la carte NVIDIA Jetson Nano au secteur et démarrer la carte.
    
-   Connecter la carte NVIDIA Jetson Nano au réseau via un câble ethernet, si impossibilité de brancher au réseau, utiliser un partage de connexion via USB depuis un téléphone portable.

  

Une fois que votre carte est connectée au réseau, passez à l’étape suivante. Gardez le moniteur et le clavier branchés sur la carte.




## 2.  Mise à jour de la carte NVIDIA Jetson Nano 
    

Sur la carte NVIDIA Jetson Nano :

-   Ouvrir un terminal
    
-   Entrer la commande
```bash
sudo apt-get update
```

    
-   Entrer la commande 
```bash
sudo apt-get upgrade
```
    

  
  

## 3. Installation de R.O.S melodic
    

Source : [installez](http://wiki.ros.org/melodic/Installation/Ubuntu) 

  

Sur la carte NVIDIA Jetson Nano :

-   Ouvrir un terminal
    
-   Configurez vos référentiels d’installation de logiciels pour autoriser les programmes Ubuntu “restreint”(restricted), “univers”(universe) et “multivers”(multiverse). En cas de problème, consultez le tutoriel disponible [ici](https://help.ubuntu.com/community/Repositories/Ubuntu) 
    
-   Entrer la commande suivante pour que l’ordinateur puisse accepter les packages de packages.ros.org : 

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
    
-   Configuration de vos clés, entrer la commande suivante : 
```bash
sudo apt install curl
```    

  

-   Entrer la commande suivante :
```bash
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```
    
-   Mettre à jour le système d’exploitation, entrer la commande suivante : 
```bash
sudo apt update
```
    
-   Installer R..O.S Melodic, entrer la commande suivante : 

```bash
sudo apt install ros-melodic-desktop-full 
```

  
- Entrer les commandes suivantes afin que les variables d’environnement de ROS soient ajoutées au bash chaque fois qu’un nouveau terminal est ouvert :
```bash
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc 
source ~/.bashrc
```

-   Pour créer et gérer vos propres espaces de travail R.O.S, installer les programmes suivants en entrant cette commande : 
```bash
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
```
    
-   Initialiser rosdep, entrez les commandes suivantes pour l’installer et l’initialiser : 
```bash
sudo apt install python-rosdep
    
sudo rosdep init

rosdep update
```
  

Ensuite, créez les dossiers dans lesquels nous allons travailler :

-   Créer un dossier catkin_ws : 
```bash
mkdir catkin_ws
```
	
-   Aller dans le dossier catkin_ws : 

```bash
cd catkin_ws
```
	
-   Créer un dossier src : 
```bash
mkdir src
```

-   Entrer dans le dossier src : 
```bash
cd src
```

-   Importer le package que nous avons créé pour notre robot : 
```bash
git clone https://github.com/zainbinsumait/rov_r
```

-   Importer le github roswifibot : 
```bash
git clone https://github.com/arnaud-ramey/roswifibot
```

-   Revenir dans le dossier catkin_ws : 
```bash
cd ..
```

-   Entrer la commande suivante : 
```bash
catkin_init_workspace
```
	
-   Entrer la commande suivante : 
```bash
catkin_make
```

  
  

## 3.  Test de la caméra
    

  

Importation d’un package dans le dossier src pour tester la caméra. 

-   Ouvrir un terminal
    
-   Se déplacer vers le dossier src créé précédemment : 
```bash
cd catkin_ws/src
```

-   Cloner le dossier github de test de la caméra : 

```bash
git clone https://github.com/ros-drivers/usb_cam
```

    
  

Pour que ROS puisse reconnaître les packages que l’on va utiliser, on entre dans le terminal les commandes suivantes :

```bash

source devel/source.bash
    
catkin_make
    
source devel/setup.bash
    
```
  

Test de la caméra : 

Dans le terminal, entrez la commande suivante : 

```bash
roslaunch usb_cam usb_cam-test.launch
```
  
  

***NB : Si vous rencontrez des difficultés pour exécuter un fichier, vous n’avez peut-être pas les droits d’exécution. Pour vérifier les droits des fichiers, entrez dans le terminal la commande : ls -la. Si le fichier que vous voulez exécuter n’a pas la permission “x”, vous devez lui donner avec la commande :***
```bash
chmod 777 nom_de_votre_fichier. 
```

***Cette commande permet de donner les droits de lecture, d’écriture et d’exécution à tous les groupes qui peuvent accéder à la carte (utilisateurs, groupes et autres)***

## 4. Connexion au robot
    

  

-   Brancher le câble série entre la carte NVIDIA Jetson Nano et le robot
    
-   Exécuter le fichier dans le terminal : 
    
```bash
roslaunch roswifibot robot_launch.launch robot:=robot
```

Cette commande établit la connexion entre le robot et la carte, en envoyant des informations sur le robot.si la connexion n’a pas pu s’effectuer, vous trouverez des erreurs qui s'afficheront dans le terminal. Pour éviter ce genre d’erreur vous devez suivre ces étapes:

1.  soyez sûr que le robot est bien branché et que le câble fonctionne bien.
    
2.  vérifier les droits des ports en tapant la commande : 
```bash
ls -al /dev/tty*
```

3.  pour donner le droit de l'exécution des ports USB, tapez la commande :
```bash
 chmod 777 /dev/ttyUSB* 
```

  
  

## 5. Test du robot
    

  

-   Surélever le robot afin d’éviter un départ inopiné dans un obstacle
    
-   Se déplacer vers le dossier du code : 

```bash
cd catkin_ws/src/rov_r/scripts
```

-   Entrer la commande suivante :  
```bash
python teleop_twist_keyboard.py
```
	
-   Si la commande ne s’exécute pas, donnez lui les droits d’exécution en entrant la commande : 
```bash
chmod 777 teleop_twist_keyboard
```

  
  

## 6. Téléopération au clavier
    

  

-   Ouvrir un terminal
    
-   Entrer la commande : 
```bash
rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/robot/cmd_vel
```

  
  

## 7. Capture d’images
    

  

-   Ouvrir un terminal
    
-   Installer la librairie Python OpenCV, entrer la commande : 
```bash
sudo apt-get install python3-opencv
``` 

  

Documentation pour plus d’informations sur opencv [click ici](https://docs.opencv.org/4.x/d2/de6/tutorial_py_setup_in_ubuntu.html#:~:text=OpenCV-Python%20can%20be%20installed%20in%20Ubuntu%20in%20two,source.%20In%20this%20section%2C%20we%20will%20see%20both)

  

Avant d’exécuter un programme Python3 utilisant la librairie OpenCV, vous devrez dans chaque terminal que vous allez ouvrir entrer la commande : 
```bash
export OPENBLAS_CORETYPE=ARMV8 
```

Vous pouvez aussi entrer les commandes qui suivent qui vont écrire la commande précédente dans le fichier .bashrc ce qui entrera automatiquement la commande précédente à chaque nouvelle ouverture d’un terminal. Vous gagnerez ainsi du temps. Les commandes à entrer sont :
```bash
echo "epxort OPENBLAS CORETYPE=ARMV8 " >> ~/.bashrc 

source ~/.bashrc
``` 
    
-    Pour capturer des images, entrer la commande : 
```bash
roslaunch rov_r usb_cam-test.launch
```

  
  

## 8. Détection de lignes
    

  
  

Préparation des fonctions de détection utilisant la transformée linéaire de Hough. Pour détecter la route, il nous faut des lignes d’un certain angle, on cherche à éliminer les lignes parasites qui peuvent venir perturber l’exécution du suivi de ligne. Les lignes sont détectées grâce à 4 coordonnées, nous les convertissons ensuite en vecteurs pour en avoir l'amplitude et l’angle.

  

Des codes python ont été écrits afin que la caméra puisse détecter des lignes et indiquer si elles sont détectées à gauche ou à droite. 

  

### Explication de code :

  

Dans le package rov_r dans le dossier scripts, vous trouverez ces 2 codes python : 

  

1.  houghDetection.py :
    

Dans ce code, on trouve la partie de traitement de l’image dans laquelle l’image passe par des fonctions comme canny pour extraire les contours , HoughLinesP pour ne détecter que les lignes. Ensuite, on traite les informations qu’on a obtenues à une seule condition, qu'il existe des lignes dans l’image. On extrait l’angle de chaque ligne et en fonction de cet angle on élimine toutes les autres lignes qui ne sont pas concernées et on affiche les lignes concernées (filtrage). 

De plus, on déduit le nombre de lignes à gauche et à droite de la caméra (avec un affichage de texte gauche ou droite sur l'écran) et en fonction de ce nombre, on donne l’ordre d’aller vers la gauche ou la droite. Cette fonction envoie cet ordre comme sortie.

  

2.  suivi_lignes.py : 
    

Ce code a pour but de gérer les différentes fonctions. Jusqu'à maintenant il appelle le premier code dans une boucle pour extraire les information en temps réel et gérer le lancement et l'arrêt du programme. 

  

pour lancer ce code, tapez (après avoir fait les étapes d’avant) :

```bash
rosrun rov_r suivi_lignes.py
```
