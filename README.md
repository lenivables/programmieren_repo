# Entwicklung einer Spotify-App
Im Rahmen dieser Portfolio-Prüfung wurde eine Spotify-App entwickelt, die als einfache Musikverwaltungssoftware dient. Sie ermöglicht dem Benutzer, Songs hinzuzufügen, zu löschen, zu durchsuchen, zu sortieren und seine Favoriten zu verwalten. Die Implementierung erfolgt in Python und nutzt verschiedene Algorithmen für die Suche und Sortierung von Songs. Ziel ist es, die Performance dieser unterschiedlichen Algorithmen zu vergleichen und deren Effizienz in der Anwendung zu analysieren.
## Funktionen der App
### 1. Add Song
#### Beschreibung:
Mit dieser Funktion kann der Benutzer einen neuen Song zur Bibliothek hinzufügen. Ein Song besteht aus drei Hauptkomponenten:
- Titel: Der Name des Songs.
- Künstler: Der Name des Musikers oder der Band.
- Album: Der Name des Albums, in dem der Song veröffentlicht wurde.
#### Funktionsweise:
Der Benutzer wird aufgefordert, die Details des Songs einzugeben (Titel, Künstler, Album). Danach wird ein neues Song-Objekt erstellt, das die Informationen speichert. Dieses Objekt wird in einer Liste oder einem Datenstruktur wie einem Red-Black-Baum (zur effizienten Verwaltung) gespeichert.
Das Hinzufügen von Songs ist der Kern der Musikverwaltung. Ohne diese Funktion wäre die Erstellung und Erweiterung einer Musikbibliothek nicht möglich.
### 2. Delete Song
#### Beschreibung: 
Diese Funktion ermöglicht es dem Benutzer, einen bestimmten Song aus der Bibliothek zu entfernen. Dazu muss der Benutzer den Titel des Songs angeben, der gelöscht werden soll.

#### Funktionsweise: 
Die Funktion sucht den Song basierend auf dem eingegebenen Titel. Wenn der Song in der Bibliothek gefunden wird, wird er aus der Liste entfernt. Dies kann durch eine lineare oder eine binäre Suche geschehen (abhängig davon, ob die Liste sortiert ist). Anschließend wird das entsprechende Objekt aus der Datenstruktur gelöscht.
### 3. Display Song
#### Beschreibung: 
Diese Funktion zeigt alle in der Bibliothek gespeicherten Songs in einer geordneten oder ungeordneten Liste an. Der Benutzer erhält eine Übersicht über die gespeicherten Titel, Künstler und Alben.

#### Funktionsweise: 
Die Funktion durchläuft die Liste aller Songs und gibt für jedes Song-Objekt dessen Details (Titel, Künstler und Album) aus. Falls die Songs sortiert sind, können sie in einer alphabetischen Reihenfolge angezeigt werden.
Zweck: Die Anzeige von Songs ist wichtig, um dem Benutzer einen Überblick über die vorhandenen Titel zu geben. Diese Funktion ermöglicht es, den aktuellen Status der Musikbibliothek zu sehen.

### 4. Search Song
#### Beschreibung:
Mit dieser Funktion kann der Benutzer nach einem bestimmten Song in der Bibliothek suchen. Dies erfolgt über die Eingabe des Songtitels, und der Benutzer erhält Informationen darüber, ob der Song in der Bibliothek vorhanden ist oder nicht.

#### Funktionsweise: 
Es gibt zwei mögliche Methoden der Suche:

1. Lineare Suche: Jedes Element der Liste wird durchgegangen, bis der gesuchte Song gefunden wird.
2. Binäre Suche: Wenn die Liste sortiert ist, wird die binäre Suche verwendet, um die Suchzeit zu optimieren.
python
### 5. Sort Song
#### Beschreibung: 
Diese Funktion sortiert die Songs in der Bibliothek basierend auf dem Titel (oder einem anderen Kriterium, falls angepasst). Der Benutzer kann aus verschiedenen Sortieralgorithmen wählen, wie z. B. Bubble Sort, Insertion Sort, Merge Sort oder Quick Sort.

