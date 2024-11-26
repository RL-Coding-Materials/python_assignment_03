import yfinance as yf
import pandas as pd
import numpy as np

def find_crossovers():
    """
    Pobiera dane BTC-USD od 2024-01-01, oblicza 50-dniową i 200-dniową średnią kroczącą,
    identyfikuje punkty przecięcia i zwraca listę dat tych przecięć.
    
    Returns:
        list: Lista dat przecięć w formacie 'YYYY-MM-DD'.
    """
    
    return # TODO lista



def calculate_total_btc_traded():
    """
    Pobiera dane BTC-USD z całego 2024 roku, oblicza ilość BTC handlowanych w każdym dniu
    oraz zwraca łączną ilość BTC dla dnia z najwyższym wolumenem.
    
    Returns:
        int: Łączna ilość BTC handlowanych w dniu z najwyższym wolumenem.
    """

    return # TODO int


if __name__ == '__main__':
    # Wywołanie funkcji i uzyskanie wyników
    crossover_dates = find_crossovers()
    total_traded = calculate_total_btc_traded()
    
    # Drukowanie wyników w żądanym formacie
    print(" ".join(crossover_dates))
    print(total_traded)
