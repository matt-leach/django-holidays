function submitHoliday(staffId, year) {
	$.ajax({
            url : "/holidays/add/",
            type : "POST",
            data : { "user_id": staffId, "start_date": $("#id_start_date").val(), "end_date": $("#id_end_date").val() },
            
            // handle a successful response
            success : function(json) {
                $("#holidays_" + staffId + "_" + year).replaceWith(json);
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                alert("failed");
            }
        });
}


function loadHolidays(staffId, year) {
	$.ajax({
	    url: '/holidays/getYearly/',
	    data: {"year": year, "userid": staffId},
	    type: 'get', 
	    success: function(data) {   
	        $("#holidays_" + staffId + "_" + year).replaceWith(data);
	    },
	    failure: function(data) { 
	        alert('Got an error');
	    }
	}); 
}