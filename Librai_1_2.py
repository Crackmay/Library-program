import os
import time
from colored import fg, bg, attr

#datos de usuarios

users = {'Tamayo': '123'}

users_Estudiante = {'paco': '123', 'Minimi': '123'}

#Datos libros

Books = {'Harry': 'Libre'}

Registro_libros = {}

#Varios

Buzon_de_sugerencias = {}

noticias_his = {}

color = fg("green") 
reset = attr("reset")
color2 = fg("red")
      
#Contraseña
def clave(createPassw):

        validar=False #que se vayan cumpliendo los requisitos uno a uno.
        long=len(createPassw) #Calcula la longitud de la contraseña
        mayuscula=False #variable para identificar letras mayúsculas
        minuscula=False #variable para contar identificar letras minúsculas
        numeros=False #variable para identificar números
        correcto=True #verifica que hayan mayuscula, minuscula, numeros y no alfanuméricos
        
        for carac in createPassw: #ciclo for que recorre caracter por caracter en la contraseña

            if carac.isupper()== True: #saber si hay mayuscula
                mayuscula=True #acumulador o contador de mayusculas
                
            if carac.islower()== True: #saber si hay minúsculas
                minuscula=True #acumulador o contador de minúsculas
                
            if carac.isdigit()== True: #saber si hay números
                numeros=True #acumulador o contador de numeros
        else:
            validar=True 
                       
        if long <5 and validar==True:
            print("Mínimo 5 caracteres")
            validar=False 

        if mayuscula == True and minuscula ==True and numeros == True and validar ==True:
           validar = True #Cumple el requisito de tener mayuscula, minuscula, numeros y no alfanuméricos
        else:
           correcto=False #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple
           
        if validar == True and correcto==False:
           print("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")

        if validar == True and correcto ==True:
           return True

#Registro de usuario_v.2

def Registro_usuario():
    print ("Bienvenido al programa librain, que se encarga de organizar datos de una biblioteca, para hacer bueno uso del sistema introdusca su identidad")
    
    global enteredName

    enteredName = input(color + "introdusca su nombre:" + reset)

    enteredPassword = input(color + "introdusca su contraseña:" + reset)

    if enteredName in users and users[enteredName] == enteredPassword:
        print(" Inicio de sesion correcto\n")
        desicion_2()
    elif enteredName in users_Estudiante and users_Estudiante[enteredName] == enteredPassword:
        print(" Inicio de sesion correcto\n")
        usuario()
    else:
        print(color2 + "El inicio de sesion es incorecto intentalo de nuevo\n" + reset)
        Registro_usuario()
        
#Menu de actividades
    
def desicion_2():            
    print ("Bienvenido Trabajador, que desas reallizar:")
    
    print (color + "1.Ingresar o eliminar Id.\n"
            "2.Registro de Id.\n"
            "3.Ingresar o eliminar libros.\n"
            "4.revisar estado de los libros.\n"
            "5.Revisar lista de prestamos.\n"
            "6.Revisar buzon de Sugerencias.\n"
            "7.Noticias semanales.\n"
            "8.salir" + reset)
        
    input_trabajo = input("ingrese su respuesta:")

    if input_trabajo == "1":
        Actividad_1()
    elif input_trabajo == "2":
        Actividad_2()
    elif input_trabajo == "3":
        Actividad_3()
    elif input_trabajo == "4":
        Actividad_4()
    elif input_trabajo == "5":
        actividad_5()
    elif input_trabajo == "6":
        actividad_6()
    elif input_trabajo == "7":
        actividad_7()
    elif input_trabajo == "8":
        Actividad_8()    
    elif input_trabajo == "a":
        Registro_usuario()
    else:
        print(color2 + "\n\nLa respuesta es invalida por favor intentalo de nuevo.\n\n" + reset)
        desicion_2()

#1ºActividad

def Actividad_1():
    
    print("Ahora que deseas hacer:")
    print(color + "a.Agregar usuarios.\n" "b.eliminar usuarios." + reset)
    remove_append = input("Ingrese su respuesta:")

    if remove_append == "a":
        print("cual es el oficio del nuevo usuario")
        print(color + "A.trabajador\nB.usuario\n" + reset)
        est_tra = input("ingrese su respuesta:")
        if est_tra == "a":
            createLogin = input("Ingresa el nombre del usuario:")
            if createLogin in users:
                print("\nEl nombre ya existe en la base de datos.")
                Actividad_1()
            else:
                createPassw = input("Ingresa la contraseña:")
                clave(createPassw)
                if clave(createPassw) == True:
                    users[createLogin] = createPassw
                    print("\nUsuario creado\n")
                    p_Menu()
                else:
                    Actividad_1()
                
        elif est_tra == "b":
            createLogin = input("Ingresa el nombre del usuario:")
            if createLogin in users_Estudiante:
                print("\nEl nombre ya existe en la base de datos.")
            else:
                createPassw = input("Ingresa la contraseña:")
                users_Estudiante[createLogin] = createPassw
                print("\nUsuario creado\n")
                p_Menu() 
        else:
            print(color2 + "La respuesta es invalida,intentalo de nuevo." + reset)
            Actividad_1()
    elif remove_append == "b":
        print("Cual es el oficio del usuario de eliminar")
        print(color + "A.Trabajador\nB.usuario\n" + reset)
        oficio = input("Ingrese su respuesta:")
        if oficio =="a":
            Append_Name = input("Ingrese el nombre de usuario a eliminar: ")
            if Append_Name in users:
                del users[Append_Name]
                print("Usuario eliminado")
                p_Menu()
        elif oficio == "b":
            Append_Name = input("Ingrese el nombre de usuario a eliminar: ")
            if Append_Name in users_Estudiante:
                del users_Estudiante[Append_Name]
                print("Usuario eliminado")
                p_Menu()
        else:
            print(color2 + "La respuesta es invalida,intentalo de nuevo.\n" + reset)
            Actividad_1()
    elif remove_append == "1":
        p_Menu()
    else:
        print(color2 + "La respuesta es invalida,intentalo de nuevo.\n" + reset)
        Actividad_1()

