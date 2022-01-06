function start_loading(){
	$("#loading").fadeIn();
}

function stop_loading(){
	$("#loading").fadeOut();
}

function has_class(ele,cls) {
	return ele.className.match(new RegExp('(\\s|^)'+cls+'(\\s|$)'));
}
 
function add_class(ele,cls) {
	if (!this.has_class(ele,cls)) ele.className += " "+cls;
}
 
function remove_class(ele,cls) {
	if (has_class(ele,cls)) {
    	var reg = new RegExp('(\\s|^)'+cls+'(\\s|$)');
		ele.className=ele.className.replace(reg,' ');
	}
}

function __checkbox(id){
	if($("#" + id).is(":checked")){
		$("#" + id + "-value").val(1);
	}else{
		$("#" + id + "-value").val(0);
	}
}

function open_form(){
	if($("#add-form").css("display") == "block"){
		close_form();
	}else{
		$("#add-form").stop().fadeIn(500);
		$("#close-form").stop().fadeIn(500);
		$("input").delay(500).eq(2).focus();
	}
}

function close_form(){
	if($("[name=id]").val() != "0"){
		$(".input").each(function(){
			$(this).val("");
		}); $("[name=id]").val("0");
	}

	$("#add-form").stop().fadeOut();
	$("#close-form").stop().fadeOut();
}

function get_id_and_ask_before_go(elemento,msg,url){
	var id = elemento.id.split("_");
		id = id[1];

	ask_before_go(msg,url + id);
}

function ask_before_go(msg,url){
	$("#ask_before_go").fadeIn();
	$("#ask_before_go_protect").fadeIn();
	$("#ask_before_go_label").html(msg);
	$("#ask_before_go_url").val(url);
}

function ask_before_go_action(){ var url = document.getElementById('ask_before_go_url').value;
	if(url == "/home/fechar" || url == "/home/abrir"){
		location = url;
	}else{
		go(url);
	}
}

function ask_before_go_close(){
	$('#ask_before_go').fadeOut();
	$('#ask_before_go_protect').fadeOut();
	$('#ask_before_go_label').html("");
	$('#ask_before_go_url').val("");
}

function get_id_and_go(elemento,url,output){
	var id = elemento.id.split("_");
	go(url + id[1]);
}

function go(url,output){
	var teste = url.split(':');
	if(teste[0] == 'location'){
		location = teste[1];
	}else if(teste[0] == 'ask_before_go'){
		var msg     = teste[1];
		var new_url = teste[2];
		ask_before_go(msg,new_url);
	}else{ start_loading();
		$.ajax({
			url:url,
			cache: false
		}).done(function(html){
			stop_loading();
			if(output == undefined) output = "main";			
			$(output).html(html);
		});
	}
}

function show_select_and_go(url,output){ $("#" + output).stop().fadeIn();
	go(url,output);
}

function post(url){ start_loading();
	var inputs  = {};
	$(".input").each(function(){
		if($(this).val() == null){
			inputs[$(this).attr("name")] = "none";
		}else{
			inputs[$(this).attr("name")] = $(this).val();
		}		
	});

	$.post(url, inputs).done(function(data){ stop_loading();
		if(data != ""){
			if(data.substring(0,3) == "go:"){
				go(data.substring(3));
				close_form();
			}else if(data != "no-message"){
				alert(data);
			}
		}
  	});
}

function open_buttons(e,id){
	var next = e.nextElementSibling;
	if(has_class(next,"list-line-active")){
		add_class(next,"list-line-hidden");
		remove_class(next,"list-line-active");
	}else{
		var ativos = document.getElementsByClassName("list-line-active");
		for(var x = 0; x < ativos.length; x++){
			add_class(ativos[x],"list-line-hidden");
			remove_class(ativos[x],"list-line-active");
		}

		add_class(next,"list-line-active");
		remove_class(next,"list-line-hidden");

		$(".list-line-active").children("td").eq(0).children(".addons").children(".addon").each(function(){
			var id = $(this).attr("id");
			var aux = id.split("_");
			
			$("#" + id).html("carregando informações...");
			go("/" + aux[1] + "?id=" + aux[2], "#" + id);
		});
	}
}

var timer = "";
function searching(e){ clearTimeout(timer);
	timer = setTimeout(function(){
		if(e.placeholder == "Buscar Produtos"){
			go("/produtos/?q=" + e.value);
		}

		if(e.placeholder == "Buscar Mesas"){
			go("/mesas/?q=" + e.value);
		}
	},500);
}

function open_menu(){
    if(window.innerWidth < 600){
        $("#menus-container").slideToggle();    
    }else{
        $("#menus-container").slideDown();
    }
}

function close_menu(){
    if(window.innerWidth < 600){
        $("#menus-container").slideUp();    
    }else{
        $("#menus-container").slideDown();
    }
}

//MASK
function phoneMask(v) {
  var r = v.replace(/\D/g, "");
  
  r = r.replace(/^0/, "");
  if (r.length > 11) {
    r = r.replace(/^(\d\d)(\d{5})(\d{4}).*/, "($1) $2-$3");
  } else if (r.length > 7) {
    r = r.replace(/^(\d\d)(\d{5})(\d{0,4}).*/, "($1) $2-$3");
  } else if (r.length > 2) {
    r = r.replace(/^(\d\d)(\d{0,5})/, "($1) $2");
  } else if (v.trim() !== "") {
    r = r.replace(/^(\d*)/, "($1");
  }
  return r;
}

function telefone(e){
	e.value = phoneMask(e.value);
}
//MASK