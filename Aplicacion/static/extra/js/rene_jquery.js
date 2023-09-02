
function ejecutarAjax(post_url,argumentos_post_json,funcion_al_obtener_respuesta){
    //funcion_al_obtener_respuesta (response)->{} donde  response.content.NOMBRE_ARGUMENTO 
    // y aveces el .content tiene que ser agregado manualmente en el servidor ejempl { 'content':{}}
    $.ajax({
        url : post_url,
        type: "POST",
        data : argumentos_post_json,
        success:funcion_al_obtener_respuesta,
    });

}

// var post_url="/metodoPOST/"
// var datos={
//     'nombreImagen':'reneImagenOriginalTemp.png',
//     'nombre_modelo_neuronal':'modeloFrutbaBomba70',
// }
// $.ajax({
//         url : post_url,
//         type: "POST",
//         data : datos,
//         success:function(response){
//             var message1 = response.content.mensaje1
//             var message2 = response.content.mensaje2
//             alert(message1);
//             $("#idLabelAcamibiar").text(message1)

//             //alert(message2);
//         },
//     });