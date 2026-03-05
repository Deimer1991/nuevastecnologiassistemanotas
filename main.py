from src.funtions import *

def inicio():
    
    while True:
        print("\n********** SISTEMA DE NOTAS **********\n")
        print("1. Registrar Estudiante")
        print("2. Registrar Nota")
        print("3. Ver Promedio Individual")
        print("4. Ver Estudiantes")
        print("5. Salir\n")
       
    
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            registrar_nota()
        elif opcion == "3":
            ver_promedio()
        elif opcion == "4":
            mostrar_estudiantes()
        elif opcion == "5":
            print("Salir")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
    

if __name__ == "__main__":
    inicio()