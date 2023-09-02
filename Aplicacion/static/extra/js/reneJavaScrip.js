function submit(id){
	getEl(id).submit()
}

function estaSeleccionado(id){
	return getEl(id).checked;
}
function setValue(id,valor) {
	document.getElementById(id).value=valor
}
function getValueCheckedRBs(){
	lista=arguments
	for (let i = 1; i < lista.length; i++) {
		const element = lista[i];
		if(a.checked){
			return a.value;
		}
	}
	return null;
}
function or(a){
	lista=arguments
	for (let i = 1; i < lista.length; i++) {
		const element = lista[i];
		if(a===element){
			return true;
		}
	}
	return false;
}

function displayNone(id,ocultar){
	if(ocultar == undefined){ocultar=true;}
	if(ocultar){
		getEl(id).style.display="none"
	}else{
		getEl(id).style.display=""
	}
}

function contains(a,b){
	return a.length>0&&a.includes(b);
	}
	// function contains(a, sub) {
	// 	return a.indexOf(sub) != -1
	// }
function setAtr(id, atributo, valor) {
	document.getElementById(id).setAttribute(atributo, valor)
}
function removeAtr(id, atributo) {
	if (containsAtr(id, atributo)) {
		//document.getElementById(id).removeAttribute(atributo)
		document.getElementById(id).attributes.removeNamedItem(atributo)
	}
}
function containsAtr(id, atributo) {
	//return document.getElementById(id).attributes.contains(atributo)
	return document.getElementById(id).attributes.getNamedItem(atributo)
}

function setHTML(id, contenidoHtml) {
	document.getElementById(id).innerHTML = contenidoHtml;
}
function getHTML(id, contenidoHtml) {
	return document.getElementById(id).innerHTML;
}

function repetirHTML(id, cantidad, contenidoHtml) {
	if (contenidoHtml == null) { contenidoHtml = getHTML(id) }
	contenido = "";
	for (let i = 0; i < cantidad; i++) {
		contenido += contenidoHtml
	}
	setHTML(id, contenido)
}

function getEl(id) {
	return document.getElementById(id)
}
function getValue(id) {
	return document.getElementById(id).value
}

function addOnChange(id, metodoUtilizarE) {
	getEl(id).addEventListener("change", metodoUtilizarE)
	//getEl("e1").onchange=function(e){alert(getValue("e1"))}
	//getEl("e1").addEventListener("change",function(e){alert("a")})
}

function addOnKeyUp(id, metodoUtilizarE) {
	getEl(id).addEventListener("keyup", metodoUtilizarE)
	//getEl("e1").onchange=function(e){alert(getValue("e1"))}
	//getEl("e1").addEventListener("change",function(e){alert("a")})
}




function irA(file) {
	location.href = file
}




function esString(a) {
	if (typeof (a) == "string") {
		return true;
	}
	return false;
}

function volverCodigoInternoATexto_Clase(clase) {
	elments = document.getElementsByClassName(clase);
	for (var i = elments.length - 1; i >= 0; i--) {
		v = elments[i];
		setText(v, v.innerHTML);
	}
}
function volverCodigoInternoATexto(id) {
	setText(id, document.getElementById(id).innerHTML);
}
function setText(id, text) {
	var v;
	if (esString(id)) {
		v = document.getElementById(id);
	} else {

		v = id;
	}

	while (contains(text, '<br><br>')) {
		text = text.replace('<br><br>', '<br>');
	}
	while (contains(text, '\n\n')) {
		text = text.replace('\n\n', '\n');
	}
	if (text.startsWith('\n')) {
		text = text.substring(1);
	}
	//console.log(text)
	v.innerText = text;
}




function ponerElementoDeLista(id, lista, indice, linea) {

	var element = lista[indice];
	lineaMomentanea = linea;
	for (var j = 0; j < element.length; j++) {
		var parAtributo = element[j];
		lineaMomentanea = lineaMomentanea.replace("{" + parAtributo[0] + "}", parAtributo[1])
	}
	lineaMomentanea = lineaMomentanea.replace("{indice}", (indice + 1) + "")

	document.getElementById(id).innerHTML = lineaMomentanea;

}



