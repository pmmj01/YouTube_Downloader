YouTube Downloader

## Introduction This is a simple YouTube downloader script written in Python using the pytube library. The script allows the user to download YouTube videos in either MP4 or MP3 format. It provides a command-line interface for user interaction.

Features Downloads YouTube videos in MP4 or MP3 format based on user preference. Displays real-time download progress with details like percentage, size, and download speed. Records download information such as timestamp, title, size, and speed in a log file (download_data.txt). Supports user input to choose the download format and exit the program when needed.

Requirements Python 3.x pytube library

How to Use Run the script (YoutubeDownloader_v2.py) in your terminal or command prompt. Input the YouTube video link when prompted. Choose the desired format (mp4 or mp3) when prompted. The script will download the video and display real-time progress. The downloaded video or audio file will be saved in the specified output path.

Important Note Ensure that you have the necessary permissions to download and save files in the specified output path. The script utilizes the pytube library, so an internet connection is required to fetch YouTube video information.

Example Usage & C:/Users/your_username/python3.12.exe YoutubeDownloader_v2.py

Additional Information This script dynamically determines the current user's name for the download path. It logs download information to the download_data.txt file for future reference.

## Changing Language

To change the language of the YouTube downloader script, follow these steps:

1. Open the `settings.txt` file located in the same directory as the script.

2. Find the `language` parameter in the `settings.txt` file.

3. Change the value of the `language` parameter to one of the following options:

   - Polish
   - English (default language)
   - Spanish
   - Chinese
   - Arabic
   - Italian
   - French

4. Save the `settings.txt` file.

5. Run the script again to apply the new language settings.

Note: If the specified language is not supported, the script will default to English.

## Wprowadzenie To prosty skrypt do pobierania filmów z serwisu YouTube napisany w języku Python przy użyciu biblioteki pytube. Skrypt umożliwia użytkownikowi pobieranie filmów z YouTube w formatach MP4 lub MP3. Zapewnia interfejs wiersza polecenia do interakcji z użytkownikiem.

Funkcje Pobieranie filmów z YouTube w formatach MP4 lub MP3 zgodnie z preferencjami użytkownika. Wyświetlanie postępu pobierania w czasie rzeczywistym z informacjami o postępie, rozmiarze i prędkości pobierania. Zapisywanie informacji o pobieraniu, takich jak znacznik czasu, tytuł, rozmiar i prędkość, w pliku dziennika (download_data.txt). Obsługa wejścia użytkownika w celu wyboru formatu pobierania i zakończenia programu w dowolnym momencie.

Wymagania Python 3.x Biblioteka pytube

Jak używać Uruchom skrypt (YoutubeDownloader_v2.py) w terminalu lub wierszu polecenia. Podaj link do filmu z YouTube, gdy zostaniesz o to poproszony. Wybierz preferowany format (mp4 lub mp3) w odpowiedzi na pytanie. Skrypt pobierze film i wyświetli postęp w czasie rzeczywistym. Pobrany plik wideo lub audio zostanie zapisany w określonej ścieżce wyjściowej.

Ważna uwaga Upewnij się, że masz odpowiednie uprawnienia do pobierania i zapisywania plików w określonej ścieżce wyjściowej. Skrypt korzysta z biblioteki pytube, więc wymagane jest połączenie internetowe w celu pobrania informacji o filmie z YouTube.

Przykładowe użycie & C:/Users/twoja_nazwa_uzytkownika/python3.12.exe YoutubeDownloader_v2.py

Dodatkowe informacje Ten skrypt dynamicznie określa nazwę bieżącego użytkownika do ścieżki pobierania. Loguje informacje o pobieraniu do pliku download_data.txt dla przyszłych odniesień.

## Zmiana Języka

Aby zmienić język skryptu do pobierania filmów z YouTube, wykonaj następujące kroki:

1. Otwórz plik `settings.txt`, znajdujący się w tym samym katalogu co skrypt.

2. Znajdź parametr `language` w pliku `settings.txt`.

3. Zmień wartość parametru `language` na jedną z następujących opcji:

   - Polish
   - English (domyślny język)
   - Spanish
   - Chinese
   - Arabic
   - Italian
   - French

4. Zapisz plik `settings.txt`.

5. Uruchom ponownie skrypt, aby zastosować nowe ustawienia językowe.

Uwaga: Jeśli określony język nie jest obsługiwany, skrypt automatycznie przełączy się na język angielski.
