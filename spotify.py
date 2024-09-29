import os
import time
import random
import string
import sys
sys.setrecursionlimit(3000)  # Erhöht das Rekursionslimit auf 1500

class Song:
    def __init__(self, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.album})"

    def __lt__(self, other):
        return self.title.lower() < other.title.lower()

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()

class RedBlackNode:
    def __init__(self, song):
        self.song = song
        self.color = "RED"  # All newly inserted nodes are red by default
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackNode(None)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    def insert(self, song):
        new_node = RedBlackNode(song)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.song < current.song:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.song < parent.song:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "RED"
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)

        self.root.color = "BLACK"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, song):
        return self._search_recursive(self.root, song)

    def _search_recursive(self, node, song):
        if node == self.NIL or node.song == song:
            return node != self.NIL
        if song < node.song:
            return self._search_recursive(node.left, song)
        else:
            return self._search_recursive(node.right, song)
        
    

class MusicApp:
    FILENAME = "songs.csv"

    def __init__(self):
        self.songs = []
        self.rbt = RedBlackTree()
        self.load_songs()
        self.favourites=[]

    def delete_song_from_favourites(self, deleted_song):
        for item in self.favourites :
            if item["title"]==deleted_song:
                self.favourites.remove(item)
                print("\nyour song is now deleted from your favourites playlist")
                return 
        print("\nthat song could not have been found in your favourites")
                   

    def new_song_to_favourites(self, song):
        for item in self.favourites:
            if item["title"]==song:
                print("\nthat song is already in your favourites")
                return
        for entry in self.songs:
            if entry.title==song:
                self.favourites.append({"title":entry.title, "artist":entry.artist, "album": entry.album})
                print("\nyour song is now in your favourites playlist")
                return 
        print("\nyour song has not been found in your songs")
       

    def load_songs(self):
        """Load songs from a file when the app starts."""
        if os.path.exists(self.FILENAME):
            with open(self.FILENAME, 'r') as file:
                for line in file:
                    title, artist, album = line.strip().split(',')
                    song = Song(title, artist, album)
                    self.songs.append(song)
                    self.rbt.insert(song)  # Insert into the Red-Black Tree
            print(f"{len(self.songs)} songs loaded from {self.FILENAME}.")
        else:
            print("No songs found. Starting with an empty music library.")

    def save_songs(self):
        """Save all songs to a file."""
        with open(self.FILENAME, 'w') as file:
            for song in self.songs:
                file.write(f"{song.title},{song.artist},{song.album}\n")
        print(f"{len(self.songs)} songs saved to {self.FILENAME}.")

    def add_song(self, title, artist, album):
        song = Song(title, artist, album)
        self.songs.append(song)
        self.rbt.insert(song)  # Insert into the Red-Black Tree
        self.save_songs()  # Save after adding a song
        print(f"'{song}' added to your music library.")

    def delete_song(self, title):
        song_to_delete = next((s for s in self.songs if s.title == title), None)
        if song_to_delete:
            self.songs.remove(song_to_delete)
            # Note: Red-Black Tree deletion would require a delete operation to be implemented
            self.save_songs()  # Save after deleting a song
            print(f"'{song_to_delete}' removed from your music library.")
        else:
            print(f"'{title}' not found in your music library.")

    def display_songs(self):
        if self.songs:
            print("Your music library:")
            for i, song in enumerate(self.songs, 1):
                print(f"{i}. {song}")
        else:
            print("Your music library is empty.")

    def linear_search(self, song_title):
        # Iteriere durch alle Songs in der Liste
            for song in self.songs:
                # Wenn der Titel übereinstimmt, gib das Song-Objekt zurück
                if song.title.lower() == song_title.lower():
                    return song
            # Wenn kein Song gefunden wurde, gib None zurück
            return None

    def binary_search(self, song_title):
        # Sortiere die Liste der Songs nach dem Titel
        self.songs.sort(key=lambda song: song.title.lower())  # Sortiere nach Titel, ignoriere Groß- und Kleinschreibung

        # Setze die Start- und Endpunkte der Liste
        low = 0
        high = len(self.songs) - 1

        # Binäre Suche durchführen
        while low <= high:
            mid = (low + high) // 2
            # Vergleiche den Titel des mittleren Elements mit dem gesuchten Titel
            if self.songs[mid].title.lower() == song_title.lower():
                return self.songs[mid]  # Song gefunden, gib das Song-Objekt zurück
            elif self.songs[mid].title.lower() < song_title.lower():
                low = mid + 1  # Suche in der oberen Hälfte weiter
            else:
                high = mid - 1  # Suche in der unteren Hälfte weiter

        # Wenn der Song nicht gefunden wird, gib None zurück
        return None

    def search_song(self):
        print("\nChoose a search method:")
        print("L for Linear Search")
        print("B for Binary Search")

        choice = input("Enter your choice: ").strip().lower()

        if choice == 'l':
            song_title = input("Enter the song title to search: ").strip()
            start_time = time.time()  # Zeitmessung starten
            result = self.linear_search(song_title)
            end_time = time.time()  # Zeitmessung beenden
            if result is not None:  # Überprüfe, ob ein Song gefunden wurde
                print(f"Song found: {result.title} by {result.artist}")
            else:
                print("Song not found.")
            print(f"Linear Search completed in {end_time - start_time:.6f} seconds.")

        elif choice == 'b':
            song_title = input("Enter the song title to search: ").strip()
            start_time = time.time()  # Zeitmessung starten
            result = self.binary_search(song_title)
            end_time = time.time()  # Zeitmessung beenden
            if result is not None:  # Überprüfe, ob ein Song gefunden wurde
                print(f"Song found: {result.title} by {result.artist}")
            else:
                print("Song not found.")
            print(f"Binary Search completed in {end_time - start_time:.6f} seconds.")

        else:
            print("Invalid choice. Please select a valid search method.")


    # Sortierschleife
    def sort_songs(self):
        print("\nChoose a sorting method:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Merge Sort")
        print("4. Quick Sort")
        print("5. Block Sort")  # Blocksort hinzugefügt

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            self.bubble_sort()

        elif choice == '2':
            start_time = time.time()  # Startzeit messen
            print("Sorting with Insertion Sort...")
            self.insertion_sort()
            end_time = time.time()  # Endzeit messen
            # print(f"Insertion Sort completed in {end_time - start_time:.6f} seconds.")  # Zeit ausgeben

        elif choice == '3':
            start_time = time.time()  # Startzeit messen
            print("Sorting with Merge Sort...")
            self.merge_sort(self.songs)
            end_time = time.time()  # Endzeit messen
            print(f"Merge Sort completed in {end_time - start_time:.6f} seconds.")  # Zeit ausgeben

        elif choice == '4':
            start_time = time.time()  # Startzeit messen
            print("Sorting with Quick Sort...")
            self.quick_sort(0, len(self.songs) - 1)
            end_time = time.time()  # Endzeit messen
            print(f"Quick Sort completed in {end_time - start_time:.6f} seconds.")  # Zeit ausgeben

        elif choice == '5':
            block_size = int(input("Enter block size for sorting: "))  # Fragt die Blockgröße ab
            print("Sorting with Block Sort...")
            self.block_sort(block_size)
            
        else:
            print("Invalid choice. Please select a valid sorting method.")






    def bubble_sort(self):
            start_time = time.time()  # Startzeit messen
            print("Sorting with Bubble Sort...")
            n = len(self.songs)
            for i in range(n):
                for j in range(0, n-i-1):
                    if self.songs[j].title.lower() > self.songs[j+1].title.lower():
                        self.songs[j], self.songs[j+1] = self.songs[j+1], self.songs[j]
            end_time = time.time()  # Endzeit messen
            print(f"Bubble Sort completed in {end_time - start_time:.6f} seconds.")  # Zeit ausgeben
    
    def insertion_sort(self):
            start_time = time.time()  # Startzeit messen
            for i in range(1, len(self.songs)):
                key = self.songs[i]
                j = i-1
                while j >= 0 and key.title.lower() < self.songs[j].title.lower():
                    self.songs[j + 1] = self.songs[j]
                    j -= 1
                self.songs[j + 1] = key
            end_time = time.time()  # Endzeit messen
            print(f"Insertion Sort completed in {end_time - start_time:.6f} seconds.")  # Zeit ausgeben
    

    # Merge Sort Methode (wie vorher beschrieben)
    def merge_sort(self, songs):
        if len(songs) > 1:
            mid = len(songs) // 2
            left_half = songs[:mid]
            right_half = songs[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i].title.lower() < right_half[j].title.lower():
                    songs[k] = left_half[i]
                    i += 1
                else:
                    songs[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                songs[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                songs[k] = right_half[j]
                j += 1
                k += 1

    def merge(self, left_half, right_half):
        """Hilfsmethode zum Mergen von zwei Listen."""
        result = []
        i = j = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i].title < right_half[j].title:
                result.append(left_half[i])
                i += 1
            else:
                result.append(right_half[j])
                j += 1

        result.extend(left_half[i:])
        result.extend(right_half[j:])
        return result

    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)



    def partition(self, low, high):
        pivot = self.songs[high]
        i = low - 1
        for j in range(low, high):
            if self.songs[j].title.lower() <= pivot.title.lower():
                i += 1
                self.songs[i], self.songs[j] = self.songs[j], self.songs[i]
        self.songs[i + 1], self.songs[high] = self.songs[high], self.songs[i + 1]
        return i + 1

    def heap_sort(self, songs):
        pass

    
        
    def create_random_songs(self, count):
       

        for _ in range(count):
            title = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            artist = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            album = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
            self.add_song(title, artist, album)
    
    def block_sort(self, block_size=10):
        """Sortiert die Songs mit einem Blocksort-Algorithmus."""
        start_time = time.time()  # Startzeit für die Messung
        n = len(self.songs)
        
        # Schritt 1: Aufteilen der Songs in Blöcke
        blocks = [self.songs[i:i + block_size] for i in range(0, n, block_size)]
        
        # Schritt 2: Sortiere jeden Block einzeln (kann z.B. Merge Sort verwenden)
        for block in blocks:
            self.merge_sort(block)  # Merge Sort wird verwendet, um jeden Block zu sortieren
        
        # Schritt 3: Mergen aller Blöcke in einer sortierten Reihenfolge
        sorted_songs = []
        for block in blocks:
            sorted_songs = self.merge(sorted_songs, block)
        
        self.songs = sorted_songs
        end_time = time.time()  # Endzeit für die Messung
        print(f"Block Sort completed in {end_time - start_time:.6f} seconds.")  # Ausgabe der Zeit



