from src.dict import estudiantes

def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    
    if nombre in estudiantes:
        print("El estudiante ya existe.")
    else:
        estudiantes[nombre] = []
        print("Estudiante registrado correctamente.")


def registrar_nota():
    nombre = input("Ingrese el nombre del estudiante: ")
    
    if nombre in estudiantes:
        try:
            nota = float(input("Ingrese la nota: "))
            estudiantes[nombre].append(nota)
            print("Nota registrada correctamente.")
        except:
            print("Debe ingresar un número válido.")
    else:
        print("El estudiante no existe.")


def ver_promedio():
    nombre = input("Ingrese el nombre del estudiante: ")
    
    if nombre in estudiantes:
        if len(estudiantes[nombre]) > 0:
            promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
            print(f"El promedio de {nombre} es: {promedio:.2f}")
        else:
            print("El estudiante no tiene notas registradas.")
    else:
        print("El estudiante no existe.")


def mostrar_estudiantes():
    if estudiantes:
        print("Lista de estudiantes:")
        for nombre in estudiantes:
            print("-", nombre)
    else:
        print("No hay estudiantes registrados.")