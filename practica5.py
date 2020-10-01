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

              return True
              self.cursos.close()
              self.conexion.close()
             

          except ConnectionError as err:
              self.conexion.rollback('SU REGISTRO NO ES VALIDO')
              return err


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


         except  ConnectionError  as err:
             return err




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
            return True



         except Exception as err:
             self.conexion.rollback()
             print("Este nombre no esta en el registro")
             return err
            



     #metodo Actualizar
     def Actualizar(self,telefono,nom):
         sql = "UPDATE agendatel SET telefono = '{}' WHERE id = '{}'".format(telefono, id)
         try:
             self.cursos.execute(sql)
             self.conexion.commit()
             print("El registro se actualizo")
             return True
             self.cursos.close()
             self.conexion.close()

         except Exception as err:
             self.conexion.rollback("NO se PUDO ACTUALIZAR EL REGISTRO!!!")
             return err

             


     #metodo eliminar
     def Eliminar(self,codigoid):

         sql = " DELETE FROM agendatel WHERE idcod = {}".format(codigoid)

         try:
             self.cursos.execute(sql)
             self.conexion.commit()
             print('EL REGISTRO SE A ELIMINADO CORRECTAMENTE!!!')
             return True
         
             self.cursos.close()
             self.conexion.close()
             

         except Exception as err:
             self.conexion.rollback()
             print('EL REGISTRO NO SE PUDO ELIMINAR!!!')
             return err

             
             







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
         print('\tWELCOME AGENDA TELEFONICA\n')

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
                 agrega= database.Agregar(id,nombre,apellido,telefono,direccion)
                 if agrega == 0:
                      print("EL REGISTRO NO SE PUDO AGREGAR")
                 else:
                      print("EL REGISTRO SE AGREGO CORRECTAMENTE")
                 print("\n")
                 agregar = input("DESEA AGREGAR OTRO REGISTRO(SI/NO)?: ")
           
                 

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
             
             idcod = str(input('Digita id del registro a Actualizar: '))
             database.Mostrar(idcod)
             clear()
             print("\n")

             cell = input('Telefono: ')

             actualizar = database.Actualizar(cell , idcod)
             if actualizar == 0:
                 print("EL REGISTRO NO SE PUDO ACTUALIZAR")
             else:
                 print("EL REGISTRO SE ACTUALIZO CORRECTAMENTE")


         elif opcion == 5:

             codigo = str(input('INTRODUZCA EL ID DEL REGISTRO: '))
             eliminar = database.Eliminar(codigo)
           
            
             print("\n")


         elif opcion == 6:
             print("Adios!!!")

         else:
             print("OPCION NO VALIDA!!!")



menu_principal()