#2ºActividad

def Actividad_2():

    print(users)
    print(users_Estudiante)
    p_Menu()

#3ºActividad

def Actividad_3():

    print("Que deseas hacer:")
    print(color + "A.Eliminar libro.\nB.Agregar libro." + reset)
    actividad3 = input("Ingrese su respuesta:")
    if actividad3 == "a":
        create_Books = input("Ingresa el nombre del libro:")
        if create_Books in Books:
            print("\nEl nombre ya existe en la base de datos.")
        else:
            create_status = input("Ingrese el estado:")
            Books[create_Books] = create_status   
            p_Menu()
        
    elif actividad3 == "b":
        LibroElim = input("Ingrese el libro a eliminar: ")
        if LibroElim in Books:
            del Books[LibroElim]
            print("Usuario eliminado")
            p_Menu()
    else:
        print(color2 + "Respuesta invalida, intentalo de nuevo.\n" + reset)
        Actividad_3()
            
#4ºActividad

def Actividad_4():
    
    print(Books)       
    p_Menu()

#5ºActividad

def actividad_5():

    print(Registro_libros)
    p_Menu()

#6ºActividad

def actividad_6():
    print(Buzon_de_sugerencias)
    p_Menu()

#7ºActividad

def actividad_7():
    print("Que deseas realiazar")
    print(color + "A. Revisar noticia.\nB. Agregar noticia." + reset)
    noticias = input()
    if noticias == "a":
        print(noticias_his)
        p_Menu()
    elif noticias == "b":
        fecha = input("Ingrese la fecha de la noticia:\n")
        datos = input("Ingrese la noticia:")

        noticias_his[fecha] = datos
        p_Menu()
    else:
        print(color2 + "Respuesta invalida, intenmtalo de nuevo.\n" + reset)
        actividad_7()

#8ºActividad

def Actividad_8():
    
    print(color2 + "Se cerrara el programa en unos segundos" + reset)
    time.sleep(1)
    os.system ("cls")

#2ºactividades

def p_Menu():

        print("Ahora que quieres hacer:")
        print(color + "A. Volver al menu de trabajos.\nB. Salir" + reset)
        Desicion_9 = input("R/")

        if Desicion_9 == "b":
            print(color2 + "El programa se cerrara en unos segundos" + reset)
            time.sleep(1)
            os.system ("cls")

        elif Desicion_9 == "a":
                desicion_2()

        else:
            print(color2 + "La respuesta es incorrecta.\n" + reset)
            p_Menu()

#p_Menu_2

def p_Menu_2():
    print("Ahora que quieres hacer:")
    print(color + "A. Volver al menu de Actividades.\nB. Salir" + reset)
    Desicion_15 = input("R/")

    if Desicion_15 == "b":
            os.system ("cls")

    elif Desicion_15 == "a":
            usuario()

    else:
        print(color2 + "La respuesta es incorrecta.\n" + reset)
        p_Menu_2()
            
#Menu de actividades estudiantes

def usuario():
    print("Bienvenido usurio, que deseas realizar:")
    print(color + "1.Revisar lista de libros:\n"
          "2.Prestar algun libro:\n"
          "3.Noticias:\n"
          "4.Buzon de sugerencias:\n"
          "5.Salir:" + reset)

    input_usuario = input("ingrese su respuesta:")

    if input_usuario == "1":
        trabajo_1()
    elif input_usuario == "2":
        trabajo_2()
    elif input_usuario == "3":
        trabajo_3()
    elif input_usuario == "5":
        trabajo_4()
    elif input_usuario == "4":
        trabajo__5()
    elif input_usuario == "6":
        trabajo_6()    
    else:
        print(color2 + "\n\nLa respuesta es invalida por favor intentalo de nuevo.\n\n" + reset)
        desicion_2()

#Trabajo_1

def trabajo_1():
    print(Books)
    p_Menu_2()

#Trabajo_2

def trabajo_2():

    Aped_Name = input("Ingrese el nombre del libro a prestar:")
        
    if Aped_Name in Books:
        del Books[Aped_Name]

        print(color2 + "Usuario eliminado" + reset)
        Registro_libros[enteredName] = Aped_Name
        p_Menu_2()
    else:
        print(color2 + "El libro no existe, intentalo de nuevo" + reset)
        usuario()




#Trabajo_3

def trabajo_3():
    print(noticias_his)
    p_Menu_2()
    

#Trabajo_4

def trabajo_4():
    print(color2 + "Se cerrara el programa en unos segundos" + reset)
    time.sleep(1)
    os.system ("cls")

#Trabajo 5

def trabajo__5():
    fecha = input("Ingrese la sugerencia: ")
    Buzon_de_sugerencias = fecha
    time.sleep(1)
    print("Mucha gracias por tu sugerencia")
    time.sleep(1)
    p_Menu_2()


#trabajo 6#

def trabajo_6():
    Registro_usuario()  

#FIN

Registro_usuario()
