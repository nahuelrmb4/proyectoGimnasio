function confirmarBorrado() {
  var confirmacion = confirm("¿Estás seguro que deseas borrar?");
  if (confirmacion) {
    alert("Borrado exitoso");
  } else {
    alert("Operación cancelada");
  }
}