#### Funktionsweise: 
Der Benutzer kann auswählen, welcher Algorithmus zur Sortierung verwendet werden soll. Abhängig vom gewählten Algorithmus wird die Liste der Songs neu angeordnet. Dabei werden die Songs alphabetisch nach dem Titel geordnet.
### 6. Exit
#### Beschreibung: 
Diese Funktion beendet die Anwendung und speichert gegebenenfalls den aktuellen Zustand der Songliste, damit bei der nächsten Nutzung darauf zugegriffen werden kann.

#### Funktionsweise: 
Die Anwendung wird ordnungsgemäß geschlossen, und falls gewünscht, wird der aktuelle Zustand der Songs (z. B. in einer Datei oder Datenbank) gespeichert, damit diese beim nächsten Start wieder geladen werden können.
### 7. Create Random Songs
#### Beschreibung: 
Diese Funktion erstellt eine vorgegebene Anzahl von zufälligen Songs und fügt sie der Bibliothek hinzu. Dies ist nützlich, um die App mit einer großen Anzahl von Songs zu testen und die Leistungsfähigkeit der Sortier- und Suchalgorithmen zu evaluieren.

#### Funktionsweise: 
Es werden zufällige Strings für Titel, Künstler und Album generiert. Diese werden als neue Song-Objekte der Bibliothek hinzugefügt. Die Anzahl der zu erstellenden Songs wird vom Benutzer bestimmt.
#### Zweck:
Diese Funktion simuliert reale Szenarien mit einer großen Anzahl von Songs und erlaubt es dem Benutzer, die App unter verschiedenen Belastungen zu testen.


### 8. Add song to your favourites
#### Beschreibung: 
Ein Benutzer kann einen Song aus der Hauptbibliothek zu einer speziellen Favoritenliste hinzufügen. Diese Liste enthält die Songs, die der Benutzer besonders mag und schnell darauf zugreifen möchte.

#### Funktionsweise: 
Der Benutzer wählt einen Song aus der Hauptbibliothek aus, und dieser wird der Favoritenliste hinzugefügt. Die Favoritenliste ist unabhängig von der Hauptbibliothek, aber sie enthält Verweise auf die gleichen Song-Objekte.

### 9. Delete song from your favourites
#### Beschreibung: 
Diese Funktion entfernt einen Song aus der Favoritenliste, wenn der Benutzer diesen nicht mehr als Favorit markieren möchte.

#### Funktionsweise: 
Der Benutzer wählt den Song, der aus den Favoriten entfernt werden soll. Dieser wird dann aus der Favoritenliste gelöscht, bleibt aber in der Hauptbibliothek erhalten.
Zweck: Das Entfernen von Songs aus den Favoriten hilft dabei, die Favoritenliste auf dem neuesten Stand zu halten und nur relevante Songs dort zu speichern.


### 10. Show favourites 
#### Beschreibung: 
Diese Funktion zeigt alle Songs an, die der Benutzer zu seinen Favoriten hinzugefügt hat. Es handelt sich hierbei um eine separate Liste von der Hauptbibliothek.

#### Funktionsweise: 
Die Favoritenliste wird durchlaufen, und die Informationen über jeden Song (Titel, Künstler, Album) werden angezeigt. Diese Liste ist meist kürzer als die Hauptliste und ermöglicht einen schnellen Überblick über bevorzugte Songs.
#### Zweck: 
Die Anzeige der Favoritenliste erleichtert dem Benutzer den schnellen Zugriff auf seine bevorzugten Songs.

## eingefügte Algorithmen
In der Spotify-App gibt es zwei Hauptmethoden, um nach einem bestimmten Song zu suchen: die Lineare Suche und die Binäre Suche. Beide Algorithmen unterscheiden sich grundlegend in ihrer Funktionsweise und Effizienz, abhängig davon, ob die Liste der Songs bereits sortiert ist oder nicht.


## Suchalgorithmen
### Lineare Suche
Die lineare Suche ist ein einfacher, aber grundlegender Suchalgorithmus, der in unsortierten Listen eingesetzt wird. Sie funktioniert, indem sie die Liste von Anfang bis Ende durchläuft und jedes Element einzeln überprüft. Der Algorithmus beginnt immer beim ersten Element und vergleicht es mit dem gesuchten Wert, in diesem Fall einem Songtitel. Wenn das Element nicht dem gesuchten Song entspricht, wird zum nächsten Element übergegangen und der Vergleich wiederholt. Dieser Prozess setzt sich so lange fort, bis entweder der gesuchte Song gefunden oder das Ende der Liste erreicht wurde.

