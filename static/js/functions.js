function enviar_datos(url, datos, callback) {
  $.ajax({
    url: url,
    type: "POST",
    data: datos,
    dataType: "json",
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
        csrfmiddlewaretoken: csrftoken, //paso el token conesta clave
      });
  enviar_datos(url, datos, function (data) {
        if (data['mensaje']){
          Swal.fire({
            position: "top-end",
            icon: "success",
            title: `${data["mensaje"]}`,
            showConfirmButton: false,
            timer: 1500,
          });
          if (accion=='eliminar'){
            var trElim = document.getElementById("item-" + itemId); //obtengo el tr del item y lo quito si la petición de eliminar es correcta
            trElim.remove();
          } else {
            if (accion == 'aumentar') {
              msj = "Se aumento";
            } else {
              msj = "Se disminuyó";
            }
            Swal.fire({
              position: "top-end",
              icon: "success",
              title: msj,
              showConfirmButton: false,
              timer: 1000,
            }).then((result) => {
              location.href = "/cart/"; //lo redirecciono por ahora a la misma vista hasta saber como cambiar los valores
            });

          }
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
 
