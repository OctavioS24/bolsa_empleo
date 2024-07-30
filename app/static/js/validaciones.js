document.addEventListener("DOMContentLoaded", function() {
    //--------------------Validacion Preferencia-----------------------

    const preferenciaSelect = document.getElementById('preferencia');
    const errorPreferencia = document.getElementById('error-preferencia');
    const btnSiguienteForm1 = document.getElementById('btn-siguiente-form1');

    // Evento para validar cuando el usuario intenta avanzar
    btnSiguienteForm1.addEventListener('click', function(event) {
        if (!validateForm()) {
            event.preventDefault(); // Evita que el formulario avance si hay un error
        }
    });

    // Mostrar el error cuando el usuario interactúe con el select
    preferenciaSelect.addEventListener('change', function() {
        validateForm(); // Valida al cambiar la selección
    });

    preferenciaSelect.addEventListener('focus', function() {
        // Muestra el mensaje de error si la opción seleccionada no es válida
        if (!preferenciaSelect.value || preferenciaSelect.value === 'selecciona') {
            preferenciaSelect.classList.add('error');
            errorPreferencia.textContent = 'Por favor, selecciona una preferencia laboral válida';
        }
    });

    function validateForm() {
        const preferenciaValue = preferenciaSelect.value;

        // Validación para la opción predeterminada
        if (!preferenciaValue || preferenciaValue === 'selecciona') {
            preferenciaSelect.classList.add('error');
            errorPreferencia.textContent = 'Por favor, selecciona una preferencia laboral válida';
            btnSiguienteForm1.disabled = true;
            return false; // Indica que hay un error
        } else {
            preferenciaSelect.classList.remove('error');
            errorPreferencia.textContent = '';
            btnSiguienteForm1.disabled = false;
            return true; // Indica que la validación fue exitosa
        }
    }
});


