export function validarFormulario(event) {
  event.preventDefault();

  const tipoProducto = document.getElementById("tipo-producto");
  const producto = document.getElementById("producto");
  const region = document.getElementById("region");
  const comuna = document.getElementById("comuna");
  const nombreComprador = document.getElementById("nombre-comprador");
  const emailComprador = document.getElementById("email-comprador");
  const numeroComprador = document.getElementById("numero-comprador");

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

  if (!region.value) {
    errores.push("Por favor, elija una región.");
  }

  if (!comuna.value) {
    errores.push("Por favor, elija una comuna.");
  }

  if (nombreComprador.value.length < 3 || nombreComprador.value.length > 80) {
    errores.push("El nombre del comprador debe tener entre 3 y 80 caracteres.");
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(emailComprador.value)) {
    errores.push(
      "Por favor, introduzca un formato de correo electrónico válido."
    );
  }

  const numeroRegex = /^569\d{8}$/;
  if (!numeroComprador.value || !numeroRegex.test(numeroComprador.value)) {
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
  const confirmacion = confirm("¿Confirma el registro de este pedido?");
  if (confirmacion) {
    alert("Hemos recibido su pedido. Muchas gracias.");
    document.getElementById("formulario").style.display = "none";
    document.getElementById("volverInicio").style.display = "block";
  } else {
    alert("Registro cancelado. Puede volver a revisar el formulario.");
  }
}