# Hauptfunktion
def main():
    app = MusicApp()

    while True:
        print("\n--- Music App ---")
        print("1. Add Song")
        print("2. Delete Song")
        print("3. Display Songs")
        print("4. Search Song")
        print("5. Sort Songs")
        print("6. Exit")
        print("7. Create Random Songs")
        print("8. Add song to your favourites")
        print("9. Delete song from your favourites")
        print("10. Show favourites")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            title = input("Enter song title: ").strip()
            artist = input("Enter artist name: ").strip()
            album = input("Enter album name: ").strip()
            app.add_song(title, artist, album)

        elif choice == '2':
            title = input("Enter song title to delete: ").strip()
            app.delete_song(title)

        elif choice == '3':
            app.display_songs()

        elif choice == '4':
            app.search_song()

        elif choice == '5':
            app.sort_songs()

        elif choice == '6':
            print("Exiting Music App. Goodbye!")
            break

        elif choice == '7':
            count = int(input("Enter number of random songs to create: "))
            app.create_random_songs(count)

        elif choice=="8":
            song=str(input("Which song do you want to add to your favourites?"))
            app.new_song_to_favourites(song)

        elif choice=="9":
            deleted_song=str(input("Which song do you want to delete from your favourites?"))
            app.delete_song_from_favourites(deleted_song)

        elif choice=="10":
            print(f"Your Favourie Playlist: {app.favourites}")

        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()