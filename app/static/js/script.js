      //--------------------Funcion Imagen---------------------------

      $(document).ready(function() {
        $('.imagen').change(function() {
            var input = $(this)[0];
            var maxSizeMB = 5;  // Define el tamaño máximo permitido en megabytes
            var maxSizeBytes = maxSizeMB * 1000 * 1000;  // Convertir megabytes a bytes

            if (input.files && input.files[0]) {
                var file = input.files[0];
                var fileSize = file.size;  // Tamaño del archivo en bytes
                var fileType = file.type.toLowerCase();

                if (fileSize > maxSizeBytes) {
                    alert("El archivo es demasiado grande. El tamaño máximo permitido es " + maxSizeMB + " MB.");
                    $(this).val('');  // Limpiar el campo de entrada
                    $('#imagen-preview').hide();  // Ocultar o limpiar la vista previa de la imagen
                } else if (fileType === "image/jpeg" || fileType === "image/jpg") {
                    var reader = new FileReader();
                    reader.onload = function(e) {
                        $('#imagen-preview').attr('src', e.target.result).show();
                    }
                    reader.readAsDataURL(file);
                } else {
                    alert("Por favor, seleccione un archivo de imagen JPG.");
                    $(this).val('');  // Limpiar el campo de entrada
                    $('#imagen-preview').hide();  // Ocultar o limpiar la vista previa de la imagen
                }
            }
        });
    });


//----------------Funcion de mostrar formulario Siguiente----------------

function mostrarSiguienteFormulario(formActual, formSiguiente) {
  document.getElementById(formActual).style.display = 'none';
  document.getElementById(formSiguiente).style.display = 'block';
  document.querySelector(`[data-form="${formSiguiente}"]`).classList.add('active');
  document.querySelector(`[data-form="${formActual}"]`).classList.remove('active');
  window.scrollTo(0, 0); // Añade esta línea para desplazar la página al comienzo
}


//----------------Funcion de mostrar formulario Anterior----------------

function mostrarAnteriorFormulario(formActual, formAnterior) {
  document.getElementById(formActual).style.display = 'none';
  document.getElementById(formAnterior).style.display = 'block';
  document.querySelector(`[data-form="${formAnterior}"]`).classList.add('active');
  document.querySelector(`[data-form="${formActual}"]`).classList.remove('active');
  window.scrollTo(0, 0);
}

//----------------Funcion de Iconos----------------

const navItems = document.querySelectorAll(".nav-item");

navItems.forEach((navItem, i) => {
navItem.addEventListener("click", () => {
  navItems.forEach((item, j) => {
    item.className = "nav-item";
  });
  navItem.className = "nav-item active";
});
});


//---------------Funcion de Mensaje------------------------

  setTimeout(function(){
          elementoP = document.querySelector('.msg');
          elementoP.style.display = 'none';
      }, 3000);




      document.addEventListener('DOMContentLoaded', function() {
        // Mostrar la imagen temporal
        var imagenTemporal = document.getElementById('imagen-temporal');
        imagenTemporal.style.display = 'block';
    
        // Ocultar la imagen después de 5 segundos (5000 milisegundos)
        setTimeout(function() {
            imagenTemporal.style.display = 'none';
        }, 8000); // 5000 milisegundos = 5 segundos
    });
    

//------------------------------------------------------------------------------

// Obtener elementos del DOM
const roundButton = document.querySelector('.round-button');
const popup = document.getElementById('popup');
const avatarButton = document.querySelector('.avatar-container');

// Agregar evento de clic al botón para abrir la ventana emergente
roundButton.addEventListener('click', () => {
    popup.classList.add('activo');
});

// Agregar evento de clic al botón de avatar para cerrar la ventana emergente
avatarButton.addEventListener('click', () => {
    popup.classList.remove('activo');
});



//-------------------------------------------------------------------------------