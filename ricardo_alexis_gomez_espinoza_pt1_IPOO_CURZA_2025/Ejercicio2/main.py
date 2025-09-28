from PasswordAnalizer import PasswordAnalizer

passwordAnalizer = PasswordAnalizer()

print(passwordAnalizer.esClaveFuerte("Alexis2"))

claveGenerica = passwordAnalizer.generarClave()
print(claveGenerica)
print(passwordAnalizer.esClaveFuerte(claveGenerica))