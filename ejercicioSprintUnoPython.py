import re # importacion de las expresiones regulares de py

# Correos registrados como ejemplo para el funcionamiento de las funciones de busqueda y de listado
correosdocentes = ["daniel@utv.edu.co", "gerardo@utv.edu.co"]
correosestudiantes = ["daniel@estudiante.utv.edu.co", "david@estudiante.utv.edu.co"]

# funcion para hacer la validacion de el correo electronico
def validaCorreo(correo):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, correo) is not None

# ciclo para mantener la ejecucion del programa
while True:
    # Mostrar el menú
    print("\nBienvenido al sistema de gestión de correos de la Universidad Tecnológica del Valle."
    "\nPara comenzar, seleccione una de las siguientes opciones:"
    "\n1. Registrar un nuevo correo"
    "\n2. Ver lista de correos registrados"
    "\n3. Buscar un correo"
    "\n4. Salir de la aplicación"
    )

    try:
        seleccionMenu = int(input("\nIngrese la opción: "))

        if seleccionMenu == 1:
            # argumentos para registrar un nuevo correo            
            print("Ha ingresado a la opción 1: Registrar un nuevo correo")
            
            nuevoCorreo= input("Ingrese el correo electrónico: ").strip().lower()
            
            if not validaCorreo(nuevoCorreo):
                print("****************************"+"\nFormato invalido, el correo NO se ha registrado"+"\n****************************")
                continue
            
            if nuevoCorreo.endswith("@estudiante.utv.edu.co"):
                correosestudiantes.append(nuevoCorreo)
                print("\n"+"****************************"+"\n")
                print(f"el correo {nuevoCorreo} ha sido registrado con exito como Estudiante")
                print("\n"+"****************************"+"\n")
                
            elif nuevoCorreo.endswith("@utv.edu.co"):
                correosdocentes.append(nuevoCorreo)
                print("\n"+"****************************"+"\n")
                print(f"el correo {nuevoCorreo} ha sido registrado con exito como Docente")
                print("\n"+"****************************"+"\n")
                
            else:
                print("Error, debe ingresar un correo institucional")
                        
            
        elif seleccionMenu == 2:
            # argumentos para listar los correos registrados
            print("\nHa ingresado a la opción 2: Ver lista de correos registrados"
                  "\nLa Lista de correos es: "
                  "\n"
                  )
            # mostrar correos de estudiantes
            print("Los Estudiantes registrados son:" + "\n")
            for correo in correosestudiantes:
                print(f"- {correo}")
                
            # mostrar correos de docentes
            print("\n")
            print("Los Docentes registrados son:" + "\n")
            for correo in correosdocentes:
                print(f"- {correo}")
                
        elif seleccionMenu == 3:
            # argumentos para la busqueda de un correo electronico con una palabra clave
            print("Ha ingresado a la opción 3: Buscar un correo")
            
            busqueda = input("Ingresa texto a buscar en los correos electrónicos: ").lower()
            
            todosLosCorreos = correosdocentes + correosestudiantes # union de ambas listas en una unica lista para la busqueda
            
            resultados = [correo for correo in todosLosCorreos if busqueda in correo] # ciclo for corto para recorrer las listas de correos electronicos

            if resultados:
                print("\nCorreos encontrados:")
                for correo in resultados:
                    categoria = "Estudiante" if correo in correosestudiantes else "Docente"
                    
                    print(f"\n- {correo} ({categoria})")
                    
            else:
                print("\n"+"****************************"+"\n")
                print("No se encontraron coincidencias.")
                print("\n"+"****************************"+"\n")
                
        elif seleccionMenu == 4:
            # cierre de la aplicacion
            print("Ha ingresado a la opción 4: Salir de la aplicación" + "\nSesion terminada, hasta luego")
            break  # Sale del bucle y termina el programa
        else:
            print("Opción inválida. Intente nuevamente.")
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número del 1 al 4.")