Der Hauptvorteil der linearen Suche liegt darin, dass sie auf jede Liste angewendet werden kann, da keine Sortierung der Daten erforderlich ist. Dies macht sie besonders nützlich für kleine oder unsortierte Datenmengen, wo die Suche vergleichsweise schnell abgeschlossen ist. Die einfache Implementierung und die Flexibilität machen sie zu einem universell einsetzbaren Ansatz. Allerdings stößt die lineare Suche bei großen Listen schnell an ihre Grenzen. Da jedes Element einzeln geprüft wird, steigt die Anzahl der erforderlichen Vergleiche linear mit der Größe der Liste an, was im schlimmsten Fall bedeutet, dass alle Elemente der Liste durchsucht werden müssen.

Angenommen, ein Benutzer sucht in einer unsortierten Liste von 100 Songs nach dem Titel „Imagine“. Die lineare Suche beginnt beim ersten Song und arbeitet sich schrittweise durch die Liste, bis „Imagine“ gefunden wird oder alle Songs ohne Erfolg überprüft wurden. Dieser Suchansatz ist besonders praktisch in Fällen, in denen die Datenstruktur chaotisch ist oder wenn die Liste überschaubar bleibt.



## Binäre Suche
Die binäre Suche ist ein deutlich effizienterer Suchalgorithmus, der jedoch nur auf sortierten Listen angewendet werden kann. Im Gegensatz zur linearen Suche, die jedes Element überprüft, halbiert die binäre Suche den Suchbereich bei jedem Schritt, indem sie das mittlere Element der Liste auswählt und mit dem gesuchten Wert vergleicht. Dieser Algorithmus basiert auf dem „Teile-und-herrsche“-Prinzip, wodurch große Teile der Liste sofort ausgeschlossen werden können. Wenn der gesuchte Songtitel alphabetisch vor dem mittleren Element liegt, wird nur die linke Hälfte der Liste weiter durchsucht. Andernfalls wird die rechte Hälfte der Liste betrachtet. Dieser Vorgang wird so lange wiederholt, bis entweder der gesuchte Song gefunden wird oder der Suchbereich auf null Elemente reduziert ist.

Die Stärke der binären Suche liegt in ihrer Effizienz. Da bei jedem Schritt die Hälfte der verbleibenden Elemente ausgeschlossen wird, ist die Suche selbst bei großen Listen sehr schnell. Während die lineare Suche eine Zeitkomplexität von O(n) hat, liegt die Zeitkomplexität der binären Suche bei O(log n), was sie für große Datenmengen erheblich schneller macht. Allerdings ist ein wesentlicher Nachteil, dass die Liste sortiert sein muss, was zusätzlichen Rechenaufwand erfordert, wenn die Liste vor der Suche nicht bereits in Ordnung gebracht wurde.

Nehmen wir an, die Liste der Songs ist alphabetisch sortiert, und ein Benutzer sucht nach dem Song „Imagine“. Die binäre Suche beginnt in der Mitte der Liste und vergleicht das mittlere Element mit „Imagine“. Liegt „Imagine“ alphabetisch vor diesem Element, wird die linke Hälfte der Liste weiter durchsucht. Dieser Prozess wird fortgesetzt, bis der Song gefunden ist oder keine weiteren Elemente zur Überprüfung übrig bleiben. Dank dieses strukturierten Ansatzes reduziert sich die Anzahl der benötigten Vergleiche drastisch, was die binäre Suche zu einer exzellenten Wahl für große, sortierte Datensätze macht.



### Sortieralgorithmen
#### Bubble Sort
Der Bubble Sort ist einer der einfachsten Sortieralgorithmen, der auf dem Prinzip basiert, dass größere Elemente innerhalb einer Liste nach und nach "nach oben" (oder "nach hinten") wandern, indem sie mit benachbarten Elementen vertauscht werden. Der Algorithmus durchläuft die Liste wiederholt und vergleicht jeweils zwei benachbarte Elemente. Wenn das aktuelle Element größer ist als das nächste, werden die beiden vertauscht. Dieser Vorgang wird so lange wiederholt, bis die gesamte Liste sortiert ist.

