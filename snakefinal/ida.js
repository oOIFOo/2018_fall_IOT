 var xx=620;
 var yy=440;
 var xx_t;
 var yy_t;
 var xxx = 10;
 var yyy = 100;
 var xxx_t;
 var yyy_t;
 var velocity = 20;
 var velocity2 = 20;
 function reset1(){
	xx=620; 
	yy=440; 
	xxx = 10; 
	yyy = 100; 
	velocity = 20;
    velocity2 = 20;	
 }
 $(function(){
        set_endpoint('http://iottalk2.tw:9992');
		set_PUSH_INTERVAL(10);  // unit: ms
		
        var profile = {
		    'dm_name': 'snake0616030', 
            'idf_list':[[Gyroscope,['None']]],		
		    'odf_list':[[moves1,moves2,['None']]],			
		    'd_name' : undefined
        };
		
		function Gyroscope(){
		    return;
		}
		
        // function moves(data){
            // if(315 < data[0]|| data[0] < 45) xx = xx + velocity;
			// else if(45 < data[0] && data[0] < 135)yy = yy - velocity;
			// else if(135 < data[0] && data[0] < 225)xx = xx - velocity;
			// else if(225 < data[0] && data[0] < 315) yy = yy + velocity;
        // }
            function moves1(data){
            tempx = xx + Math.cos((data[0]-90)*Math.PI/180)*velocity;
            tempy = yy - Math.sin((data[0]-90)*Math.PI/180)*velocity;
            if(tempx > 10 && tempx < 640)
                xx = tempx;
            else if(tempx < 10)
                xx = 10;
            else if(tempx > 640)
                xx = 640;
            if(tempy > 10 && tempy < 480)
                yy = tempy;
            else if(tempy < 10)
                yy = 10;
            else if(tempy > 480)
                yy = 480;
	    }
        function moves2(data){
            tempxxx = xxx + Math.cos((data[0]-90)*Math.PI/180)*velocity2;
            tempyyy = yyy - Math.sin((data[0]-90)*Math.PI/180)*velocity2;
            if(tempxxx > 10 && tempxxx < 640)
                xxx = tempxxx;
            else if(tempxxx < 0)
                xxx = 10;
            else if(tempxxx > 640)
                xxx = 640;
            if(tempyyy > 10 && tempyyy < 480)
                yyy = tempyyy;
            else if(tempyyy < 10)
                yyy = 10;
            else if(tempyyy > 480)
                yyy = 480;
       }

	   
/*******************************************************************/                
        function ida_init(){console.log('Success.');}
        var ida = {
            'ida_init': ida_init,
        }; 
        dai(profile,ida);     
});
