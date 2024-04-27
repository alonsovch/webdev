import regionesData from "../data/regionesData.js";
import productosData from "../data/productosData.js";
import { validarFormulario } from "./validatorPedido.js";

function obtenerRegiones() {
  const regionSelect = document.getElementById("region");
  regionesData.regiones.forEach((region) => {
    const regionOption = document.createElement("option");
    regionOption.value = region.region;
    regionOption.textContent = region.region;
    regionSelect.appendChild(regionOption);
  });
  obtenerComunas();
}

function obtenerComunas() {
  const region = document.getElementById("region").value;
  const regionData = regionesData.regiones.find((r) => r.region === region);
  const comunaSelect = document.getElementById("comuna");
  comunaSelect.innerHTML = "";
  if (regionData) {
    regionData.comunas.forEach((comuna) => {
      const comunaOption = document.createElement("option");
      comunaOption.value = comuna;
      comunaOption.textContent = comuna;
      comunaSelect.appendChild(comunaOption);
    });
  }
}

function obtenerTipoProducto() {
  const tipoProductoSelect = document.getElementById("tipo-producto");
  productosData.productos.forEach((producto) => {
    const tipoProductoOption = document.createElement("option");
    tipoProductoOption.value = producto.tipo;
    tipoProductoOption.textContent = producto.tipo;
    tipoProductoSelect.appendChild(tipoProductoOption);
  });
  obtenerProductos();
}

function obtenerProductos() {
  const tipoProducto = document.getElementById("tipo-producto").value;
  const productoData = productosData.productos.find(
    (p) => p.tipo === tipoProducto
  );
  const productoSelect = document.getElementById("producto");
  productoSelect.innerHTML = "";
  if (productoData) {
    productoData.productos.forEach((producto) => {
      const productoOption = document.createElement("option");
      productoOption.value = producto;
      productoOption.textContent = producto;
      productoSelect.appendChild(productoOption);
    });
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const formulario = document.getElementById("formulario");
  formulario.addEventListener("submit", function (event) {
    event.preventDefault();
    validarFormulario(event);
  });

  obtenerRegiones();
  obtenerTipoProducto();

  document.getElementById("region").addEventListener("change", obtenerComunas);
  document
    .getElementById("tipo-producto")
    .addEventListener("change", obtenerProductos);

  const volverInicioBtn = document.getElementById("volverInicio");
  volverInicioBtn.addEventListener("click", function () {
    event.preventDefault();
    window.location.href = "/";
  });
});
