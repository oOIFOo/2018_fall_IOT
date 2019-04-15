 var xxx=320;
 var yyy=240;
 $(function(){
	    csmapi.set_endpoint ('http://140.113.199.189:9999');
        var profile = {
		    'dm_name': 'snakes',          
			'odf_list':[moves],
            'd_name' : undefined			
        };
		
        function moves(data){
		   xxx = data[0];
		   yyy = data[1];
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
