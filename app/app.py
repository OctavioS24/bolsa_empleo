import base64
import io
import os
from PIL import Image
from flask import Flask, render_template, request, make_response
import pdfkit
from validacion import *
from confiDB import coneccionBD



app = Flask(__name__)



@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')


@app.route('/from', methods = ['GET', 'POST'])
def registrarForm():

    global id_datos_personales_global # Accede a la variable global
    global id_datos_formacion_global
    global id_datos_experiencia_global

    if request.method == 'POST':
        msg = ''

        #--------------------Preferencia------------------------

        preferencia = request.form.get('preferencia')

        #--------------------Datos Personales------------------------

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        imagen = request.files['imagen']
        edad = request.form['edad']
        nacimiento = request.form['nacimiento']
        genero = request.form.get('genero')
        correo = request.form['correo']
        calle = request.form['calle']
        numeracion = request.form['numeracion']
        domicilio = f"{calle} {str(numeracion)}"
        confirmar_correo = request.form['confirmar_correo']
        residencia = request.form.get('residencia')
        telefono = request.form['telefono']
        idioma = request.form.get('idioma')
        aptitudes_seleccionadas = request.form.getlist('aptitudes[]')
        
        #--------------------Institucion Educativa------------------------

        institucion = request.form['institucion']
        especialidad = request.form.get('especialidad')
        inicio = request.form['inicio']
        fin = request.form['fin']
        grado = request.form.get('grado')
        notasFormacion = request.form['notasFormacion']

        #--------------------Experiencia Laboral------------------------

        descripcion = request.form['descripcion']
        empresa = request.form['empresa']
        tareas = request.form['tareas']
        desde = request.form['desde']
        hasta = request.form['hasta']
        notasExperiencia = request.form['notasExperiencia']

        #--------------------------------------------
        aptitudes = ', '.join(aptitudes_seleccionadas)

#--------------------Validacion de Preferencia------------------------

        if not validar_preferencia(preferencia):
            error_preferencia = "Debe seleccionar uno"
            return render_template('formulario.html', error_preferencia = error_preferencia, msg='¡Falta completar campos o datos no validos!')