document.addEventListener("DOMContentLoaded", function() {
    // Obtener elementos del DOM para Formulario 1
    const nombreInput = document.getElementById("nombre");
    const apellidoInput = document.getElementById("apellido");
    const edadInput = document.getElementById("edad");
    const fechaNacimientoInput = document.getElementById("fecha-nacimiento");
    const generoRadios = document.querySelectorAll('input[name="genero"]');
    const correoInput = document.getElementById("correo");
    const confirmarCorreoInput = document.getElementById("confirmar_correo");
    const calleInput = document.getElementById("calle");
    const numeroInput = document.getElementById("numeracion");
    const residenciaSelect = document.getElementById('residencia');
    const telefonoInput = document.getElementById("telefono");
    const imagenInput = document.getElementById("imagen");
    const idiomaRadios = document.querySelectorAll('input[name="idioma"]');
    const btnSiguienteForm2 = document.getElementById('btn-siguiente-form2');

    // Obtener elementos del DOM para Formulario 2
    const institucionInput = document.getElementById("institucion");
    const especialidadSelect = document.getElementById('especialidad');
    const inicioInput = document.getElementById("inicio");
    const finInput = document.getElementById("fin");
    const gradoRadios = document.querySelectorAll('input[name="grado"]');
    const btnSiguienteForm3 = document.getElementById('btn-siguiente-form3');

    // Elementos para mostrar errores para Formulario 1
    const errorNombre = document.getElementById("error-nombre");
    const errorApellido = document.getElementById("error-apellido");
    const errorEdad = document.getElementById("error-edad");
    const errorFecha = document.getElementById("error-fecha");
    const errorGenero = document.getElementById('error-genero');
    const errorCorreo = document.getElementById("error-correo");
    const errorCalle = document.getElementById("error-calle");
    const errorNumero = document.getElementById("error-numeracion");
    const errorResidencia = document.getElementById('error-residencia');
    const errorTelefono = document.getElementById("error-telefono");
    const errorImagen = document.getElementById("error-imagen");
    const errorIdioma = document.getElementById("error-idioma");

    // Elementos para mostrar errores para Formulario 2
    const errorInstitucion = document.getElementById("error-institucion");
    const errorEspecialidad = document.getElementById('error-especialidad');
    const errorInicio = document.getElementById("error-inicio");
    const errorFin = document.getElementById("error-fin");
    const errorFormacion = document.getElementById('error-formacion');

    // Agregar event listeners para Formulario 1
    nombreInput.addEventListener("input", validateNombre);
    apellidoInput.addEventListener("input", validateApellido);
    edadInput.addEventListener("input", validateEdad);
    fechaNacimientoInput.addEventListener("input", validateFechaNacimiento);
    generoRadios.forEach(radio => radio.addEventListener('change', validateGenero));
    correoInput.addEventListener("input", validateCorreo);
    confirmarCorreoInput.addEventListener("input", validateCorreo);
    calleInput.addEventListener("input", validateCalle);
    numeroInput.addEventListener("input", validateNumero);
    residenciaSelect.addEventListener('input', validateResidencia);
    telefonoInput.addEventListener("input", validateTelefono);
    imagenInput.addEventListener("change", validateImagen);
    idiomaRadios.forEach(radio => radio.addEventListener('change', validateIdioma));

    // Agregar event listeners para Formulario 2
    institucionInput.addEventListener("input", validateInstitucion);
    especialidadSelect.addEventListener('change', validateEspecialidad);
    inicioInput.addEventListener("input", validateInicio);
    finInput.addEventListener("input", validateFin);
    gradoRadios.forEach(radio => radio.addEventListener('change', validateFormacion));

    // Funciones de validación para Formulario 1
    function validateNombre() { 
        const nombreValue = nombreInput.value.trim();
        if (!nombreValue) {
            nombreInput.classList.add("error");
            errorNombre.textContent = "Este campo es obligatorio";
        } else if (nombreValue.length < 2) {
            nombreInput.classList.add("error");
            errorNombre.textContent = "El nombre debe tener al menos 2 caracteres";
        } else if (!/^[a-zA-Z\sáéíóúÁÉÍÓÚñÑ]+$/.test(nombreValue)) {
            nombreInput.classList.add("error");
            errorNombre.textContent = "Por favor, ingrese solo letras y espacios";
        } else {
            nombreInput.classList.remove("error");
            errorNombre.textContent = "";
        }
        checkForm1Validity();
    }

    function validateApellido() {
        const apellidoValue = apellidoInput.value.trim();
        if (!apellidoValue) {
            apellidoInput.classList.add("error");
            errorApellido.textContent = "Este campo es obligatorio";
        } else if (apellidoValue.length < 2) {
            apellidoInput.classList.add("error");
            errorApellido.textContent = "El apellido debe tener al menos 2 caracteres";
        } else if (!/^[a-zA-Z\sáéíóúÁÉÍÓÚñÑ]+$/.test(apellidoValue)) {
            apellidoInput.classList.add("error");
            errorApellido.textContent = "Por favor, ingrese solo letras y espacios";
        } else {
            apellidoInput.classList.remove("error");
            errorApellido.textContent = "";
        }
        checkForm1Validity();
    }

    function validateEdad() {
        const edadValue = edadInput.value.trim();
        if (!edadValue || isNaN(edadValue) || edadValue < 18 || edadValue > 120) {
            edadInput.classList.add("error");
            errorEdad.textContent = "Ingrese una edad válida (entre 18 y 120 años)";
        } else {
            edadInput.classList.remove("error");
            errorEdad.textContent = "";
        }
        checkForm1Validity();
    }

    function validateFechaNacimiento() {
        const fechaNacimientoValue = fechaNacimientoInput.value.trim();
        if (!fechaNacimientoValue) {
            fechaNacimientoInput.classList.add("error");
            errorFecha.textContent = "Este campo es obligatorio";
        } else {
            const fechaNacimiento = new Date(fechaNacimientoValue);
            const fechaLimiteMenor = new Date();
            fechaLimiteMenor.setFullYear(fechaLimiteMenor.getFullYear() - 18); // 18 años atrás desde la fecha actual
            const fechaLimiteMayor = new Date();
            fechaLimiteMayor.setFullYear(fechaLimiteMayor.getFullYear() - 80); // 80 años atrás desde la fecha actual

            if (fechaNacimiento < fechaLimiteMayor || fechaNacimiento > fechaLimiteMenor) {
                fechaNacimientoInput.classList.add("error");
                errorFecha.textContent = "La fecha debe ser mayor a 18 años y menor a 80 años";
            } else {
                fechaNacimientoInput.classList.remove("error");
                errorFecha.textContent = "";
            }
        }
        checkForm1Validity();
    }

    function validateGenero() {
        let selected = Array.from(generoRadios).some(radio => radio.checked);

        if (!selected) {
            errorGenero.textContent = 'Por favor, selecciona una opción de género';
        } else {
            errorGenero.textContent = '';
        }
        checkForm1Validity();
    }

    function validateCorreo() {
        const correoValue = correoInput.value.trim();
        const confirmarCorreoValue = confirmarCorreoInput.value.trim();

        if (!correoValue || !isValidEmail(correoValue)) {
            correoInput.classList.add("error");
            errorCorreo.textContent = "Ingrese un correo electrónico válido";
        } else if (correoValue !== confirmarCorreoValue) {
            confirmarCorreoInput.classList.add("error");
            errorCorreo.textContent = "Los correos electrónicos no coinciden";
        } else {
            correoInput.classList.remove("error");
            confirmarCorreoInput.classList.remove("error");
            errorCorreo.textContent = "";
        }
        checkForm1Validity();
    }

    function validateCalle() {
        const calleValue = calleInput.value.trim();
        if (!calleValue) {
            calleInput.classList.add("error");
            errorCalle.textContent = "Este campo es obligatorio";
        } else {
            calleInput.classList.remove("error");
            errorCalle.textContent = "";
        }
        checkForm1Validity();
    }

    function validateNumero() {
        const numeroValue = numeroInput.value.trim();
        if (!numeroValue || isNaN(numeroValue)) {
            numeroInput.classList.add("error");
            errorNumero.textContent = "Ingrese un número válido";
        } else {
            numeroInput.classList.remove("error");
            errorNumero.textContent = "";
        }
        checkForm1Validity();
    }

    function validateResidencia() {
        const residenciaValue = residenciaSelect.value;

        if (!residenciaValue) {
            residenciaSelect.classList.add('error');
            errorResidencia.textContent = 'Por favor, selecciona tu lugar de residencia';
        } else {
            residenciaSelect.classList.remove('error');
            errorResidencia.textContent = '';
        }
        checkForm1Validity();
    }

    function validateTelefono() {
        const telefonoValue = telefonoInput.value.trim();
        if (!telefonoValue || telefonoValue.length !== 10 || isNaN(telefonoValue)) {
            telefonoInput.classList.add("error");
            errorTelefono.textContent = "Ingrese un número de teléfono válido (10 dígitos)";
        } else {
            telefonoInput.classList.remove("error");
            errorTelefono.textContent = "";
        }
        checkForm1Validity();
    }

    function validateImagen() {
        const imagenValue = imagenInput.files[0];
        if (!imagenValue || imagenValue.type !== 'image/jpeg') {
            imagenInput.classList.add("error");
            errorImagen.textContent = "Por favor, sube una imagen en formato JPG";
        } else {
            imagenInput.classList.remove("error");
            errorImagen.textContent = "";
        }
        checkForm1Validity();
    }

    function validateIdioma() {
        const idiomaSeleccionado = Array.from(idiomaRadios).some(radio => radio.checked);
        if (!idiomaSeleccionado) {
            errorIdioma.textContent = 'Por favor, selecciona un idioma';
        } else {
            errorIdioma.textContent = '';
        }
        checkForm1Validity();
    }

    function isValidEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    function checkForm1Validity() {
        const nombreValido = nombreInput.value.trim() && nombreInput.value.length >= 2 && /^[a-zA-Z\sáéíóúÁÉÍÓÚñÑ]+$/.test(nombreInput.value.trim());
        const apellidoValido = apellidoInput.value.trim() && apellidoInput.value.length >= 2 && /^[a-zA-Z\sáéíóúÁÉÍÓÚñÑ]+$/.test(apellidoInput.value.trim());
        const edadValida = edadInput.value.trim() && !isNaN(edadInput.value.trim()) && edadInput.value.trim() >= 18 && edadInput.value.trim() <= 120;
        const fechaNacimientoValida = fechaNacimientoInput.value.trim() && (function() {
            const fechaNacimiento = new Date(fechaNacimientoInput.value.trim());
            const fechaLimiteMenor = new Date();
            fechaLimiteMenor.setFullYear(fechaLimiteMenor.getFullYear() - 18);
            const fechaLimiteMayor = new Date();
            fechaLimiteMayor.setFullYear(fechaLimiteMayor.getFullYear() - 80);
            return fechaNacimiento >= fechaLimiteMayor && fechaNacimiento <= fechaLimiteMenor;
        })();
        const generoValido = Array.from(generoRadios).some(radio => radio.checked);
        const correoValido = correoInput.value.trim() && isValidEmail(correoInput.value.trim()) && correoInput.value.trim() === confirmarCorreoInput.value.trim();
        const calleValida = calleInput.value.trim();
        const numeroValido = numeroInput.value.trim() && !isNaN(numeroInput.value.trim());
        const residenciaValida = residenciaSelect.value;
        const telefonoValido = telefonoInput.value.trim() && telefonoInput.value.trim().length === 10 && !isNaN(telefonoInput.value.trim());
        const imagenValida = imagenInput.files.length > 0 && imagenInput.files[0].type === 'image/jpeg';
        const idiomaValido = Array.from(idiomaRadios).some(radio => radio.checked);

        if (nombreValido && apellidoValido && edadValida && fechaNacimientoValida && generoValido && correoValido && calleValida && numeroValido && residenciaValida && telefonoValido && imagenValida && idiomaValido) {
            btnSiguienteForm2.disabled = false;
        } else {
            btnSiguienteForm2.disabled = true;
        }
    }

    // Funciones de validación para Formulario 2
    function validateInstitucion() {
        const institucionValue = institucionInput.value.trim();
        if (!institucionValue) {
            institucionInput.classList.add("error");
            errorInstitucion.textContent = "Este campo es obligatorio";
        } else {
            institucionInput.classList.remove("error");
            errorInstitucion.textContent = "";
        }
        checkForm3Validity();
    }

    function validateEspecialidad() {
        const especialidadValue = especialidadSelect.value;
        if (!especialidadValue) {
            especialidadSelect.classList.add('error');
            errorEspecialidad.textContent = 'Por favor, selecciona una especialidad';
        } else {
            especialidadSelect.classList.remove('error');
            errorEspecialidad.textContent = '';
        }
        checkForm3Validity();
    }

    function validateInicio() {
        const inicioValue = inicioInput.value;
        if (!inicioValue) {
            inicioInput.classList.add("error");
            errorInicio.textContent = "Este campo es obligatorio";
        } else {
            const fechaInicio = new Date(inicioValue);
            const fechaLimite = new Date("1880-12-31");
            if (fechaInicio <= fechaLimite) {
                inicioInput.classList.add("error");
                errorInicio.textContent = "La fecha debe ser posterior a 1880";
            } else {
                inicioInput.classList.remove("error");
                errorInicio.textContent = "";
            }
        }
        validateFin(); // Validar fin después de inicio
        checkForm3Validity();
    }

    function validateFin() {
        const finValue = finInput.value;
        if (!finValue) {
            finInput.classList.add("error");
            errorFin.textContent = "Este campo es obligatorio";
        } else {
            const fechaFin = new Date(finValue);
            const fechaLimite = new Date("1881-01-01");
            if (fechaFin < fechaLimite) {
                finInput.classList.add("error");
                errorFin.textContent = "La fecha debe ser posterior o igual a 1881";
            } else {
                finInput.classList.remove("error");
                errorFin.textContent = "";
                // Validar la relación entre inicio y fin
                const inicioValue = inicioInput.value;
                if (inicioValue && fechaFin <= new Date(inicioValue)) {
                    finInput.classList.add("error");
                    errorFin.textContent = "La fecha de fin debe ser mayor que la fecha de inicio";
                } else {
                    finInput.classList.remove("error");
                    errorFin.textContent = "";
                }
            }
        }
        checkForm3Validity();
    }

    function validateFormacion() {
        const selected = Array.from(gradoRadios).some(radio => radio.checked);
        if (!selected) {
            errorFormacion.textContent = 'Por favor, selecciona una opción de formación académica';
        } else {
            errorFormacion.textContent = '';
        }
        checkForm3Validity();
    }

    function checkForm3Validity() {
        const institucionValida = institucionInput.value.trim() !== "";
        const especialidadValida = especialidadSelect.value !== "";
        const inicioValido = inicioInput.value.trim() !== "" && new Date(inicioInput.value.trim()) > new Date("1880-12-31");
        const finValido = finInput.value.trim() !== "" && new Date(finInput.value.trim()) >= new Date("1881-01-01") &&
            (inicioInput.value.trim() === "" || new Date(finInput.value.trim()) > new Date(inicioInput.value.trim()));
        const formacionValida = Array.from(gradoRadios).some(radio => radio.checked);

        if (institucionValida && especialidadValida && inicioValido && finValido && formacionValida) {
            btnSiguienteForm3.disabled = false;
        } else {
            btnSiguienteForm3.disabled = true;
        }
    }

    // Inicializa la validación al cargar la página
    checkForm1Validity();
    checkForm3Validity();
});


