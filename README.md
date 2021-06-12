
Speech 4 Gaming é um software que utiliza a tecnologia ASR para combater a falta de acessibilidade nos jogos na atualidade. 
Este software utiliza a tecnologia Vosk API para reconhecer os comandos de vozes dos usuários e com o resultado dado pelo Vosk API, simular uma das 
22 chave (q,w,e,r,a,s,d,f,g,z,x,c,v,ctrl,space,shift,tab,1,2,3,4 e 5). Assim, com este software, as pessoas com deficiência física podem jogar alguns jogos de vídeo para computador.


## Speech 4 Gaming

:star: Star me on GitHub — it motivates me a lot!

Speech 4 Gaming is a software that use the ASR tecnologic to combat the lack of accessibility in games nowadays. 
This software uses the Vosk API to recognition the users'commands voices and with the result gave by Vosk API, simulate one of 
22 key (q,w,e,r,a,s,d,f,g,z,x,c,v,ctrl,space,shift,tab,1,2,3,4 and 5). So with this software, the people who has physical impaired can play some computer video games.

### Speech 4 Gaming Menu Screen


## Table of content

- [How to Install and Run](#how-to-install-and-run)
    - [Windows](#Windows)
    - [Linux](#Linux)   
    - [Run and Stop](#run-and-stop)
    

## How to Install and Run

This document is for the Speech 4 Gaming beta test  

### Windows

If you wanna have fun and training some terminal code continue the guide, but if you want to use the faster way use this link below.

[Speech 4 Gaming Installer](https://mega.nz/file/AzJAkRAK#HWxT_yBcHfYzucbj0qZO6p13m2baFWJnX3W-NRoVw8c)     :point_left:

Since you choose this way, let's start to code  :mechanical_arm: :keyboard: :heart_eyes::heart_eyes:

Download the [python](https://www.python.org/downloads/windows/) lastest version , nowadays is 3.9.5. On the python website, click on the latest version button as show the image below :point_down:.

<img src="https://drive.google.com/uc?export=view&id=1RK1VWZ2X8f5y0jPsmbduLkvHX8CiKKqP" alt="Download Python on Windows" title="Download Python on Windows" align="center"  />

On the execution file, click on button add python <version> to path as you can see on this next image
    
<br/>

<img src="https://drive.google.com/uc?export=view&id=1mqDiaYM5B7jW8ooyjuDkvhsAVoGzdzRu" alt="Select Python to paht option" title="Select Python to paht option" align="center" />
    
<br/>
    
After that, open the windows terminal terminal and use this next code to download the virtualenv package  
    
   
<img src="https://drive.google.com/uc?export=view&id=1S-6H2UWTARSjXJqCaSDEi7rKyT9ZHi3U " alt="Download Python on Windows" title="Download Python on Windows" align="center" />
    

    python pip install virtualenv
    

If you having trouble on the installation :pray:, please go to the virtualenv [website](https://virtualenv.pypa.io/en/latest/installation.html).

Then, choose the directory that you want to put the Speech 4 Gaming Project and open it on the terminal to clone the project with this code below 
    
    
    git clone https://github.com/Lucas-Nardi/Speech-4-Gaming.git Speech_4_Gaming       
    
    
 After the download, go to the directory created with the code below  
 
    cd Speech_4_Gaming
    
 then, use this next code to create a virtual enviroment  
    
    virtualenv env

The next step is to activate the virtual enviroment created, to do this use this code below.

    env\Scripts\activate.bat

Now, you will see the name (env) before your pc name on terminal line.

Finally, we will install all dependencies that the Speech 4 Gaming uses with this code:
    

    pip install -r requirements.txt (Python 2)

or

    pip3 install -r requirements.txt (Python 3)

       
Afther this command, you will need to see which python version do you have, to do that use this code
    
    python --version
    
Knowing which python version do you have on your pc, use the next code to donwload the last necessary package named pyAudio. 
    
**Note1:** If your python vesion is not one of this (3.9, 3.8, 3.7, 3.6, 3.5,3.4 or 2.7), please download one of then on the [website](https://www.python.org/downloads/windows/).
    
**Note2:** If your python version is above 3.9, visit this [website](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) to download the last package named pyAudio. On this website choose the file acording to your python version and the windows SO system(64bits, 32 bits).
    
    pip install pyAudio_file/PyAudio-0.2.11-cp<Python version>-cp<Python version>-win_amd<SO System>.whl
 
Example:
    
if your python version is 3.9 use this code
    
     pip install pyAudio_file/PyAudio-0.2.11-cp39-cp39-win_amd64.whl for windows 64(bits) 
    
    or
    
     pip install pyAudio_file/PyAudio‑0.2.11‑cp39‑cp39‑win32.whl  for windows ( 32bits) 
    
if your python version is 3.8 use this code
    
    pip install pyAudio_file/PyAudio-0.2.11-cp38-cp38-win_amd64.whl for windows 64(bits)
    
    or
    
     pip install pyAudio_file/PyAudio‑0.2.11‑cp38‑cp38‑win32.whl  for windows( 32bits)     
 
    
    
### Linux
    
First we need to install python, to do that use this 3 codes below.
    
    sudo apt-get update
    
    sudo apt -y upgrade
    
    sudo apt install -y python3-pip
    
Next, we need to create a virtual enviroment, to do that we will install the python package named virtualenv
    
    sudo apt install -y python3-venv
    
Then, we will clone the Speech 4 Gaming project with this code below
    
    git clone https://github.com/Lucas-Nardi/Speech-4-Gaming.git Speech_4_Gaming 
 
 After the Speech 4 Gaming Cloning, enteder to the project directory we this next code
    
    cd Speech_4_Gaming
 
 Now, we will create the virtual enviroment and activate it using this 2 codes
    
    python3 -m venv env
    
    source env/bin/activate

To see with the virtual enviroment is activate, just look at you terminal line and see if the name env appears before your pc name, like this example below

    (env)lucas@ubunto:~/Speech_4_Gaming$
    
The next step is to install all the dependencies that the Speech 4 Gaming uses with this code:

    pip install -r requirements.txt (Python 2)

or

    pip3 install -r requirements.txt (Python 3)
    

Finally, we will install the last package named pyAudio, to do that use this the first code, if wont work, use the last 2 codes
    
    pip3 install PyAudio
    
    pip install pipwin
    
    pipwin install pyaudio 
    

**Note1:** We need to install this libxc to prevent error
    
    sudo apt-get install libxcb-randr0-dev libxcb-xtest0-dev libxcb-xinerama0-dev libxcb-shape0-dev libxcb-xkb-dev

   
### Run and Stop
    
To run the Speech 4 Gaming in all 3 SO System use this code below    
      
   python Speech 4 Gaming.py
 
To stop the Speech 4 Gaming just click on the exit button like the image below
    
 <img src="https://drive.google.com/uc?export=view&id=140zOJpwPP2ZztS3I57eKocPQb-n3qI88" alt="Download Python on Windows" title="Download Python on Windows" align="center" />
    
To deactivate the virtual enviroment just use the next code
    
    deactivate
    
**Important!** If you deactivate the virtual enviroment , you will need to active it to run the Speech 4 Gaming again
 
***Note1** Code to activate the virtual enviroment on Linux and Mac OS X
    
    source env/bin/activate
    
    
 **Note2:** Code to activate the virtual enviroment on Windows
    
 
    env\Scripts\activate.bat
    
    
