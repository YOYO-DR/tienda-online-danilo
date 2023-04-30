/* function enviar_datos(url, datos, callback) {
  const csrftoken = $("[name=csrfmiddlewaretoken]").val(); // obtener el token CSRF del input escondido de la pagina
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
}*/

//fetch chatgpt

function enviar_datos(url, datos, callback) {
  const csrftoken = $("[name=csrfmiddlewaretoken]").val(); // obtener el token CSRF del input escondido de la pagina

  fetch(url, {
    method: "POST",
    body: JSON.stringify(datos), // Convierte los datos en JSON para poder procesarlos en la vista
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      callback(data);
    })
    .catch((error) => {
      alert(error);
    });
};

function carritoAcciones(itemId,url,accion) {
      var datos = {
        pk: itemId,
        action: accion,
      };
  enviar_datos(url, datos, function (data) {//funcion si la petición se hace correctamente
    if (data['error']) {
  Swal.fire({
    position: "top-end",
    icon: "error",
    title: `${data["error"]}`,
    showConfirmButton: false,
    timer: 1500,
  });
    } else {
      if (accion == "add_cart") {
        //si existe la clave mensaje
        /*Swal.fire({
        position: "top-end",
        icon: "success",
        title: `${data["mensaje"]}`,
        showConfirmButton: false,
        timer: 1500,
      }).then((result) => {*/ //despues del modal
        const pTotal = document.getElementById("cart-total"); //obtengo el p del carrito
        pTotal.innerHTML = `${data["can_carrito"]}`; //le pongo la cantidad
        //});

        //si es alguna de las 3 acciones del carrito lo pongo aqui
      } else if (accion == "eliminar") {
        var trElim = document.getElementById("item-" + itemId); //obtengo el tr del item y lo quito si la petición de eliminar es correcta
        trElim.remove();
      } else if (accion == "aumentar" || accion == "disminuir") {
        //si es aumentar o disminuir, modifico el mensaje del modal
        /*if (accion == "aumentar") {
          msj = "Se aumento ";
        } else if (accion == "disminuir") {
          msj = "Se disminuyó ";
        }
        Swal.fire({
          position: "top-end",
          icon: "success",
          title: msj+data['mensaje'],
          showConfirmButton: false,
          timer: 1000,
        }).then((result) => {*/
        const cantidad = document.getElementById(`product/${itemId}`); //donde va la cantidad
        const total = document.getElementById(`total_product/${itemId}`); //donde va el total
        cantidad.innerHTML = `${data["can_cantidad"]}`;
        totalN=data["can_total"].toLocaleString("es-ES", {
          minimumFractionDigits: 1,
          maximumFractionDigits: 1,
        })
        total.innerHTML = `${totalN}`;
        //});
      }
      if (accion == "aumentar" || accion == "disminuir" || accion == "eliminar") {
        //independientemente de la accion, eliminar, aumentar o disminuir, se modifica el total del checkout
        const checkoutTotal = document.getElementById(`checkout_total`);
        checkTotalN = data["check_total"].toLocaleString("es-ES", { //para convertirlo a numero natural o el intcomma de django
          minimumFractionDigits: 1,
          maximumFractionDigits: 1,
        });
        checkoutTotal.innerHTML = `${checkTotalN}`;
        if (data["check_total"] == 0) {
          //si el el total del carrito es 0, remplazo todo el contenido y pongo un mensaje
          const contenedorABorrar = document.getElementById("contenedor_todo");
          contenedorABorrar.innerHTML =
            "<h2>No hay productos en el carrito</h2>";
        }
      }
      
}
    
    
     
  });
    };
 