function repetidor(id, lista, linea) {
	contenidoHtml = ""

	if (linea == undefined || linea === "") {

		linea = document.getElementById(id).innerHTML

	}

	for (var i = 0; i < lista.length; i++) {
		var element = lista[i];
		lineaMomentanea = linea;
		for (var j = 0; j < element.length; j++) {
			var parAtributo = element[j];
			lineaMomentanea = lineaMomentanea.replaceAll("{" + parAtributo[0] + "}", parAtributo[1])
		}
		lineaMomentanea = lineaMomentanea.replaceAll("{indice}", (i + 1) + "")
		contenidoHtml += "\n" + lineaMomentanea;
	}

	document.getElementById(id).innerHTML = contenidoHtml;


}



function ponerElementoDeLista(id, lista, indice, linea) {
	contenidoHtml = ""
	if (linea == undefined || linea === "") {

		linea = document.getElementById(id).innerHTML

	}
	var element = lista[indice];
	lineaMomentanea = linea;
	for (var j = 0; j < element.length; j++) {
		var parAtributo = element[j];
		lineaMomentanea = lineaMomentanea.replace("{" + parAtributo[0] + "}", parAtributo[1])
	}
	lineaMomentanea = lineaMomentanea.replace("{indice}", (indice + 1) + "")
	contenidoHtml += "\n" + lineaMomentanea;


	document.getElementById(id).innerHTML = contenidoHtml;


}


function ponerElemntosDeLista(id, lista, llave) {
	linea = document.getElementById(id).innerHTML;


	lineaMomentanea = "";
	for (var j = 0; j < lista.length; j++) {

		lineaMomentanea += linea.replace("{" + llave + "}", lista[j])
	}




	document.getElementById(id).innerHTML = lineaMomentanea;

}

function put(llave, valor) {
	localStorage.setItem(llave, valor);
}

function get(llave) {
	return localStorage.getItem(llave);
}

var LLAVE_INDICE = "LLAVE_INDICE";


function irA(direccion) {
	location.href = direccion;
}

function getItem(lista, indice, llave) {
	var element = lista[indice];

	for (var j = 0; j < element.length; j++) {
		var parAtributo = element[j];
		if (llave === parAtributo[0]) {
			return parAtributo[1];
		}


	}

}



function ponerElemntosDeListaGeneral(id, lista, indice, llave) {
	listaMomentanea = getItem(lista, indice, llave);
	ponerElemntosDeLista(id, listaMomentanea, llave);

}

function ponerElemntosDeListaTodos(id, lista, indice, llaves) {
	for (var j = 0; j < llaves.length; j += 2) {
		ponerElemntosDeListaGeneral(llaves[j], lista, indice, llaves[j + 1]);
	}
	ponerElementoDeLista(id, lista, indice);

}




class ArgumentosParaActualizadorDeListaYValidacion {
	constructor() {
		this.idIndependiente = null;
		this.idDependiente = null;
		this.listaDatosDependientes = null;
		this.idPadreIndependiente = null;
		this.idPadreDependiente = null;
		this.contenidoVacioIndependiente = null;
		this.contenidoVacioDependiente = null;
		this.idBotonADesactivar = null
	}

}

