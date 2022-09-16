$(document).ready(function(){
    $("#btn").click(function(e) {
        e.preventDefault();
        finddata();
    });
});

function finddata(){
    stockname = document.getElementById("select-stock").value;
    start_date = document.getElementById("fromDate").value
    end_date = document.getElementById("toDate").value;
    if (start_date == "" || end_date=="" || stockname ==""){
        alert("All fields are mandatory to fill.")
        return;
    }
    if (start_date>end_date){
        alert("Start Date can not be greater than End Date")
        return;
    }
    document.getElementById("result").style.display="none";
    var res = document.createElement("div")
    res.id = "result1"
    res.style.width = "70%";
    res.style.marginLeft = "145px";
    res.style.padding = "40px";
    var p = document.createElement("p")
    console.log(res)
    $.ajax({
        url: "/home",
        type: "GET",
        async: true,
        data: {
            stockname:stockname,
            start_date:start_date,
            end_date:end_date,
        },
        success: function(response){
            console.log(response)
            if (response.data.includes('<td>')){
            var textnode = document.createTextNode("The "+stockname.toString()+" stock details is shown below:")
            p.appendChild(textnode)
            res.appendChild(p)
            res.insertAdjacentHTML('beforeend',response.data.replaceAll("\n",""));
            var element = document.getElementById("main");
            element.appendChild(res);}
            else{
                var textnode = document.createTextNode("Opps! No records found with "+stockname.toString()+" stock between given date range:")
                p.appendChild(textnode)
                res.appendChild(p)
                var element = document.getElementById("main");
                element.appendChild(res);
            }
        }
        });
}

