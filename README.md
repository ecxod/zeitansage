# zeitansage
It is a python script that is inspired from saytime, and improoved with a feedreader

This package was first written on a debian machine but it sure can run on any other linux machine.
You wil need a soundcard and a loudspeaker connected to your computer

personally I use the alsa driver that come in a package called alsa-utils
the package aplay comes with alsa-utils.

*apt install alsa-utils*

There are some dependencies you must install.

first of all you need to install feedparser from pip/pip3 or from somewhere else.

*pip install feedparser*
(if you do not have pip install it "apt install python3-pip")

after this you need espeak from https://packages.debian.org/buster/espeak-ng-espeak or from somewhere else

*apt install espeak*
or (better) 
*apt install espeak-ng*

I use a german female voice from the mbrola package "german-mbrola-3" you can find it in the non-free repository on debian https://packages.debian.org/de/buster/mbrola-voice or on his homepage http://tcts.fpms.ac.be/synthesis/

*apt install mbrola-voice mbrola-de3*

of course you can also use another language or even another synthesis. Please read the man page and configure to fit your taste
