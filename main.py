nome = "Riccardo"
cognome = "Motta"
nome_completo = nome + " " + cognome

with open("output.txt", mode = "a") as file:
    file.write("Hello World")

print("\nStringa 'hello world' scritta sul file 'output.txt' correttamente")