Der Prozess beginnt beim ersten Element der Liste, welches mit dem nächsten verglichen wird. Sollte das erste Element größer sein als das zweite, erfolgt ein Tausch der beiden. Dieser Vergleich wird für jedes Paar in der Liste wiederholt, bis das größte Element an den letzten Platz „gebubbelt“ ist. Mit jeder abgeschlossenen Runde erreicht ein weiteres größeres Element seine endgültige Position. Der Algorithmus stoppt, sobald keine weiteren Vertauschungen mehr notwendig sind, was bedeutet, dass die Liste vollständig sortiert ist.

Der Hauptvorteil von Bubble Sort ist seine einfache Implementierung und die leicht verständliche Logik, die ihn zu einem guten Lernbeispiel für grundlegende Sortieralgorithmen macht. Nachteilig ist jedoch seine Ineffizienz bei großen Datensätzen, da er viele Vergleiche und Vertauschungen durchführt. Dies führt zu einer hohen Laufzeit, insbesondere bei bereits fast sortierten oder sehr großen Listen, wodurch er im Vergleich zu anderen Sortierverfahren deutlich langsamer ist.

### Insertion Sort
Der Insertion Sort funktioniert ähnlich wie das Sortieren von Spielkarten in der Hand. Dabei wird die Liste in einen sortierten und einen unsortierten Teil aufgeteilt. Der Algorithmus nimmt jeweils ein Element aus dem unsortierten Teil der Liste und fügt es an der passenden Stelle im bereits sortierten Teil ein. Dies wird so lange wiederholt, bis die gesamte Liste sortiert ist.

Zu Beginn wird mit dem zweiten Element der Liste gestartet, das mit dem ersten verglichen wird. Ist das zweite Element kleiner als das erste, wird es an die richtige Position verschoben. Danach wird das dritte Element genommen und ebenfalls mit den vorherigen verglichen, um es an der passenden Stelle im sortierten Abschnitt einzufügen. Dieser Vorgang wird fortgeführt, bis jedes Element an seinem richtigen Platz ist und die Liste vollständig sortiert ist.

Ein großer Vorteil des Insertion Sort ist, dass er gut für kleine oder bereits teilweise sortierte Listen geeignet ist. Zudem ist der Algorithmus relativ einfach zu verstehen und zu implementieren. Ein Nachteil liegt jedoch in seiner Ineffizienz bei sehr großen, unsortierten Listen, da die Anzahl der benötigten Vergleiche und Verschiebungen mit der Größe der Liste zunimmt.

### Merge Sort
Der Merge Sort basiert auf dem „Teile-und-herrsche“-Prinzip, bei dem eine Liste in immer kleinere Teilmengen zerlegt wird, bis jede Teilmenge nur noch ein einziges Element enthält. Anschließend werden diese Teilmengen so zusammengeführt, dass die resultierende Liste sortiert ist. Der Algorithmus arbeitet rekursiv und bietet eine systematische sowie effiziente Methode zur Sortierung.

Die Funktionsweise beginnt damit, dass die Liste in der Mitte geteilt wird, sodass zwei Teillisten entstehen. Jede dieser Teillisten wird wiederum rekursiv weiter in kleinere Teillisten unterteilt, bis nur noch einzelne Elemente übrig bleiben. Sobald dies erreicht ist, beginnt der eigentliche Sortiervorgang, bei dem die kleinsten Teilmengen in aufsteigender Reihenfolge wieder zusammengeführt werden. Dabei werden die Elemente der Teillisten miteinander verglichen und in sortierter Reihenfolge in eine neue Liste eingefügt. Dieser Vorgang setzt sich fort, bis alle Teillisten wieder zu einer großen, vollständig sortierten Liste zusammengeführt wurden.

Ein Vorteil von Merge Sort ist seine hohe Effizienz, besonders bei großen Datenmengen, da der Algorithmus die Liste in überschaubare Teile zerlegt und systematisch sortiert. Ein Nachteil ist jedoch der zusätzliche Speicherplatz, der benötigt wird, da beim Zusammenführen der Teillisten neue Listen erstellt werden müssen.

