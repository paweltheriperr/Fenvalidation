import re

def is_fen(fen):
    # Sprawdzenie poprawności FEN przy użyciu wyrażenia regularnego
    pattern = r'^([rnbqkpRNBQKP1-8]+\/){7}[rnbqkpRNBQKP1-8]+ [wb] (-|[KQkq]+) (-|[a-h][36]) \d+ \d+$'
    return bool(re.match(pattern, fen))

while True:
    fen = input("Podaj pozycję szachową w notacji FEN: ")
    if is_fen(fen):
        break
    print("Niepoprawna notacja FEN. Spróbuj jeszcze raz.")

print("Podana pozycja to:", fen)

print(is_fen(fen))
