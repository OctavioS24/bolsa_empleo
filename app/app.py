import base64
import io
import os
from PIL import Image
from flask import Flask, render_template, request, make_response, session
import pdfkit
from confiDB import coneccionBD

app = Flask(__name__)
app.secret_key = 'octavio123'  # Cambia esta clave secreta a una adecuada para tu entorno

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/from', methods=['GET', 'POST'])
def registrarForm():
    if request.method == 'POST':
        #--------------------Preferencia------------------------
        preferencia = request.form.get('preferencia')

        #--------------------Datos Personales------------------------
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        imagen = request.files['imagen']
        edad = request.form['edad']
        nacimiento = request.form['fecha-nacimiento']
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

        #--------------------------------------------
        # Abrir la imagen con PIL
        imagen_pil = Image.open(imagen)

        # Convertir la imagen en binario en formato JPEG
        buffer_binario = io.BytesIO()
        imagen_pil.save(buffer_binario, format="JPEG")
        imagen_binario = buffer_binario.getvalue()

        #----------------Abrir la Base-----------------
        conexion_MySQLdb = coneccionBD()
        cursor = conexion_MySQLdb.cursor()

        #--------------------Insert de D.Personales------------------------
        sql_Datos_Preferencias = "INSERT INTO datos_preferencia (preferencia) VALUES (%s)"
        valores_Datos_Preferencias = (preferencia,)
        cursor.execute(sql_Datos_Preferencias, valores_Datos_Preferencias)
        id_datos_preferencia = cursor.lastrowid

        #--------------------Insert de D.Personales------------------------
        sql_Datos_Personales = "INSERT INTO datos_personales (nombre, apellido, imagen, edad, nacimiento, genero, correo, domicilio, residencia, telefono, idioma, aptitudes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores_Datos_Personales = (nombre, apellido, imagen_binario, edad, nacimiento, genero, confirmar_correo, domicilio, residencia, telefono, idioma, aptitudes)
        cursor.execute(sql_Datos_Personales, valores_Datos_Personales)
        id_datos_personales = cursor.lastrowid

        #--------------------Insert de F.Academica------------------------
        sql_Formacion_Academica = "INSERT INTO formacion_academica (institucion, especialidad, inicio, fin, grado, notasFormacion) VALUES (%s, %s, %s, %s, %s, %s)"
        valores_Formacion_Academica = (institucion, especialidad, inicio, fin, grado, notasFormacion)
        cursor.execute(sql_Formacion_Academica, valores_Formacion_Academica)
        id_datos_formacion = cursor.lastrowid

        #--------------------Insert de E.Personal-------------------------
        sql_Experiencia_Laboral = "INSERT INTO experiencia_laboral (descripcion, empresa, tareas, desde, hasta, notasExperiencia) VALUES (%s, %s, %s, %s, %s, %s)"
        valores_Experiencia_Laboral = (descripcion, empresa, tareas, desde, hasta, notasExperiencia)
        cursor.execute(sql_Experiencia_Laboral, valores_Experiencia_Laboral)
        id_datos_experiencia = cursor.lastrowid

        #--------------------Insert de curriculums------------------------
        current_working_directory = os.getcwd()
        ruta_cv = os.path.join(current_working_directory, f"static/pdfs/{nombre}_{apellido}.pdf")

        sql_curriculums = "INSERT INTO curriculums (nombre, apellido, curriculo, id_datos_personales, id_datos_formacion, id_datos_experiencia, id_datos_preferencia) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores_curriculum = (nombre, apellido, ruta_cv, id_datos_personales, id_datos_formacion, id_datos_experiencia, id_datos_preferencia)
        cursor.execute(sql_curriculums, valores_curriculum)

        conexion_MySQLdb.commit()
        cursor.close()
        conexion_MySQLdb.close()

        # Guardar IDs en la sesión
        session['id_datos_personales'] = id_datos_personales
        session['id_datos_formacion'] = id_datos_formacion
        session['id_datos_experiencia'] = id_datos_experiencia

        # Debugging: Verifica los valores en la sesión
        print(f"ID Datos Personales Guardado en Sesión: {session.get('id_datos_personales')}")
        print(f"ID Datos Formacion Guardado en Sesión: {session.get('id_datos_formacion')}")
        print(f"ID Datos Experiencia Guardado en Sesión: {session.get('id_datos_experiencia')}")

        return render_template("descarga.html", msg='¡Postulación Enviada!')
    else:
        return render_template("formulario.html", msg='¡Error!')