#--------------------Validacion de D.Personales------------------------

        if not validacionNombre(nombre):
            error_nombre = "El nombre no es valido. Debe contener solo letras y menos de 40 caracteres"
            return render_template('formulario.html', error_nombre = error_nombre, msg='¡Falta completar campos o datos no validos!')

        if not validacionApellido(apellido):
            error_apellido = "El apellido no es valido. Debe contener solo letras y menos de 40 caracteres"
            return render_template('formulario.html', error_apellido = error_apellido, msg='¡Falta completar campos o datos no validos!')
        
        if not validacionImagen(imagen):
            error_imagen = "El formato de la imagen no es válido. Debe ser jpg "
            return render_template('formulario.html', error_imagen=error_imagen, msg='¡Falta completar campos o datos no validos!')
        
        if not validar_edad(edad):
            error_edad = "La edad no corresponde. Debe ser mayor de 18 años"
            return render_template('formulario.html', error_edad = error_edad, msg='¡Falta completar campos o datos no validos!')
        
        if not validar_nacimiento(nacimiento):
            error_nacimiento = "La fecha no es correcta"
            return render_template('formulario.html', error_nacimiento = error_nacimiento, msg='¡Falta completar campos o datos no validos!')
        
        if not validar_genero(genero):
            error_genero = "Debe seleccionar uno"
            return render_template('formulario.html', error_genero = error_genero, msg= '¡Falta completar campos o datos no validos!')

        if not validar_correo(correo, confirmar_correo):
            error_correo = "Los correos no coisiden"
            return render_template('formulario.html', error_correo = error_correo, msg='¡Falta completar campos o datos no validos!')
        
        if not validacionCalle(calle):
            error_calle = "La calle no es valido. Debe tener menos de 40 caracteres"
            return render_template('formulario.html', error_calle = error_calle, msg='¡Falta completar campos o datos no validos!')
        
        if not validacionNumeracion(numeracion):
            error_numeracion = "Debe ingresar solo numeros"
            return render_template('formulario.html', error_numeracion = error_numeracion, msg='¡Falta completar campos o datos no validos!')
        
        if not validar_residencia(residencia):
            error_residencia = "Seleccione un Lugar de Residencia"
            return render_template('formulario.html', error_residencia = error_residencia, msg='¡Falta completar campos o datos no validos!')

        if not validar_telefono(telefono):
            error_telefono = "No se permiten caracteres de tipo letras"
            return render_template('formulario.html', error_telefono = error_telefono, msg='¡Falta completar campos o datos no validos!')

        if not validar_idioma(idioma):
            error_idioma = "Selecione uno"
            return render_template('formulario.html', error_idioma=error_idioma, msg='¡Falta completar campos o datos no validos!')

        if not validar_aptitudes(aptitudes):
            error_aptitudes = "Selecione uno"
            return render_template('formulario.html', error_aptitudes=error_aptitudes, msg='¡Falta completar campos o datos no validos!')
        
        #------------------------Validacion de F.Academica--------------------------------

        if not validar_institucion(institucion):
            error_institucion = " Debe contener solo letras y menos de 40 caracteres"
            return render_template('formulario.html', error_institucion = error_institucion, msg='¡Falta completar campos o datos no validos!')

        if not validar_especialidad(especialidad):
            error_especialidad = "Debe seleccionar uno"
            return render_template('formulario.html', error_especialidad = error_especialidad, msg='¡Falta completar campos o datos no validos!')
        
        if not validar_inicio(inicio):
            error_inicio = "La fecha no corresponde. Debe ser desde 1970 en adelante"
            return render_template('formulario.html', error_inicio = error_inicio, msg='¡Falta completar campos o datos no validos!')

        if not validar_fin(inicio, fin):
            error_fin = "La fecha no corresponde. Debe ser mayor a la de inicialización"
            return render_template('formulario.html', error_fin = error_fin, msg='¡Falta completar campos o datos no validos!')
        
        if not validar_grado(grado):
            error_grado = "Debe seleccionar uno"
            return render_template('formulario.html', error_grado = error_grado, msg= '¡Falta completar campos o datos no validos!')
        
        if not validar_notasFormacion(notasFormacion):
            error_notasFormacion = "Debe contener menos de 200 caracteres"
            return render_template('formulario.html', error_notasFormacion = error_notasFormacion, msg='¡Falta completar campos o datos no validos!')
        
        #------------------------Validacion de E.Laboral--------------------------------

        if not validar_descripcion(descripcion):
            error_descripcion = " Debe contener menos de 400 caracteres"
            return render_template('formulario.html', error_descripcion = error_descripcion, msg='¡Falta completar campos o datos no validos!')

        if not validar_Empresa(empresa):
            error_empresa = " Debe contener solo letras y menos de 40 caracteres"
            return render_template('formulario.html', error_empresa = error_empresa, msg='¡Falta completar campos o datos no validos!')
        
        if not validar_tareas(tareas):
            error_tareas = " Debe contener menos de 200 caracteres"
            return render_template('formulario.html', error_tareas = error_tareas, msg='¡Falta completar campos o datos no validos!')
        
        if not validar_desde(desde):
            error_desde = "La fecha no corresponde. Debe ser desde 1970 en adelante"
            return render_template('formulario.html', error_desde = error_desde, msg='¡Falta completar campos o datos no validos!')
        
        if not validar_hasta(desde, hasta):
            error_hasta = "La fecha no corresponde. Debe ser mayor a la de inicialización"
            return render_template('formulario.html', error_hasta = error_hasta, msg='¡Falta completar campos o datos no validos!')
        
        if not validar_notasExperiencia(notasExperiencia):
            error_notasExperiencia = "Debe contener menos de 200 caracteres"
            return render_template('formulario.html', error_notasExperiencia = error_notasExperiencia, msg='¡Falta completar campos o datos no validos!')

        #--------------------------------------------
        # Abrir la imagen con PIL
        imagen_pil = Image.open(imagen)

        # Convertir la imagen en binario en formato JPEG
        buffer_binario = io.BytesIO()
        imagen_pil.save(buffer_binario, format="JPEG")
        imagen_binario = buffer_binario.getvalue()

        #----------------Abrir la Base-----------------

        conexion_MySQLdb = coneccionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)

        #--------------------Insert de D.Personales------------------------

        sql_Datos_Preferencias = "INSERT INTO datos_preferencia (preferencia) VALUES (%s)"
        valores_Datos_Preferencias = (preferencia,)
        cursor.execute(sql_Datos_Preferencias, valores_Datos_Preferencias)
        id_datos_preferencia = cursor.lastrowid # ID de datos_preferencia

        #--------------------Insert de D.Personales------------------------

        sql_Datos_Personales = "INSERT INTO datos_personales (nombre, apellido, imagen, edad, nacimiento, genero, correo, domicilio, residencia, telefono, idioma, aptitudes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores_Datos_Personales = (nombre, apellido, imagen_binario, edad, nacimiento, genero, confirmar_correo, domicilio, residencia, telefono, idioma, aptitudes)
        cursor.execute(sql_Datos_Personales, valores_Datos_Personales)

        id_datos_personales = cursor.lastrowid  # ID de datos_personales
        id_datos_personales_global = id_datos_personales # Guardar en la variable global

        #--------------------Insert de F.Academica------------------------

        sql_Formacion_Academica = "INSERT INTO formacion_academica (institucion, especialidad, inicio, fin, grado, notasFormacion) VALUES (%s, %s, %s, %s, %s, %s)"
        valores_Formacion_Academica = (institucion, especialidad, inicio, fin, grado, notasFormacion)
        cursor.execute(sql_Formacion_Academica, valores_Formacion_Academica)

        id_datos_formacion = cursor.lastrowid  # ID de formacion_academica
        id_datos_formacion_global = id_datos_formacion

        #--------------------Insert de E.Personal-------------------------

        sql_Experiencia_Laboral = "INSERT INTO experiencia_laboral (descripcion, empresa, tareas, desde, hasta, notasExperiencia) VALUES (%s, %s, %s, %s, %s, %s)"
        valores_Experiencia_Laboral = (descripcion, empresa, tareas, desde, hasta, notasExperiencia)
        cursor.execute(sql_Experiencia_Laboral, valores_Experiencia_Laboral)

        id_datos_experiencia = cursor.lastrowid  # ID de experiencia_laboral
        id_datos_experiencia_global = id_datos_experiencia

        #--------------------Insert de curriculums------------------------
        

        print("ID de datos_personales:", id_datos_personales)
        print("ID de formacion_academica:", id_datos_formacion)
        print("ID de experiencia_laboral:", id_datos_experiencia)
        print("ID de datos_preferencia:", id_datos_preferencia)
        

        current_working_directory = os.getcwd()
        ruta_cv = current_working_directory + f"/static/pdfs/{nombre}_{apellido}"
        print(ruta_cv)

        sql_curriculums = "INSERT INTO curriculums(nombre, apellido, curriculo, id_datos_personales, id_datos_formacion, id_datos_experiencia, id_datos_preferencia) VALUES (%s, %s, %s,%s, %s, %s, %s)"
        valores_curriculum = (nombre, apellido, ruta_cv, id_datos_personales, id_datos_formacion, id_datos_experiencia, id_datos_preferencia)
        cursor.execute(sql_curriculums, valores_curriculum)

        conexion_MySQLdb.commit()

        cursor.close() #cerrando conecion SQL
        conexion_MySQLdb.close() # cerrando coneccion de la BD
    

        return render_template("descarga.html", msg='¡Postulación Enviada!')
    else:
        return render_template("formulario.html", msg='¡Error!')


