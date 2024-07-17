from translate import Translator

# Crear un objeto traductor
translator = Translator(from_lang='spanish', to_lang="english")
# Pregunta la frase
txt = input("Que quieres traducir?  ")
# Traducir una frase
res = translator.translate(txt)
# Imprime la frase traducida
print(res)