### Quick Sort
Der Quick Sort ist ein „Teile-und-herrsche“-Algorithmus, der im Gegensatz zu Merge Sort keinen zusätzlichen Speicherplatz benötigt. Er arbeitet, indem ein sogenanntes Pivot-Element ausgewählt wird, das als Bezugspunkt für die Teilung der Liste dient. Die Liste wird dann so um das Pivot-Element organisiert, dass alle kleineren Elemente links und alle größeren Elemente rechts davon platziert werden. Dieser Vorgang wird rekursiv auf die entstehenden Teillisten angewendet, bis die gesamte Liste sortiert ist.

Die Funktionsweise beginnt mit der Wahl eines Pivot-Elements, das entweder zufällig oder nach bestimmten Kriterien ausgewählt wird. Anschließend wird die Liste um dieses Pivot-Element herum angeordnet: Alle Elemente, die kleiner als das Pivot sind, werden auf die linke Seite verschoben, und alle größeren auf die rechte. Der Prozess wiederholt sich rekursiv für die beiden Teillisten, bis alle Elemente in der richtigen Reihenfolge sortiert sind. Sobald die Teillisten vollständig sortiert sind, werden sie zusammengeführt, um die ursprüngliche Liste in sortierter Form zu erhalten.

Ein großer Vorteil von Quick Sort ist seine hohe Effizienz, insbesondere bei der Sortierung großer Listen, da er in der Regel weniger Speicherplatz benötigt als andere Algorithmen wie Merge Sort. In der Praxis ist er oft schneller als andere Sortiermethoden. Ein Nachteil besteht jedoch darin, dass die Leistung im schlimmsten Fall stark abnehmen kann, insbesondere wenn das Pivot-Element schlecht gewählt ist, was zu einer ungleichmäßigen Teilung der Liste führt.

### Block Sort
Der Block Sort (auch Block Merge Sort genannt) ist ein hybrider Sortieralgorithmus, der auf dem Merge Sort basiert, jedoch zusätzliche Techniken verwendet, um sowohl die Effizienz zu steigern als auch den Speicherverbrauch zu minimieren. Im Gegensatz zu Merge Sort arbeitet Block Sort in-place, das heißt, er sortiert die Elemente innerhalb des vorhandenen Speicherplatzes, ohne zusätzliche Arrays zu erstellen.

Die Funktionsweise beginnt mit der Unterteilung der Liste in mehrere Blöcke, ähnlich wie bei Merge Sort. Diese Blöcke werden dann einzeln in aufsteigender Reihenfolge sortiert. Anschließend führt der Algorithmus die sortierten Blöcke zusammen, wobei er nur minimalen zusätzlichen Speicher benötigt. Durch diese blockweise Bearbeitung wird der Sortiervorgang beschleunigt, ohne dass große zusätzliche Datenstrukturen erforderlich sind.

Zu den Vorteilen von Block Sort zählt der geringere Speicherverbrauch im Vergleich zu Merge Sort sowie seine Effizienz bei der Bearbeitung großer Datenmengen. Ein Nachteil ist jedoch, dass er komplexer zu implementieren ist als einfachere Sortieralgorithmen.


## Laufzeiten
Sortieralgorithmen sind essenziell, um eine Liste von Songs nach bestimmten Kriterien zu ordnen, z. B. alphabetisch nach Songtitel oder nach Künstler. In der Spotify-App stehen verschiedene Sortieralgorithmen zur Verfügung, von einfachen und intuitiven Methoden wie dem Bubble Sort bis hin zu komplexeren Algorithmen wie dem Merge Sort und Quick Sort. Jeder dieser Algorithmen hat seine spezifische Funktionsweise und wird für unterschiedliche Anwendungsfälle verwendet.
### Erkärung der Laufzeiten

