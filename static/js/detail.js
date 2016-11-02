$(function(){ 
	$(".add").click(function(){ 
		var t=$(this).parent().find('input[class*="num_show"]');
		t.val(parseInt(t.val())+1) 	
		setTotal(); 
	}); 

	$(".minus").click(function(){ 
		var t=$(this).parent().find('input[class*="num_show"]'); 
		t.val(parseInt(t.val())-1) 
		if(parseInt(t.val()-1)<1){ 
			t.val(1); 
		}
		setTotal();
	}); 

	function setTotal(){ 
		var s=0; 
		s=(parseInt($(".num_show").val())*parseFloat($(".show_pirze > em").html())).toFixed(2); 
		$(".total").children(":first").html(s);
	}
}) 