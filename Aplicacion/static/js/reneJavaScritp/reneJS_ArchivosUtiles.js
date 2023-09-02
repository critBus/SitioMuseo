class FileBinario{
	constructor(){
		this.nombre;
		this.datosBinarios;
		this.size;
	}
	cargarDesdeInputFile(idFile){
		let input=document.querySelector('#'+idFile);
		let file = input.files[0];

		let start=0;
		this.size=file.size;
		this.datosBinarios=file.slice(start, this.size);
		this.nombre=file.name;

		return this;//
	}
	ponerImagen(idImg){
		getEl(idImg).src =URL.createObjectURL(this.datosBinarios);
	}
}

function getCantMGB_DeByts(cantidadByts){
    let kybs=cantidadByts/1024;
    let mbgs=kybs/1024;
    return mbgs;
}

function elArchivoEnInputFileEsMenorQueMGBs(idInputFile,cantidadMGBs){
    if(hayArchivoEnInput(idInputFile)){
        return getCantMGB_DeByts(getTamanoEnBytsDeArchivoEnInput(idInputFile))<cantidadMGBs;
    }
}

function notEmpty_ArchivoEnInput(idInputFile){
	let tamn=getTamanoEnBytsDeArchivoEnInput(idInputFile);
	return tamn!=null&&tamn>0;
}

function getTamanoEnBytsDeArchivoEnInput(idInputFile){
	if(hayArchivoEnInput(idInputFile)){
		let file=getEl(idInputFile).files[0];
		//console.log("va a mostrar al file");
		//console.log(file);
		return file.size;
	}
	return null;
}

function hayArchivoEnInput(idInputFile){
	return getEl(idInputFile).files.length>0;
}

function getNombreArchivoEnInput(idInputFile){
	if(hayArchivoEnInput(idInputFile)){
		return getValue(idInputFile).split('\\').pop();
	}
	return null;
}

function getExtencion(url){
	if(url==null||url==undefined){return null;}
	let ext=url.split('\\').pop().split('.').pop();
	return (ext!=null&&ext.length>0)?"."+ext:null;
}
function getExtencionArchivoEnInput(idInputFile){
	if(hayArchivoEnInput(idInputFile)){
		return getExtencion(getValue(idInputFile));
	}
	return null
}

function esZipEnInput(idInputFile){
	return (getExtencionArchivoEnInput(idInputFile)+"").toLocaleLowerCase()==".zip";
}