from src.dict import estudiantes

def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    
    if nombre in estudiantes:
        print("El estudiante ya existe.")
    else:
        estudiantes[nombre] = []
        print("*" * 50)
        print("Estudiante registrado correctamente.")
        print("*" * 50)


def registrar_nota():
    nombre = input("Ingrese el nombre del estudiante: ")
    
    if nombre in estudiantes:
        while True:
            try:
                nota = float(input("Ingrese la nota (0 a 5): "))
                
                if 0 <= nota <= 5:
                    estudiantes[nombre].append(nota)
                    print("Nota registrada correctamente.")
                    break
                else:
                    print("La nota debe estar entre 0 y 5.")
                    
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