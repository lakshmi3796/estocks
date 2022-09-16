$(document).on("submit", "#formBtn", function(e) {
    e.preventDefault();
    finddata();
});

function finddata(){
    stockname = document.getElementById("select-stock").value;
    start_date = document.getElementById("fromDate").value
    end_date = document.getElementById("toDate").value;
    if (start_date>end_date){
        alert("Start Date can not be greater than End Date")
        return;
    }
    $.ajax({
        url: '{% homepage %}',
        type: "POST",
        async: true,
        data: {
            stockname:stockname,
            start_date:start_date,
            end_date:end_date,
            csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function(response){
            console.log(response)
            
        }
        });
}

