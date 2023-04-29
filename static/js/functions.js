function enviar_datos(url, datos, csrftoken, callback) {
  $.ajax({
    url: url,
    type: "POST",
    data: datos,
    dataType: "json",
    headers: {
      "X-CSRFToken": csrftoken, //aqui va el token para que entre por la petición post sin necesidad de quitarle la seguridad
    },
  })
    .done(function (data) {
      //Este metodo se ejecuta si la peticion se realiza de manera exitosa
      callback(data);
    })
    .fail(function (jqXHR, textStatus, errorThrown) {
      //Este se ejecuta si la peticion tiene algun error
      alert(`${textStatus} : ${errorThrown}`);
    })
    .always(function () {
      //este se ejecuta siempre
    });
}

function carritoAcciones(itemId,url,accion, user_id, csrftoken) {
      var datos = JSON.stringify({
        // Convierte los datos en JSON para poder procesarlos en la vista
        pk: itemId,
        user_id: user_id,
        action: accion,
      });
  enviar_datos(url, datos, csrftoken, function (data) {
    if (data["mensaje"]) {
      Swal.fire({
        position: "top-end",
        icon: "success",
        title: `${data["mensaje"]}`,
        showConfirmButton: false,
        timer: 1500,
      }).then((result) => {
        const pTotal = document.getElementById("cart-total"); //poner el total en el carrito
        pTotal.innerHTML = `${data['can_carrito']}`;
      });
      //si es alguna de las 3 acciones del carrito lo pongo aqui 
      if (accion == "eliminar") {
        var trElim = document.getElementById("item-" + itemId); //obtengo el tr del item y lo quito si la petición de eliminar es correcta
        trElim.remove();
      } else if (accion == "aumentar" || accion == "disminuir") {
        if (accion == "aumentar") {
          msj = "Se aumento";
        } else if (accion == "disminuir") {
          msj = "Se disminuyó";
        }
        Swal.fire({
          position: "top-end",
          icon: "success",
          title: msj,
          showConfirmButton: false,
          timer: 1000,
        }).then((result) => {
            const cantidad = document.getElementById(`product/${itemId}`); //donde va la cantidad
            const total = document.getElementById(`total_product/${itemId}`); //donde va el total
            cantidad.innerHTML = `${data['can_cantidad']}`
          total.innerHTML = `${data["can_total"].toFixed(2)}`;
        });
      };
      const checkputTotal = document.getElementById(`checkout_total`);
      checkputTotal.innerHTML = `${data["check_total"].toFixed(1)}`;
      
    } else {
      Swal.fire({
        position: "top-end",
        icon: "error",
        title: `${data["error"]}`,
        showConfirmButton: false,
        timer: 1500,
      });
    }
  });
    };
 
