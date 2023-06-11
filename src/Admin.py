class Admin:
    def __init__(self, user, password):
        self._user = None
        self._password = None

    #Métodos getters y setters
    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, user):
        self._user = user

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password


    def validar_user(self):
        intentos_user = 4
        intentos_password = 4
        datos_correctos = False #bandera o flag
        self._user = input('Ingresá el nombre de usuario o correo: ')
        
        while not datos_correctos and intentos_user > 0:
            
            if self._user == 'admin' :
                while intentos_password > 0:
                    self._password = input('Ingresá la contraseña: ')
                    if self._password == '12345':
                        datos_correctos = True
                        print('------------------------------------------\nBienvenid@ al sistema de gestión de turnos\n--Ingresaste como usuario administrador--\n------------------------------------------')
                        break #sale del bucle
                    else:
                        intentos_password -= 1 #disminuye la cantidad a 3 intentos restantes
                        print('------------------------------------\n--------Contraseña incorrecta-------\n--------Intentalo nuevamente--------\n------------------------------------')

                        if intentos_password == 0: #si es cero, lo saca del sistema y lo devuelve al menú
                            print('Demasiados intentos..\n       Acceso denegado..\n              ..Saliendo del menú...')
                            break

                        if intentos_password == 1:
                            print(f'Te queda {intentos_password} restante.')
                        else:
                            print(f'Te quedan {intentos_password} intentos restantes.')
    
            else:
                intentos_user -=1
                
                if intentos_user == 0: #si es cero, lo saca del sistema y lo devuelve al menú
                    print('\n---------------------------------\nDemasiados intentos..\n       Acceso denegado..\n              ..Saliendo del menú...')
                    break
                if intentos_user == 1:
                    print(f'Te queda {intentos_user} intento restante.')
                else:
                    print('------------------------------------------------------------')
                    print('Nombre de usuario o correo incorrecto. Intentalo nuevamente')
                    print(f'Te quedan {intentos_user} intentos restantes.')
                self._user = input('----------------------------------------------\nIngresá tu nombre de usuario o correo: ')


            
admin = Admin('', '') #se instancia un objeto vacío de la clase para validar
admin.validar_user() #se llama al método para validar el usuario