### Sortieralgorithmen
#### Bubble Sort
Im besten Fall beträgt die Laufzeit von Bubble Sort O(n), wenn die Liste bereits vollständig sortiert ist. Der Algorithmus muss dann nur einmal durch die Liste laufen, um festzustellen, dass keine Vertauschungen nötig sind. Im schlimmsten Fall, wenn die Liste in umgekehrter Reihenfolge sortiert ist, beträgt die maximale Laufzeit O(n²). In diesem Szenario muss jedes Element mehrfach mit seinen Nachbarn verglichen und vertauscht werden, was zu einer quadratischen Laufzeit führt.

#### Insertion Sort
Der beste Fall für den Insertion Sort ist ebenfalls O(n), wenn die Liste bereits sortiert ist. In diesem Fall wird jedes Element nur einmal überprüft und bleibt an seinem Platz, ohne dass Verschiebungen erforderlich sind. Im schlimmsten Fall, wenn die Liste in umgekehrter Reihenfolge vorliegt, kann die maximale Laufzeit O(n²) erreichen. Hierbei muss jedes Element bis zu seiner korrekten Position verschoben werden, was zu einer quadratischen Laufzeit führt.

#### Merge Sort
Merge Sort hat sowohl im besten als auch im schlimmsten Fall eine konstante Laufzeit von O(n log n). Unabhängig von der Anordnung der Liste bleibt der Algorithmus bei O(n log n), da er die Liste in log n Teillisten aufteilt und anschließend n Vergleiche durchführt, um die Liste wieder zusammenzuführen. Diese Effizienz bleibt konstant, egal wie die ursprüngliche Liste sortiert ist.

#### Block Sort
Für den Block Sort beträgt die beste Laufzeit O(n) im Fall, dass die Blöcke bereits sortiert sind. In diesem Fall muss der Algorithmus nur einmal durch die Liste der Blöcke laufen, um zu bestätigen, dass keine weiteren Sortierungen notwendig sind. Im schlimmsten Fall kann die Laufzeit jedoch auf O(n log n) ansteigen. Dies geschieht, wenn die Blöcke zunächst unsortiert sind und der Algorithmus jeden Block sortieren und anschließend zusammenführen muss, was zusätzliche Vergleiche und Verschiebungen erfordert.

#### Quick Sort
Der beste Fall für den Quick Sort tritt auf, wenn das Pivot-Element ideal gewählt wird, sodass es das Array gleichmäßig teilt. In diesem Szenario beträgt die minimale Laufzeit O(n log n), da der Algorithmus die Liste in jeder Rekursion halbiert. Im schlimmsten Fall, beispielsweise wenn das Pivot-Element immer das kleinste oder größte Element ist und das Array somit nicht gut geteilt wird, kann die Laufzeit auf O(n²) ansteigen. Dies führt dazu, dass der Algorithmus in einer ungeordneten Liste immer nur ein Element auf einmal verarbeitet, was die Effizienz stark beeinträchtigt.
### Suchalgorithmen
#### Lineare Suche
Der beste Fall für die lineare Suche tritt ein, wenn der gesuchte Song das erste Element in der Liste ist. In diesem Fall beträgt die minimale Laufzeit O(1), da das Element sofort gefunden wird. Im schlimmsten Fall muss der Algorithmus jedoch die gesamte Liste durchsuchen, was zu einer maximalen Laufzeit von O(n) führt. Dies geschieht, wenn der gesuchte Song das letzte Element der Liste ist oder gar nicht vorkommt, wobei n die Anzahl der Songs in der Liste darstellt.

#### Binäre Suche
Die binäre Suche hat im besten Fall eine minimale Laufzeit von O(1), wenn der gesuchte Song das mittlere Element der Liste ist und sofort gefunden wird. Im schlimmsten Fall, wenn der gesuchte Song nicht in der Liste vorhanden ist oder sich am Rand der sortierten Liste befindet, beträgt die maximale Laufzeit O(log n). Der Algorithmus halbiert die Liste bei jedem Durchlauf, was zu einer logarithmischen Laufzeit führt, da n in Teilschritte von n/2, n/4 usw. unterteilt wird.

### Messen der tatsächlichen Laufzeiten
![image](https://github.com/user-attachments/assets/16723c4c-e42d-40a0-8b69-d2558fca014e)
![image](https://github.com/user-attachments/assets/8d03fa37-8749-447e-907c-f0f1e6e1c922)

## Fazit der Laufzeiten

## Zusammenfassung
