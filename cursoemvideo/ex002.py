n = input('Digite algo que para ser analisado: ')
print('qual seu tipo primitivo', type(n))
print('é do tipo numerico: ', n.isnumeric())
print('È do tipo alfabetico: ', n.isalpha())
print('Ele contem espaços: ', n.isspace())
print('Ele é do tipo alfanumerico: ', n.isalnum())
print('Esta escrito en letras maiusculas: ', n.isupper())
print('Esta escrito em letras minusculas: ', n.islower())
print('Esta capitalizado: ', n.istitle())