def verificar_notas_formacion_vacias(id_datos_formacion):
    try:
        conexion_MySQLdb = coneccionBD()
        cursor = conexion_MySQLdb.cursor()

        cursor.execute("SELECT notasFormacion FROM formacion_academica WHERE id = %s", (id_datos_formacion,))
        resultadoFormacion = cursor.fetchone()
        cursor.close()
        conexion_MySQLdb.close()

        if resultadoFormacion and resultadoFormacion[0]:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al verificar las notas de formación: {e}")
        return False

def verificar_notas_experiencia_vacias(id_datos_experiencia):
    try:
        conexion_MySQLdb = coneccionBD()
        cursor = conexion_MySQLdb.cursor()

        cursor.execute("SELECT notasExperiencia FROM experiencia_laboral WHERE id = %s", (id_datos_experiencia,))
        resultadoExperiencia = cursor.fetchone()
        cursor.close()
        conexion_MySQLdb.close()

        if resultadoExperiencia and resultadoExperiencia[0]:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al verificar las notas de experiencia: {e}")
        return False
    


@app.route('/descargar_pdf', methods=['GET', 'POST'])
def descargar_pdf():
    try:


        id_datos_personales_global = session.get('id_datos_personales')
        id_datos_formacion_global = session.get('id_datos_formacion')
        id_datos_experiencia_global = session.get('id_datos_experiencia')

        print(f"ID Datos Personales: {session.get('id_datos_personales')}")
        print(f"ID Datos Formacion: {session.get('id_datos_formacion')}")
        print(f"ID Datos Experiencia: {session.get('id_datos_experiencia')}")

        if id_datos_personales_global is None:
            return "Error: El ID de datos personales no está definido.", 500

        config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

        # Convertir la imagen del logo a base64
        with open(os.path.join(app.root_path, 'static/IMG/logo_mm.jpg'), 'rb') as img_file:
            logo1 = base64.b64encode(img_file.read()).decode('utf-8')

        with open(os.path.join(app.root_path, 'static/IMG/escudo_muni.png'), 'rb') as img_file:
            logo2 = base64.b64encode(img_file.read()).decode('utf-8')

        conexion_MySQLdb = coneccionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)

        # Consulta para obtener la fila más reciente de datos_personales
        cursor.execute("SELECT * FROM datos_personales WHERE id = %s", (id_datos_personales_global,))
        datos_personales = cursor.fetchone()

        if datos_personales is None:
            return "No se encontraron datos personales.", 404

        if 'imagen' in datos_personales and datos_personales['imagen'] is not None:
            imagen_blob = datos_personales['imagen']
            imagen_base64 = base64.b64encode(imagen_blob).decode('utf-8')
        else:
            return "No se encontró la imagen de datos personales.", 404

        # Obtener nombre y apellido
        nombre_persona = f"{datos_personales['nombre']} {datos_personales['apellido']}"

        # Consulta para obtener la fila más reciente de formacion_academica
        cursor.execute("SELECT * FROM formacion_academica WHERE id = %s", (id_datos_formacion_global,))
        formacion_academica = cursor.fetchone()

        # Consulta para obtener la fila más reciente de experiencia_laboral
        cursor.execute("SELECT * FROM experiencia_laboral WHERE id = %s", (id_datos_experiencia_global,))
        experiencia_laboral = cursor.fetchone()

        notasFormacion_vacias = verificar_notas_formacion_vacias(id_datos_formacion_global)
        notasExperiencia_vacias = verificar_notas_experiencia_vacias(id_datos_experiencia_global)

        # Cerrar cursor y conexión
        cursor.close()
        conexion_MySQLdb.close()

        # Renderiza el HTML con los datos recuperados
        rendered = render_template('pdf_template.html',
            datos_personales=datos_personales,
            formacion_academica=formacion_academica,
            experiencia_laboral=experiencia_laboral,
            imagen_base64=imagen_base64,
            notasFormacion_vacias=notasFormacion_vacias,
            notasExperiencia_vacias=notasExperiencia_vacias,
            logo1=logo1,
            logo2=logo2
        )

        options = {
            'enable-local-file-access': None,
            'page-size': 'A4'
        }

        # Convierte el HTML renderizado a PDF
        pdf = pdfkit.from_string(rendered, False, configuration=config, options=options)

        # Ruta donde se guardará el archivo PDF en la carpeta "static"
        ruta_pdf = os.path.join(app.root_path, 'static/pdfs', f"{nombre_persona}.pdf")

        # Guarda el PDF en la carpeta "static"
        with open(ruta_pdf, 'wb') as archivo_pdf:
            archivo_pdf.write(pdf)

        # Crea una respuesta con el PDF como contenido y el encabezado adecuado
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename={nombre_persona}_Curriculum.pdf'
        
        return response
    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True)
