$(function () {
	csmapi.set_endpoint ('http://140.113.199.189:9999');
	var profile = {
		'dm_name': 'Bulb',          
		'odf_list':[Color_O ,Luminance]
	}
    var r,g,b,lum;
	
	function draw () {
		var rr = Math.floor((r * lum) / 100);
		var gg = Math.floor((g * lum) / 100);
		var bb = Math.floor((b * lum) / 100);
		$('.bulb-top, .bulb-middle-1, .bulb-middle-2, .bulb-middle-3, .bulb-bottom, .night').css(
			{'background': 'rgb('+ rr +', '+ gg +', '+ bb +')'}
		);
	}
	
	function Color_O (data) {
		console.log(data);
		r = data[0];
		g = data[1];
		b = data[2];
		draw();
	}
	
	function Luminance (data) {
		console.log(data);
		lum = data[0];
		draw();
	}
	
	function ida_init(){
			console.log(profile.d_name);
			$('.font123')[0].innerText= profile.d_name;
	    }
        var ida = {
            'ida_init': ida_init,
        }; 
        dai(profile,ida);
});
