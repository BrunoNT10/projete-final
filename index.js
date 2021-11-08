//cria uma variavel para usar com o firebase
// erro
const db = firebase.database();
function liberar(){
    console.log("botão liberar pressionado");
    document.getElementById("botaoresposta").innerHTML = "Funcionário liberado!"
    try{
        db.ref("users").set({
            libera: "1"
        });
        // alert("Dados salvos com sucesso!");
    }catch(err){
        alert("Houve algum erro!");
    }
    setTimeout(function espera_tempo(){
    	try{
            db.ref("users").set({
                libera: "0"
        });
        }catch(err){
            alert("Houve algum erro!");

        }
        document.getElementById("botaoresposta").innerHTML = "Selecione o que deseja fazer"
        console.log("funcionou o setTimeout");

    }, 3000)
}
function verificar(){
    document.getElementById("botaoresposta").innerHTML = "O funcionário será verificado novamente!"
    try{
        db.ref("users").set({
            libera: "2"
        });
        // alert("Dados salvos com sucesso!");
    }catch(err){
        alert("Houve algum erro!");
    }
    setTimeout(function espera_tempo(){
    	try{
            db.ref("users").set({
                libera: "0"
        });
        }catch(err){
            alert("Houve algum erro!");

        }
        document.getElementById("botaoresposta").innerHTML = "Selecione o que deseja fazer"
        console.log("funcionou o setTimeout");

    }, 3000)
}
function esperar(){
	document.getElementById("botaoresposta").innerHTML = "O funcionário irá esperar."
    try{
        db.ref("users").set({
            libera: "3"
        });
    }catch(err){
        alert("Houve algum erro!");
    }
    setTimeout(function espera_tempo(){
    	try{
            db.ref("users").set({
                libera: "0"
        });
        }catch(err){
            alert("Houve algum erro!");

        }
        document.getElementById("botaoresposta").innerHTML = "Selecione o que deseja fazer!"
        console.log("funcionou o setTimeout");

    }, 3000)
      
}
function enviar(){
	const mensagemdigitada=document.getElementById("mensagem");
    const mensagemenviada=mensagemdigitada.value;
	console.log(mensagemenviada);
	try{
        db.ref("texto").set({
            mensagem: mensagemenviada
        });
        alert("Dados salvos com sucesso!");

    }catch(err){
        alert("Houve algum erro!");
    }
} 

function download(){
	document.getElementById("resposta").innerHTML = "Abrindo a imagem..."
	try{
  	    db
 	      .ref('Arquivo')
   	      .once('value')
   	      .then(function(snapshot){
   	      	resElement = JSON.stringify(snapshot.val());
   	  	    console.log(resElement);
       	    const file = resElement;
       	    arquivo1 = file.replace(/['"]+/g, '')
       	    console.log(arquivo1)
	        const storageRef = firebase.storage().ref("imagens funcionarios/" + arquivo1);
	        storageRef.getDownloadURL().then(function(url){
		    const image = document.getElementById("image");
		    console.log(url);
		    image.src = url;
		    setTimeout(function imagem(){
		    	image.src = ""
   			    console.log("tempo")
   			    document.getElementById("resposta").innerHTML = "Clique no botão para abrir a imagem."

		    }, 5000)
		    // image.src = "";
	})
   	   });
}catch(err){
   	alert("Houve algum erro!");
}
	
}