document.addEventListener("DOMContentLoaded", function() {
    // Obtener elementos del DOM para Formulario 3
    const empresaInput = document.getElementById("empresa");
    const descripcionInput = document.getElementById("descripcion");
    const tareasTextarea = document.getElementById('tareas');
    const desdeInput = document.getElementById("desde");
    const hastaInput = document.getElementById("hasta");
    const notasExperienciaTextarea = document.querySelector(".notasExperiencia");
    
    const errorEmpresa = document.getElementById("error-empresa");
    const errorDescripcion = document.getElementById("error-descripcion");
    const errorTareas = document.getElementById('error-tareas');
    const errorDesde = document.getElementById("error-desde");
    const errorHasta = document.getElementById("error-hasta");
    const errorNotasExperiencia = document.getElementById("error-notasExperiencia");
    
    const btnSiguienteForm4 = document.getElementById('btn-siguiente-form4');

    // Validaciones
    empresaInput.addEventListener("input", function() {
        const empresaValue = empresaInput.value.trim();
        if (!empresaValue) {
            empresaInput.classList.add("error");
            errorEmpresa.textContent = "Este campo es obligatorio";
        } else {
            empresaInput.classList.remove("error");
            errorEmpresa.textContent = "";
        }
        checkForm3Validity();
    });

    descripcionInput.addEventListener("input", function() {
        const descripcionValue = descripcionInput.value.trim();
        if (!descripcionValue) {
            descripcionInput.classList.add("error");
            errorDescripcion.textContent = "Este campo es obligatorio";
        } else {
            descripcionInput.classList.remove("error");
            errorDescripcion.textContent = "";
        }
        checkForm3Validity();
    });

    tareasTextarea.addEventListener('input', function() {
        validateTareas();
    });

    function validateTareas() {
        const tareasValue = tareasTextarea.value.trim();
        if (!tareasValue) {
            tareasTextarea.classList.add('error');
            errorTareas.textContent = 'Este campo es obligatorio';
        } else {
            tareasTextarea.classList.remove('error');
            errorTareas.textContent = '';
        }
        checkForm3Validity();
    }

    desdeInput.addEventListener("input", function() {
        const desdeValue = desdeInput.value.trim();
        if (!desdeValue) {
            desdeInput.classList.add("error");
            errorDesde.textContent = "Este campo es obligatorio";
        } else {
            const fechaDesde = new Date(desdeValue);
            const fechaLimiteDesde = new Date("1980-01-01");
            const fechaActual = new Date();

            if (fechaDesde <= fechaLimiteDesde || fechaDesde > fechaActual) {
                desdeInput.classList.add("error");
                errorDesde.textContent = "La fecha debe ser posterior a 1980 y anterior a la fecha actual";
            } else {
                desdeInput.classList.remove("error");
                errorDesde.textContent = "";

                // Validar que la fecha de Desde sea menor que la fecha de Hasta si ambos tienen valor
                const hastaValue = hastaInput.value.trim();
                if (hastaValue) {
                    const fechaHasta = new Date(hastaValue);
                    if (fechaDesde >= fechaHasta) {
                        hastaInput.classList.add("error");
                        errorHasta.textContent = "La fecha de fin debe ser mayor que la fecha de inicio";
                    } else {
                        hastaInput.classList.remove("error");
                        errorHasta.textContent = "";
                    }
                }
            }
        }
        checkForm3Validity();
    });

    hastaInput.addEventListener("input", function() {
        const hastaValue = hastaInput.value.trim();
        if (!hastaValue) {
            hastaInput.classList.add("error");
            errorHasta.textContent = "Este campo es obligatorio";
        } else {
            const fechaHasta = new Date(hastaValue);
            const fechaLimiteDesde = new Date("1980-01-01");
            const fechaActual = new Date();

            if (fechaHasta < fechaLimiteDesde || fechaHasta > fechaActual) {
                hastaInput.classList.add("error");
                errorHasta.textContent = "La fecha debe estar entre 1980 y la fecha actual";
            } else {
                hastaInput.classList.remove("error");
                errorHasta.textContent = "";

                // Validar que la fecha de Hasta sea mayor que la fecha de Desde si ambos tienen valor
                const desdeValue = desdeInput.value.trim();
                if (desdeValue) {
                    const fechaDesde = new Date(desdeValue);
                    if (fechaHasta <= fechaDesde) {
                        hastaInput.classList.add("error");
                        errorHasta.textContent = "La fecha de fin debe ser mayor que la fecha de inicio";
                    } else {
                        hastaInput.classList.remove("error");
                        errorHasta.textContent = "";
                    }
                }
            }
        }
        checkForm3Validity();
    });

    notasExperienciaTextarea.addEventListener("input", function() {
        const notasExperienciaValue = notasExperienciaTextarea.value.trim();
        if (notasExperienciaValue.length > 150) {
            notasExperienciaTextarea.classList.add("error");
            errorNotasExperiencia.textContent = "Debe contener menos de 150 caracteres";
        } else {
            notasExperienciaTextarea.classList.remove("error");
            errorNotasExperiencia.textContent = "";
        }
        checkForm3Validity();
    });

    function checkForm3Validity() {
        const empresaValida = empresaInput.value.trim() !== "";
        const descripcionValida = descripcionInput.value.trim() !== "";
        const tareasValidas = tareasTextarea.value.trim() !== "";
        const desdeValido = desdeInput.value.trim() !== "" && new Date(desdeInput.value.trim()) > new Date("1980-01-01") && new Date(desdeInput.value.trim()) <= new Date();
        const hastaValida = hastaInput.value.trim() !== "" && new Date(hastaInput.value.trim()) >= new Date("1980-01-01") && new Date(hastaInput.value.trim()) <= new Date() && (desdeInput.value.trim() === "" || new Date(hastaInput.value.trim()) > new Date(desdeInput.value.trim()));
        const notasExperienciaValida = notasExperienciaTextarea.value.trim().length <= 150;

        if (empresaValida && descripcionValida && tareasValidas && desdeValido && hastaValida && notasExperienciaValida) {
            btnSiguienteForm4.disabled = false;
        } else {
            btnSiguienteForm4.disabled = true;
        }
    }

    // Inicializa la validación al cargar la página
    checkForm3Validity();
});








