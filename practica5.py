import mysql.connector
import os


class Database:
     def __init__(self):
          self.conexion = mysql.connector.Connect(
               host='localhost',
               user= 'root',
               password='melenciano1629',
               db='agenda'

         )

          self.cursos = self.conexion.cursor()

     #Metodo Agregar
     def Agregar(self,id,nombre,apellido,telefono,direccion):

          sql = "INSERT INTO agendatel (idcod,nombre,apellido,telefono,direccion) VALUES ('{}','{}','{}','{}','{}')".format(id,nombre,apellido,telefono,direccion)

          try:
              self.cursos.execute(sql)
              count = self.cursos.rowcount
              self.conexion.commit()
              self.cursos.close()
              self.conexion.close()
              print('SUS REGISTROS SE A AGREGADO CORRECTAMENTE')

          except Exception as ex:
              print('SU REGISTRO NO ES VALIDO')

              raise


     #Metodo listar todos los contactos
     def listar_contactos(self):
         sql = 'SELECT idcod,nombre,apellido,telefono,direccion FROM agendatel'

         try:
             self.cursos.execute(sql)
             agendatel = self.cursos.fetchall()

             for mostrar in agendatel:
                 print('ID:', mostrar[0])
                 print('Nombre:', mostrar[1])
                 print('Apellido:', mostrar[2])
                 print('Telefono:', mostrar[3])
                 print('Direccion:', mostrar[4])
                 print('----------\n')


         except Exception as ex:
             raise




     #Metodo mostrar
     def Mostrar(self,name):

         sql= "SELECT idcod, nombre, apellido, telefono, direccion FROM agendatel WHERE nombre = '{}' ".format(name)

         try:

            self.cursos.execute(sql)
            agendatel = self.cursos.fetchone()

            print('ID:', agendatel[0])
            print('Nombre:', agendatel[1])
            print('Apellido:', agendatel[2])
            print('Telefono:', agendatel[3])
            print('Direccion:', agendatel[4])
            self.cursos.close()
            self.conexion.close()



         except Exception as ex:
           
             raise



     #metodo Actualizar
     def Actualizar(self,telefono,nom):
         sql = "UPDATE agendatel SET telefono = '{}' WHERE nombre = '{}'".format(telefono, nom)
         try:
             self.cursos.execute(sql)
             self.conexion.commit()
             self.cursos.close()
             self.conexion.close()

         except Exception as ex:

             raise


     #metodo eliminar
     def Eliminar(self,codigoid):

         sql = " DELETE FROM agendatel WHERE idcod = {}".format(codigoid)

         try:
             self.cursos.execute(sql)
             self.conexion.commit()
             self.cursos.close()
             self.conexion.close()
             print('EL REGISTRO SE A ELIMINADO CORRECTAMENTE!!!')

         except Exception as ex:
             print('EL ID_CODIGO NO ES VALIDO!!!')
             raise







#Funcion de limpiar consola
def clear():
    if os.name == "posix":
        os.system("cls")
    elif os.name == ("ce","nt","dos"):

        os.system("clear")




#Funcion de menu principal.
def menu_principal():

    opcion = 0
    while opcion != 6:
         print('\tWELCOME AGENDA TELEFONICA')

         print('1.AGREGAR NUEVO CONTACTO.')
         print('2.MOSTRAR TODOS LOS CONTACTOS.')
         print('3.BUSCAR CONTACTO.')
         print('4.ACTUALIZAR CONTACTO.')
         print('5.ELIMINAR UN CONTACTO.')
         print('6.SALIR.')
         opcion = int(input("ELEGIR OPCION: "))
         clear()
         
         print("\n")


         
         database = Database()
         if opcion == 1:

             agregar = ""
             while agregar != "no":

                 id= str(input('Ingrese CodigoID: '))
                 nombre = str(input('Digite su nombre: '))
                 apellido = str(input('Introduzca su Apellido: '))
                 telefono = str(input('Diga cual es su Telefono: '))
                 direccion = str(input('Cual es su direccion: '))
                 agregar= database.Agregar(id,nombre,apellido,telefono,direccion)
                 if agregar == 0:
                      print("EL REGISTRO NO SE PUDO AGREGAR")
                 else:
                      print("EL REGISTRO SE AGREGO CORRECTAMENTE")
                 print("\n")
                 agregar = input("DESEA AGREGAR OTRO REGISTRO(SI/NO)?: ")
                 print("\n")
                 

         #opciones del menu
         elif opcion == 2:
             database.listar_contactos()
             print("\n")


         elif opcion == 3:
            nom = str(input('Digite el Nombre A buscar: '))
            print("\n")
            database.Mostrar(nom)




         elif opcion == 4:
             clear()
             nom = str(input('Digita el nombre del registro a Actualizar: '))
             database.buscar_user(nom)
             clear()
             print("\n")

             cell = input('Telefono: ')

             actualizar = database.Actualizar(cell , nom)
             if actualizar == 0:
                 print("EL REGISTRO NO SE PUDO ACTUALIZAR")
             else:
                 print("EL REGISTRO SE ACTUALIZO CORRECTAMENTE")


         elif opcion == 5:

             codigo = str(input('INTRODUZCA EL ID DEL REGISTRO: '))
             eliminar = database.Eliminar(codigo)
             if eliminar == 0:
                 print("EL REGISTRO NO SE PUDO ELIMINAR")
             else:
                 print("EL REGISTRO SE ELIMINO")
             print("\n")


         elif opcion == 6:
             print("Adios!!!")

         else:
             print("OPCION NO VALIDA!!!")



menu_principal()