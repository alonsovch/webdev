export function validarFormulario(event) {
  event.preventDefault(); // Evitar que el formulario se envíe automáticamente

  // Obtener referencias a los campos del formulario
  const tipoProducto = document.getElementById("tipo-producto");
  const producto = document.getElementById("producto");
  const multimedia = document.getElementById("multimedia");
  const region = document.getElementById("region");
  const comuna = document.getElementById("comuna");
  const nombreProductor = document.getElementById("nombre-productor");
  const emailProductor = document.getElementById("email-productor");
  const numeroProductor = document.getElementById("numero-productor");

  // Validar cada campo
  if (!tipoProducto.value) {
    alert("Por favor, elija un tipo de producto.");
    return;
  }

  if (
    producto.selectedOptions.length < 1 ||
    producto.selectedOptions.length > 5
  ) {
    alert("Por favor, elija entre 1 y 5 productos.");
    return;
  }

  if (multimedia.files.length < 1 || multimedia.files.length > 3) {
    alert("Por favor, suba entre 1 y 3 archivos multimedia.");
    return;
  }

  if (!region.value) {
    alert("Por favor, elija una región.");
    return;
  }

  if (!comuna.value) {
    alert("Por favor, elija una comuna.");
    return;
  }

  if (nombreProductor.value.length < 3 || nombreProductor.value.length > 80) {
    alert("El nombre del productor debe tener entre 3 y 80 caracteres.");
    return;
  }

  // Validar el formato de correo electrónico utilizando una expresión regular
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(emailProductor.value)) {
    alert("Por favor, introduzca un formato de correo electrónico válido.");
    return;
  }

  // Validar el formato de número de teléfono móvil opcional
  const numeroRegex = /^[0-9]{9}$/;
  if (numeroProductor.value && !numeroRegex.test(numeroProductor.value)) {
    alert(
      "Por favor, introduzca un formato de número de teléfono móvil válido."
    );
    return;
  }

  // Si todas las validaciones pasan, puedes enviar el formulario aquí
  alert("Formulario enviado con éxito!");
  event.target.reset(); // Restablecer el formulario después del envío exitoso
}
