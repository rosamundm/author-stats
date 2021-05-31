## Einführung

Dieses Praxisprojekt repräsentiert meine Absolvierung eines Kurses in Vorbereitung auf die [PCAP-Prüfung](https://pythoninstitute.org/certification/pcap-certification-associate/). Der zweimonatige Teilzeitkurs wurde durch [BBQ Berlin](https://www.bbq.de/standorte/berlin/) mit der Absicht von Präsenzunterrichten angeboten, die jedoch aufgrund des COVID-19 unmöglich wurden. So hat die Klasse (bestehend aus ca. 6 Personen) endgültig komplett an Fernunterrichten teilgenommen.

Mein Projekt heißt *authorCount*. Es handelt sich um eine Web-Anwendung, bei der Benutzer_innen, die an einem längeren schriftlichen Werk arbeiten (z.B. einem Roman, einer These), eine gezielte Wortanzahl setzen. Jeden Tag kann der_die Benutzer_in die bisherige Wortanzahl eingeben und Auskunft bekommen, wie viele Wörter noch bleiben, bis das Ziel erreicht wird.

Ich habe *authorCount* selber auf meine eigenen Bedürfnisse als Schriftstellerin konzipiert und auf [Django](https://www.djangoproject.com/) gebaut. Zum Frontend-Design habe ich [Bootstrap 4](getbootstrap.com) als Hilfsframework genommen.

## Die Anwendung
Man kann sich über die Startseite ein Konto anlegen oder wieder einloggen. \
![homepage](/screenshots/pic1.png)
![sign-up form](/screenshots/pic2.png)
![sign-up form 2](/screenshots/pic3.png)
![sign-in form](/screenshots/pic4.png)

Einmal eingeloggt landet man auf eine Seite, die die bisherigen Bücher darstellt. Hier kann man auch ein neues Buch anlegen. \
![book list](/screenshots/pic5.png)
![new book](/screenshots/pic6.png)
![new book 2](/screenshots/pic7.png)

Beim Klicken auf einen Buchtitel wird man zu einer Detail-Seite weitergeleitet: \
![book detail](/screenshots/pic8.png)

Hier kommen die Python-Funktionen ins Spiel.
Anpassen: \
![update book](/screenshots/pic9.png)

Löschen: \
![delete book](/screenshots/pic10.png)

Statistiken: \
![book stats](/screenshots/pic11.png)

Kurze Vorstellung: \
![about](/screenshots/pic12.png)

Responsive Navbar bei mittelgroßen bzw. schmalen Bildschirmen: \
![toggle](/screenshots/pic13.png)
![toggle2](/screenshots/pic14.png)
