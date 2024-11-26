import json
import re

def process_tram_data(input_file):
    # Wczytaj dane z pliku JSON input_file

    # Przekształć dane na format słownikowy


    # trams - zawartość do zapisu w pliku 'tramwaje_out.json'
    # line_stop_counts - lista krotek (linia, liczba przystanków)
    # all_stops - set ze wszystkich przystanków
    return trams, line_stop_counts, len(all_stops)

if __name__ == '__main__':
    # Wywołanie funkcji
    trams, line_stop_counts, unique_stop_count = process_tram_data('tramwaje.json')

    # Zapisz dane do nowego pliku JSON 'tramwaje_out.json'

    # Wypisz wyniki: linia - liczba przystanków (po tym posortowane od największego) 
    # Wypisz wyniki: liczba wszystkich unikanych przystanków