def verificar_notas_formacion_vacias():
    global id_datos_formacion_global
    try:
        conexion_MySQLdb = coneccionBD()
        cursor = conexion_MySQLdb.cursor()
        
        cursor.execute("SELECT notasFormacion FROM formacion_academica WHERE id = %s ORDER BY id DESC LIMIT 1", (id_datos_formacion_global,))
        resultadoFormacion = cursor.fetchone()  # fetchone porque solo esperamos un resultado
        print("Resultado de la consulta:", resultadoFormacion)
        cursor.close()
        conexion_MySQLdb.close()
        
        if resultadoFormacion and resultadoFormacion[0]:  # Comprueba si el resultado no está vacío
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al verificar las notas de formación: {e}")
        return False

def verificar_notas_experiencia_vacias():
    global id_datos_experiencia_global
    try:
        conexion_MySQLdb = coneccionBD()
        cursor = conexion_MySQLdb.cursor()
        
        cursor.execute("SELECT notasExperiencia FROM experiencia_laboral WHERE id = %s ORDER BY id DESC LIMIT 1", (id_datos_experiencia_global,))
        resultadoExperiencia = cursor.fetchone()  # fetchone porque solo esperamos un resultado
        print("Resultado de la consulta:", resultadoExperiencia)
        cursor.close()
        conexion_MySQLdb.close()
        
        if resultadoExperiencia and resultadoExperiencia[0]:  # Comprueba si el resultado no está vacío
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al verificar las notas de formación: {e}")
        return False





