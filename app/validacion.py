import re
from datetime import datetime
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

#------------Validacion D.Personales---------------

def validacionNombre(nombre):
    if len(nombre) == 0:  
        return False

    if len(nombre) > 40:
        return False
    
    if not re.match("^[a-zA-Z]+$", nombre.replace(" ", "")):
        return False
    
    return True

def validacionApellido(apellido):
    if len(apellido) == 0:  
        return False

    if len(apellido) > 40:
        return False
    
    if not re.match("^[a-zA-Z]+$", apellido.replace(" ", "")):
        return False
    
    return True

def validacionImagen(imagen):
    if '.' not in imagen.filename:
        return False
    extension = imagen.filename.rsplit('.', 1)[1].lower()
    if extension != 'jpg':
        return False
    
    return True


def validar_edad(edad):
    if len(edad) == 0:  
        return False
    
    try:
        edad = int(edad)
        if 18 <= edad <= 120:
            return True
        else:
            return False
    except ValueError:
        return False

def validar_nacimiento(fecha_str):
    if len(fecha_str) == 0:  
        return False

    try:
        # Intenta convertir la cadena de fecha al formato especificado
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
        # Verifica si la fecha es válida
        if fecha.year < 1920 or fecha.date() > datetime.now().date():
            return False
        return True
    except ValueError:
        return False

def validar_genero(genero):
    # Verificar si al menos una opción de género ha sido seleccionada
    if genero:
        return True  # Al menos una opción de género ha sido seleccionada
    else:
        return False 

def validar_correo(correo, confirmar_correo):
    if len(correo) == 0 or len(confirmar_correo) == 0: 
        return False

    if correo == confirmar_correo:
        return True
    else:
        return False

def validacionCalle(calle):
    if len(calle) == 0:  
        return False

    if len(calle) > 80:
        return False
    
    return True

def validacionNumeracion(numeracion):
    if numeracion.isdigit():  # Verifica si todos los caracteres son dígitos
        return True
    else:
        return False


def validar_residencia(residencia):
    if residencia is None or residencia == "":
        return False
    return True


def validar_telefono(telefono):
    # Remover todos los caracteres que no sean dígitos
    solo_digitos = re.sub(r'\D', '', telefono)
    
    # Comprobar que la longitud sea exactamente 10
    if len(solo_digitos) == 10:
        return True
    else:
        return False
    


def validar_idioma(idioma):
    # Verificar si al menos una opción de género ha sido seleccionada
    if idioma:
        return True  # Al menos una opción de género ha sido seleccionada
    else:
        return False 

def validar_aptitudes(aptitudes):
    if len(aptitudes) > 0:
        return True
    else:
        return False

#------------Validacion E.Laboral---------------

def validar_descripcion(descripcion):
    if len(descripcion) == 0:  
        return False

    if len(descripcion) <= 100:
        return True
    else:
        return False

def validar_Empresa(empresa):
    if len(empresa) == 0:  
        return False
    
    if len(empresa) > 40:
        return False
    
    if not re.match("^[a-zA-Z]+$", empresa.replace(" ", "")):
        return False
    
    return True

def validar_tareas(tareas):
    if len(tareas) == 0:  
        return False

    if len(tareas) <= 200:
        return True
    else:
        return False

def validar_desde(desde):
    if len(desde) == 0:  
        return False
    
    try:
        fecha = datetime.strptime(desde, '%Y-%m-%d')
        if fecha.year < 1970 or fecha.date() > datetime.now().date():
            return False
        return True
    except ValueError:
        return False

def validar_hasta(desde, hasta):
    if len(hasta) == 0:  
        return False
    
    try:
        fecha_desde = datetime.strptime(desde, '%Y-%m-%d')
        fecha_hasta = datetime.strptime(hasta, '%Y-%m-%d')
        if fecha_hasta.year < 1971 or fecha_hasta.date() > datetime.now().date():
            return False
        if fecha_hasta <= fecha_desde:
            return False
        return True
    except ValueError:
        return False


def validar_notasExperiencia(notasExperiencia):

    if len(notasExperiencia) <= 200:
        return True
    else:
        return False

#------------Validacion F.Academica---------------

def validar_institucion(institucion):
    if len(institucion) == 0:  
        return False
    
    if len(institucion) <= 40:
        return True
    else:
        return False

def validar_especialidad(especialidad):
    if especialidad is None or especialidad == "":
        return False
    return True

def validar_inicio(inicio):
    if len(inicio) == 0:  
        return False
    
    try:
        fecha = datetime.strptime(inicio, '%Y-%m-%d')
        if fecha.year < 1970 or fecha.date() > datetime.now().date():
            return False
        return True
    except ValueError:
        return False

def validar_fin(inicio, fin):
    if len(fin) == 0:  
        return False
    
    try:
        fecha_inicio = datetime.strptime(inicio, '%Y-%m-%d')
        fecha_fin = datetime.strptime(fin, '%Y-%m-%d')
        if fecha_fin.year < 1971 or fecha_fin.date() > datetime.now().date():
            return False
        if fecha_fin <= fecha_inicio:
            return False
        return True
    except ValueError:
        return False
    
def validar_grado(grado):
    # Verificar si al menos una opción de género ha sido seleccionada
    if grado:
        return True  # Al menos una opción de género ha sido seleccionada
    else:
        return False

def validar_notasFormacion(notasFormacion):
    
    if len(notasFormacion) <= 200:
        return True
    else:
        return False
    