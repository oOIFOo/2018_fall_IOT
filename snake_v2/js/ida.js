 var xx=320;
 var yy=240;
 $(function(){
        set_endpoint('http://iottalk2.tw:9992');
		set_PUSH_INTERVAL(200);  // unit: ms
		
        var profile = {
		    'dm_name': 'snake', 
            'idf_list':[[Gyroscope,['None']]],		
		    'odf_list':[[moves,['None']]],			
		    'd_name' : undefined
        };
		
		function Gyroscope(){
		    return;
		}
		
        function moves(data){
            if(315 < data[0]|| data[0] < 45) xx = xx + 10;
			else if(45 < data[0] && data[0] < 135)yy = yy - 10;
			else if(135 < data[0] && data[0] < 225)xx = xx - 10;
			else if(225 < data[0] && data[0] < 315) yy = yy + 10
        }
      
/*******************************************************************/                
        function ida_init(){console.log('Success.');}
        var ida = {
            'ida_init': ida_init,
        }; 
        dai(profile,ida);     
});
