
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

- [Installation](#installation)
    - [Windows](#Windows)
    - [Linux](#Linux)
    - [Mac](#Mac)
- [How to run](#How-to-run)
    
- [Page setup](#page-setup)
    - [Upload the page tree file](#upload-the-page-tree-file)
    - [Go to the import view](#go-to-the-import-view)
    - [Import the page tree](#import-the-page-tree)
    - [SEO-friendly URLs](#seo-friendly-urls)
- [License](#license)
- [Links](#links)

## Installation

This document is for the Speech 4 Gaming beta test  

### Windows

Download the [python](https://www.python.org/downloads/windows/) lastest version , nowadays is 3.9.5. On the python website, click on the latest version button as show the image below.

<img src="https://drive.google.com/uc?export=view&id=1RK1VWZ2X8f5y0jPsmbduLkvHX8CiKKqP" alt="Download Python on Windows" title="Download Python on Windows" align="center"  />

On the execution file, click on button add python <version> to path as you can see on this next image
    

<img src="https://drive.google.com/uc?export=view&id=1mqDiaYM5B7jW8ooyjuDkvhsAVoGzdzRu" alt="Select Python to paht option" title="Select Python to paht option" align="center" />
    

After that, open the windows terminal terminal and use this code below to download the virtualenv package  
    
   
<img src="https://drive.google.com/uc?export=view&id=1S-6H2UWTARSjXJqCaSDEi7rKyT9ZHi3U " alt="Download Python on Windows" title="Download Python on Windows" align="center" />
    

    python pip install virtualenv
    

If you having trouble on the installation, please go to the virtualenv [website](https://virtualenv.pypa.io/en/latest/installation.html).

Then, choose the directory that you want to put the Speech 4 Gaming Project and open it on the terminal to clone the project with this code below 
    
    
    git clone https://github.com/Lucas-Nardi/Speech-4-Gaming.git Speech_4_Gaming       
    
    
 After the download, go to the directory created with the code below  
 
    cd Speech_4_Gaming
    
 then, use this next code to create a virtual enviroment  
    
    virtualenv env

The next step is to activate the virtual enviroment created, to do this use this code below.

    env\Scripts\activate.bat

Now, you will se the name (env) before the path name on terminal line.

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
    

Finally, we will install the last package named pyAudio, to do that use this 2 codes
    
    pip install pipwin
    
    pipwin install pyaudio
    
### Mac Os


### How to run

If you are on the directory named Speech_4_Gaming just use this code below
    
    `python Speech_4_Gaming.py`

## License

The Aimeos TYPO3 extension is licensed under the terms of the GPL Open Source
license and is available for free.

## Links

* [Web site](https://aimeos.org/integrations/typo3-shop-extension/)
* [Documentation](https://aimeos.org/docs/TYPO3)
* [Forum](https://aimeos.org/help/typo3-extension-f16/)
* [Issue tracker](https://github.com/aimeos/aimeos-typo3/issues)
* [Source code](https://github.com/aimeos/aimeos-typo3)

## License
[MIT](https://choosealicense.com/licenses/mit/)
