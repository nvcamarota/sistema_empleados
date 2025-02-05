"""
SISTEMA DE EMPLEADOS
Crea una superclase Empleado con:
• Un atributo nombre.
• Un método mostrar_info() que imprime el nombre del empleado.

Crear las siguientes subclases:
• Profesor: Agrega un atributo materia y modifica mostrar_info() para incluir la materia que enseña.
• Desarrollador: Agrega un atributo lengüaje y muestra qué lengüaje programa.
• Doctor: Agrega un atributo especialidad y muestra en qué se especializa.

Objetivo: Implementa la herencia correctamente.
• Usa super().__init__ para reutilizar código.
• Crea una lista con varios empleados y muestra su información.
"""

# Superclase Empleado
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre.title()
    
    def mostrar_info(self):
        return f'Nombre del empleado: {self.nombre}.'
    
# Subclase Profesor - Contiene el atributo nombre de la superclase Empleado y el atributo materia de esta subclase
class Profesor(Empleado):
    def __init__(self, nombre, materia):
        super().__init__(nombre)
        self.materia = materia.capitalize()

# Reutiliza la función mostrar_info() de la superclase Empleado más un mensaje personalizado para esta subclase
    def mostrar_info(self):
        return f'{super().mostrar_info()}\n{self.nombre} enseña {self.materia} a sus estudiantes.\n'

# Subclase Desarrollador - Contiene el atributo nombre de la superclase Empleado y el atributo lengüaje de esta subclase
class Desarrollador(Empleado):
    def __init__(self, nombre, lengüaje):
        super().__init__(nombre)
        self.lengüaje = lengüaje.capitalize()
  
# Reutiliza la función mostrar_info() de la superclase Empleado más un mensaje personalizado para esta subclase 
    def mostrar_info(self):
        return f'{super().mostrar_info()}\n{self.nombre} sabe programar en {self.lengüaje}.\n'
    
# Subclase Doctor - Contiene el atributo nombre de la superclase Empleado y el atributo especialidad de esta subclase
class Doctor(Empleado):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre)
        self.especialidad = especialidad.capitalize()
        
# Reutiliza la función mostrar_info() de la superclase Empleado más un mensaje personalizado para esta subclase
    def mostrar_info(self):
        return f'{super().mostrar_info()}\n{self.nombre} se especializa en {self.especialidad}.\n'
    
# Función que contiene un título principal y una lista de empleados utilizando la lógica de las subclases
def listado_personal():
    print('Listado de empleados:\n')
    return [
        Profesor('Rodrigo Pérez', 'Matemática'),
        Desarrollador('Eric Mena', 'JavaScript'),
        Doctor('Mayra Miranda', 'Radiología')
    ]
    
# Bucle que recorre el listado de empleados de la función listado_personal() e imprime su respectiva información
for persona in listado_personal():
    print(persona.mostrar_info())

# Mensaje de cierre
print('Cerrando "Sistema de empleados". ¡Hasta la próxima! 👋')