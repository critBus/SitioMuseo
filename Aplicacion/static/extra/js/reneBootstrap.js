// Para activar lo tooltip
// Codigo de bootstrap
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

function showDlgBostrap(id){
  $("#"+id).modal('show')
}

function hideDlgBostrap(id){
  $("#"+id).modal('hide')
}