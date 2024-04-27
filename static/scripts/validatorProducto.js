export function validarFormulario(event) {
  event.preventDefault();

  const tipoProducto = document.getElementById("tipo-producto");
  const producto = document.getElementById("producto");
  const multimedia = document.getElementById("multimedia");
  const region = document.getElementById("region");
  const comuna = document.getElementById("comuna");
  const nombreProductor = document.getElementById("nombre-productor");
  const emailProductor = document.getElementById("email-productor");
  const numeroProductor = document.getElementById("numero-productor");

  const errores = [];

  if (!tipoProducto.value) {
    errores.push("Por favor, elija un tipo de producto.");
  }

  if (
    producto.selectedOptions.length < 1 ||
    producto.selectedOptions.length > 5
  ) {
    errores.push("Por favor, elija entre 1 y 5 productos.");
  }

  if (multimedia.files.length < 1 || multimedia.files.length > 3) {
    errores.push("Por favor, suba entre 1 y 3 archivos multimedia.");
  }

  if (!region.value) {
    errores.push("Por favor, elija una región.");
  }

  if (!comuna.value) {
    errores.push("Por favor, elija una comuna.");
  }

  if (nombreProductor.value.length < 3 || nombreProductor.value.length > 80) {
    errores.push("El nombre del productor debe tener entre 3 y 80 caracteres.");
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(emailProductor.value)) {
    errores.push(
      "Por favor, introduzca un formato de correo electrónico válido."
    );
  }

  const numeroRegex = /^569\d{8}$/;
  if (!numeroProductor.value || !numeroRegex.test(numeroProductor.value)) {
    errores.push(
      "Por favor, introduzca un número de teléfono móvil chileno válido."
    );
  }

  if (errores.length > 0) {
    alert(errores.join("\n"));
    return false;
  }
  mostrarConfirmacion();
  return true;
}

function mostrarConfirmacion() {
  const confirmacion = confirm("¿Confirma el registro de este producto?");
  if (confirmacion) {
    alert("Hemos recibido el registro de producto. Muchas gracias.");
    document.getElementById("formulario").style.display = "none";
    document.getElementById("volverInicio").style.display = "block";
  } else {
    alert("Registro cancelado. Puede volver a revisar el formulario.");
  }
}
