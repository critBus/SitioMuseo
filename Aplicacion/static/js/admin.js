$(document).ready(function () {
	"use strict"; // start of use strict

function readURL(input,idImg) {
		if (input.files && input.files[0]) {
			var reader = new FileReader();

			reader.onload = function(e) {
				$('#'+idImg).attr('src', e.target.result);
			}

			reader.readAsDataURL(input.files[0]);
		}
	}
	function ponerEventoImg(idImg,idInput){
	//console.log("se llamo");

	$('#'+idInput).on('change', function() {
		readURL(this,idImg);
	});
	$('#'+idImg).on("click",function () {
		$('#'+idInput).click();
	});
	}



	function getIdsWithClass(className) {
	  var elements = document.getElementsByClassName(className);
	  var ids = [];
	  for (var i = 0; i < elements.length; i++) {
		if (elements[i].id) {
		  ids.push(elements[i].id);
		}
	  }
	  return ids;
	}

	function executeMethodOnIdsWithClass(className, method) {
	//console.log("llamada uno");
	  var ids = getIdsWithClass(className);
	  for (var i = 0; i < ids.length; i++) {
		var id = ids[i];
		method(id);
	  }
	}

	function transformString_PatronImagen(str) {
	  var prefix = str.substring(0, str.indexOf('_img_id'));
	  return 'id_' + prefix;
	  //var id = str.substring(str.indexOf('_img_id') + 8);
	  //return 'id_' + id + '_' + prefix;
	}

	executeMethodOnIdsWithClass("img-admin"
		,idImg=>ponerEventoImg(idImg,transformString_PatronImagen(idImg)));

});