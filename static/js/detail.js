$(function(){ 

	$(".add").click(function(){ 
		
		var t=$(this).parent().find('input[class*="num_show"]');
		t.val(parseInt(t.val())+1); 
		$(".num_show").trigger("change");	
		setTotal(); 
	}); 

	$(".minus").click(function(){ 
		$(".num_show").trigger("change");
		var t=$(this).parent().find('input[class*="num_show"]'); 
		t.val(parseInt(t.val())-1) 
		if(parseInt(t.val()-1)<1){ 
			t.val(1); 
		}
		setTotal();
		$(".num_show").trigger("change");
	}); 

	function setTotal(){ 
		var s=0; 
		s=(parseInt($(".num_show").val())*parseFloat($(".show_pirze > em").html())).toFixed(2); 
		$(".total").children(":first").html(s);
	
	}

$('.num_show').change(function(){
		$('.buy_btn').attr({href:$('.buy_btn').attr('href').split('?')[0]+'?id='+$('.add_cart').attr('value')+'&&count='+$('.num_show').val()})
})
		

	$('#add_cart').click(function(){
			$.ajax({
   	 	url: '/addcart/',
    	type: 'POST',
    	dataType: 'json',
    	data:{'goodsName':$('.add_cart').attr('value'),'buyCount':$('.num_show').val()}
	})
	.done(function(data) {
			$('#show_count').html(data.number);
		
		}
	)
	.fail(function() {
		// error_name = 'True';
		window.location.href='/login/'
    // alert('服务器超时，请重试！');
	});
}
		)

$(".num_show").trigger("change");
}) 