@app.route('/descargar_pdf', methods = ['GET', 'POST'])
def descargar_pdf():

    global id_datos_personales_global
    global id_datos_formacion_global
    global id_datos_experiencia_global 

    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

    # Convertir la imagen del logo a base64
    with open(os.path.join(app.root_path, 'static/IMG/logo_mm.jpg'), 'rb') as img_file:
        logo1 = base64.b64encode(img_file.read()).decode('utf-8')

    with open(os.path.join(app.root_path, 'static/IMG/escudo muni.png'), 'rb') as img_file:
        logo2 = base64.b64encode(img_file.read()).decode('utf-8')

    conexion_MySQLdb = coneccionBD()
    cursor           = conexion_MySQLdb.cursor(dictionary=True)

    # Consulta para obtener la fila más reciente de datos_personales
    cursor.execute("SELECT * FROM datos_personales WHERE id = %s ORDER BY id DESC LIMIT 1", (id_datos_personales_global,))
    datos_personales = cursor.fetchone()

    # Convertir la imagen de datos binarios a base64
    imagen_blob = datos_personales['imagen']
    imagen_base64 = base64.b64encode(imagen_blob).decode('utf-8')

    #Obtenemos el nombre y apellido y guardamos en la variable nombre_persona
    nombre_persona = f"{datos_personales['nombre']} {datos_personales['apellido']}"

    # Consulta para obtener la fila más reciente de formacion_academica
    cursor.execute("SELECT * FROM formacion_academica WHERE id = %s ORDER BY id DESC LIMIT 1", (id_datos_formacion_global,))
    formacion_academica = cursor.fetchone()

    # Consulta para obtener la fila más reciente de experiencia_laboral
    cursor.execute("SELECT * FROM experiencia_laboral WHERE id = %s ORDER BY id DESC LIMIT 1", (id_datos_experiencia_global,))
    experiencia_laboral = cursor.fetchone()
    

    notasFormacion_vacias = verificar_notas_formacion_vacias()
    notasExperiencia_vacias = verificar_notas_experiencia_vacias()
    
    # Cerrar cursor y conexión
    cursor.close()
    conexion_MySQLdb.close()


    # Renderiza el HTML con los datos recuperados
    rendered = render_template('pdf_template.html',datos_personales = datos_personales, formacion_academica = formacion_academica, experiencia_laboral = experiencia_laboral, imagen_base64=imagen_base64, notasFormacion_vacias=notasFormacion_vacias, notasExperiencia_vacias=notasExperiencia_vacias, logo1=logo1, logo2=logo2)

    options = {
        'enable-local-file-access': None,
        'page-size': 'A4'
        }

    # Convierte el HTML renderizado a PDF utilizando la configuración proporcionada
    pdf = pdfkit.from_string(rendered, False, configuration=config, options=options)


# Ruta donde se guardará el archivo PDF en la carpeta "static"
    ruta_pdf = os.path.join(app.root_path, 'static/pdfs', f"{nombre_persona}.pdf")

    # Guarda el PDF en la carpeta "static"
    with open(ruta_pdf, 'wb') as archivo_pdf:
        archivo_pdf.write(pdf)


    # Crea una respuesta con el PDF como contenido y el encabezado adecuado
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] =  f'attachment; filename={nombre_persona}_Curriculum.pdf'
    
    return  response

if __name__ == '__main__':
    app.run(debug=True)