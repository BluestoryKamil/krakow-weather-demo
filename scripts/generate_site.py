plik_html = "../templates/index.html"

with open(plik_html, "r", encoding="utf-8") as file:
    stuff_inside = file.read()

stuff_inside = stuff_inside.replace("{{TITLE}}", "Pogoda i jakość powietrza w Krakowie")
stuff_inside = stuff_inside.replace("{{DESCRIPTION}}", "Dzisiaj jest naprawdę bardzo fajny dzień")

with open(plik_html, "w", encoding="utf-8") as file:
    file.write(stuff_inside)