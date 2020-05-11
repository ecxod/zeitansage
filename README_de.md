# zeitansage
Es ist ein Python-Skript, das von saytime inspiriert und mit einem Feedreader verbessert wurde

Dieses Paket wurde zuerst auf einem Debian-Computer geschrieben, kann aber sicher auf jedem anderen Linux-Computer ausgeführt werden.
Sie benötigen eine Soundkarte und einen Lautsprecher, die an Ihren Computer angeschlossen sind

Ich persönlich benutze den alsa-Treiber, der in einem Paket namens alsa-utils enthalten ist
das paket aplay wird mit alsa-utils geliefert.

* apt install alsa-utils *

Es gibt einige Abhängigkeiten, die Sie installieren müssen.

Zunächst müssen Sie feedparser von pip / pip3 oder von einem anderen Ort installieren.

* pip install feedparser *

Danach benötigen Sie einen Espeak von https://packages.debian.org/buster/espeak-ng-espeak oder von einem anderen Ort

* apt install espeak *
oder
* apt install espeak-ng *

Ich benutze eine deutsche Frauenstimme aus dem mbrola-Paket "german-mbrola-3". Sie finden es im non-free Repository unter Debian https://packages.debian.org/de/buster/mbrola-voice oder auf seiner Homepage http://tcts.fpms.ac.be/synthesis/

* apt install mbrola-voice mbrola-de3 *

Natürlich können Sie auch eine andere Sprache oder sogar eine andere Synthese verwenden. Bitte lesen Sie die Manpage und konfigurieren Sie sie nach Ihrem Geschmack
