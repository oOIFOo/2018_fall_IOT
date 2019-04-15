 $(function(){
        csmapi.set_endpoint ('http://140.113.199.189:9999');
        var profile = {
		    'dm_name': 'OIFO',          
			'idf_list':[OIFOI],
			'odf_list':[OIFOO],			
        };
		
        function OIFOI(){
            return Math.random();
        }

        function OIFOO(data){
           if(data[2] > 0) $('.ODF_value')[0].innerText=[data[0],data[1],data[2]];
		   else  $('.ODF_value')[0].innerText= " ";
        }
      
/*******************************************************************/                
        function ida_init(){
			console.log(profile.d_name);
	    }
        var ida = {
            'ida_init': ida_init,
        }; 
        dai(profile,ida); 
});