function setActualizadorDeListaYValidacion(argumentosParaActualizadorDeListaYValidacion) {
	idIndependiente = argumentosParaActualizadorDeListaYValidacion.idIndependiente
	idDependiente = argumentosParaActualizadorDeListaYValidacion.idDependiente
	listaDatosDependientes = argumentosParaActualizadorDeListaYValidacion.listaDatosDependientes

	idPadreIndependiente = argumentosParaActualizadorDeListaYValidacion.idPadreIndependiente;
	idPadreDependiente = argumentosParaActualizadorDeListaYValidacion.idPadreDependiente;
	contenidoVacioIndependiente = argumentosParaActualizadorDeListaYValidacion.contenidoVacioIndependiente;
	contenidoVacioDependiente = argumentosParaActualizadorDeListaYValidacion.contenidoVacioDependiente;
	idBotonADesactivar = argumentosParaActualizadorDeListaYValidacion.idBotonADesactivar
	//asumo que el value de idIndependiente es un #i 0-...
	//listaDatosDependientes [ [i,[opcionesParaDependiente]] , [i2,[opcionesParaDependiente]] , ... ]

	contenidoPadreIndependiente = null
	contenidoPadreDependiente = null
	estaDesactivado = false

	function guardarContenidoPadreIndependiente() {
		contenidoPadreIndependiente = getHTML(idPadreIndependiente)
	}
	function guardarContenidoPadreDependiente() {
		contenidoPadreDependiente = getHTML(idPadreDependiente)
	}
	function cargarContenidoPadreDependiente() {
		setHTML(idPadreDependiente, contenidoPadreDependiente)
	}

	function desactivar() {
		setAtr(idBotonADesactivar, "disabled", "")
		estaDesactivado = true
	}
	function activar() {
		removeAtr(idBotonADesactivar, "disabled")
		estaDesactivado = false
	}

	if (listaDatosDependientes.length == 0) {
		guardarContenidoPadreIndependiente()
		setHTML(idPadreIndependiente, contenidoVacioIndependiente)
		guardarContenidoPadreDependiente()
		setHTML(idPadreDependiente, contenidoVacioDependiente)
		desactivar()
	} else {
		function crearOpcion(indice, contenido) {
			return '<option value="' + indice + '">' + contenido + '</option>'
		}


		contenido = ""
		for (let index = 0; index < listaDatosDependientes.length; index++) {
			const element = listaDatosDependientes[index][0];
			contenido += crearOpcion(index, element)
		}
		setHTML(idIndependiente, contenido)

		function actualizar(e) {
			indice = getValue(idIndependiente)
			listaActual = listaDatosDependientes[indice][1]
			if (listaActual.length == 0) {
				guardarContenidoPadreDependiente()
				setHTML(idPadreDependiente, contenidoVacioDependiente)
				desactivar()
			} else {
				contenido = ""
				for (let index = 0; index < listaActual.length; index++) {
					const element = listaActual[index];
					contenido += crearOpcion(index, element)
				}
				if (estaDesactivado) {
					cargarContenidoPadreDependiente()
				}
				setHTML(idDependiente, contenido)
				activar()
			}


		}

		addOnChange(idIndependiente, actualizar)
		actualizar("")

	}






}



function setActualizadorDeLista(idIndependiente, idDependiente, listaDatosDependientes) {
	//asumo que el value de idIndependiente es un #i 0-...
	//listaDatosDependientes [ [i,[opcionesParaDependiente]] , [i2,[opcionesParaDependiente]] , ... ]

	function crearOpcion(indice, contenido) {
		return '<option value="' + indice + '">' + contenido + '</option>'
	}

	contenido = ""
	for (let index = 0; index < listaDatosDependientes.length; index++) {
		const element = listaDatosDependientes[index][0];
		contenido += crearOpcion(index, element)
	}
	setHTML(idIndependiente, contenido)

	function actualizar(e) {
		indice = getValue(idIndependiente)
		listaActual = listaDatosDependientes[indice][1]
		contenido = ""
		for (let index = 0; index < listaActual.length; index++) {
			const element = listaActual[index];
			contenido += crearOpcion(index, element)
		}
		setHTML(idDependiente, contenido)

	}

	addOnChange(idIndependiente, actualizar)
	actualizar("")



}

function setFiltroText(idText,lista,keyID_elemento_a_comprobar_en_lista,predicate_evaluar_propiedad){
	//keyID_elemento_a_comprobar_en_lista es el elemtento por el que se va a obtener
	//el elemento que se va a ocultar o no
	//predicate_evaluar_propiedad (e)->{boolean} donde e va a ser el key actual y va aretornar si 
	//comparar el contenido de esta llave en la lista con el texxto actual
	//la idea es seleccionar que elementos de la lista son los comparables y si estos elementos
	//son seleccionables en otro punto,saver cuales son los que hay que evaluar en el momento

	
	addOnKeyUp(idText,function(e){
		textoActual=e.target.value
		//console.log(textoActual)
		for (let i = 0; i < lista.length; i++) {
			const element = lista[i];
			ocultarElemento=true;
			idElemento=null;
			//console.log("------------------------------")
			for (let j = 0; j < element.length; j++) {
				const parKeyValue = element[j];
				key=parKeyValue[0];
				value=parKeyValue[1];
				if(key!==keyID_elemento_a_comprobar_en_lista){
					if((ocultarElemento)&&predicate_evaluar_propiedad(key)){
						
						if(contains(value.toLowerCase(),textoActual.toLowerCase())){
							//console.log("value="+value)
							//console.log("textoActual="+textoActual)
							ocultarElemento=false;
						}
					}
				}else{
					idElemento=value+(i+1);
				}
				
			}
			//console.log("i="+idElemento)
			if(idElemento!=null){
				//console.log("ocultarElemento="+ocultarElemento)
				displayNone(idElemento,ocultarElemento)
			}
			
			
			
		}
	})
}
