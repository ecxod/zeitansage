# zeitansage
Es ist ein Python-Skript, das von saytime inspiriert und mit einem Feedreader verbessert wurde

Dieses Paket wurde zuerst auf einem Debian-Computer geschrieben, kann aber sicher auf jedem anderen Linux-Computer ausgeführt werden.
Sie benötigen eine Soundkarte und einen Lautsprecher, die an Ihren Computer angeschlossen sind

Ich persönlich benutze den alsa-Treiber, der in einem Paket namens alsa-utils enthalten ist
das paket aplay wird mit alsa-utils geliefert.

*apt install alsa-utils*

Es gibt einige Abhängigkeiten, die Sie installieren müssen.

Zunächst müssen Sie feedparser von pip / pip3 oder von einem anderen Ort installieren.

*pip install feedparser*

Danach benötigen Sie einen Espeak von https://packages.debian.org/buster/espeak-ng-espeak oder von einem anderen Ort

*apt install espeak*
oder
*apt install espeak-ng*

Ich benutze eine deutsche Frauenstimme aus dem mbrola-Paket "german-mbrola-3". Sie finden es im non-free Repository unter Debian https://packages.debian.org/de/buster/mbrola-voice oder auf seiner Homepage http://tcts.fpms.ac.be/synthesis/

*apt install mbrola-voice mbrola-de3*

Natürlich können Sie auch eine andere Sprache oder sogar eine andere Synthese verwenden. Bitte lesen Sie die Manpage und konfigurieren Sie sie nach Ihrem Geschmack

Die Datei glocke-anschlagen-einmal.ogg - laden wir nach /media/effekte/ herunter, sie stammt ursprünglich Sebastian Karpp von https://www.salamisound.de/7958026-glocke-anschlagen-einmal und wurde mit dir2ogg in das freie format ogg umgewandelt. Die Datei Für den privaten / persönlichen / künstlerischen / pädagogischen Gebrauch ist es gestattet die mp3 Dateien zu kopieren und weiter zu verarbeiten. Alle Rechte dem Autor.

*apt install dir2ogg*

*dir2ogg /media/effekte/*

laden Sie jetzt zeitansage.py herunter und verschieben sie sie nach /sbin und geben ihr ausführbare rechte

*wget https://raw.githubusercontent.com/ecxod/zeitansage/master/zeitansage.py*
c*p zeitansage.py /sbin/zeitansage.py*
*cd /sbin*
*chmod a+x /sbin/zeitansage.py*

kopieren sie nun die Vorlage crontab -e in einen neuen crontab. Falls Sie die Datei zeitansage.py anderswohin als /sbin geladen haben, bitte anzupassen in der crontab -e
