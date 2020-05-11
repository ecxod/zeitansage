#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Diese Datei ist Teil von "zeitansage". Autor Chr. Eichert 2020
# https://github.com/ecxod/zeitansage
#
# Dieses Programm ist Freie Software: Sie können es unter den Bedingungen
# der GNU General Public License, wie von der Free Software Foundation,
# Version 3 der Lizenz oder (nach Ihrer Wahl) jeder neueren
# veröffentlichten Version, weiter verteilen und/oder modifizieren.
#
# Dieses Programm wird in der Hoffnung bereitgestellt, dass es nützlich 
# sein wird, jedoch OHNE JEDE GEWÄHR,; sogar ohne die implizite
# Gewähr der MARKTFÄHIGKEIT oder EIGNUNG FÜR EINEN BESTIMMTEN ZWECK.
# Siehe die GNU General Public License für weitere Einzelheiten.
#
# Sie sollten eine Kopie der GNU General Public License zusammen mit diesem
# Programm erhalten haben. Wenn nicht, siehe <https://www.gnu.org/licenses/>.
#
# espeak - espeak/espeak-ng https://packages.debian.org/buster/espeak-ng-espeak
# german-mbrola-3 - apt im non-free repository. http://tcts.fpms.ac.be/synthesis/
# aplay - als teil von alsa-utils 
# 
# feedparser - pip/pip3 install feedparser
#
# glocke-anschlagen-einmal.ogg - stammt ursprünglich Sebastian Karpp von 
# https://www.salamisound.de/7958026-glocke-anschlagen-einmal und wurde mit dir2ogg 
# in das freie format ogg umgewandelt. Die Datei Für den privaten / persönlichen / 
# künstlerischen / pädagogischen Gebrauch ist es gestattet die mp3 Dateien zu 
# kopieren und weiter zu verarbeiten. Alle Rechte dem Autor.

import os
import re
import datetime
import feedparser

hr = datetime.datetime.now().hour;
mn = datetime.datetime.now().minute;

gong = 'play -q -V1 "/media/effekte/glocke-anschlagen-einmal.ogg"';
cmd = 'espeak -a100 -s120 -p65 -vgerman-mbrola-3+croak+whisper "ACHTUNG! Es ist {0} Uhr und {1} Minuten" --stdout | aplay -q'.format(hr, mn);
fix = 'espeak -a100 -s120 -p65 -vgerman-mbrola-3+croak+whisper "ACHTUNG, ACHTUNG! Es ist genau {0} Uhr." --stdout | aplay -q'.format(hr);

if mn == "00":
  rss = feedparser.parse("https://www.nzz.ch/recent.rss");
elif mn == "10":
  rss = feedparser.parse("https://www.achgut.com/rss2");
elif mn == "20":
  rss = feedparser.parse("https://www.compact-online.de/feed/");
elif mn == "30":
  rss = feedparser.parse("https://www.journalistenwatch.com/feed/");
elif mn == "40":
  rss = feedparser.parse("https://feeds.feedburner.com/politikversagen");
else:
  rss = feedparser.parse("https://www.tichyseinblick.de/rss");


anz = len(rss.entries);
i=1;
if anz>3:
  anz=3;

if mn == "00":
    os.system(gong);
    os.system(gong);
    os.system(fix);
    while i < anz:
      entry = rss.entries[i]
      try:
        ti = re.sub('<[^<]+?>', '', entry.title);
        #print("TITLE "+entry.title);
        news = 'espeak -a100 -s120 -p65 -vgerman-mbrola-3+croak+whisper "{0}" --stdout | aplay -q'.format(ti);
        os.system(news);
      except Exception:
        pass;

      try:
        su = re.sub('<[^<]+?>', '', entry.summary);
        #print("SUMMARY "+su);
        news = 'espeak -a100 -s120 -p65 -vgerman-mbrola-3+croak+whisper "{0}" --stdout | aplay -q'.format(su);
        os.system(news);
      except Exception:
        pass;
      i += 1;
else:
    os.system(gong);
    os.system(cmd);
    while i < anz:
      entry = rss.entries[i]
      try:
        ti = re.sub('<[^<]+?>', '', entry.title);
        #print("TITLE "+entry.title);
        news = 'espeak -a100 -s120 -p65 -vgerman-mbrola-3+croak+whisper "{0}" --stdout | aplay -q'.format(ti);
        os.system(news);
      except Exception:
        pass;

      try:
        su = re.sub('<[^<]+?>', '', entry.summary);
        #print("SUMMARY "+su);
        news = 'espeak -a100 -s120 -p65 -vgerman-mbrola-3+croak+whisper "{0}" --stdout | aplay -q'.format(su);
        os.system(news);
      except Exception:
        pass;
      i += 1;
