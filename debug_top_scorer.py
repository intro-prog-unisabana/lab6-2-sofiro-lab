scores = {}  # ← cambio 1: debe ser diccionario, no lista

while True:
    user_input = input("Enter player and score as 'name score' (or type 'stop' to finish):\n")
    
    if user_input.lower() == "stop":
        break

    name, score = user_input.split()
    score = int(score)

    if name in scores:
        scores[name] += score   # ← cambio 2: sumar, no restar
    else:
        scores[name] = score

if len(scores) == 0:
    print("No scores recorded.")
else:
    top_name = ""
    top_score = -1  # ← cambio 3: iniciar en -1 para comparar correctamente

    for name in scores:
        if scores[name] > top_score:  # ← cambio 4: usar '>' para máximo
            top_score = scores[name]
            top_name = name

    print(f"Top scorer: {top_name} with {top_score} points.")