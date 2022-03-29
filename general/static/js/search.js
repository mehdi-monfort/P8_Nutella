var form = document.querySelector(".submit");
form.addEventListener("click", function (event) {
    event.preventDefault();
    var name = document.querySelector(".usertext").value;
    window.location.replace("your_food/"+name);
    })

var form1 = document.querySelector(".submit1");
form1.addEventListener("click", function (event) {
    event.preventDefault();
    var name = document.querySelector(".search1").value;
    window.location.replace("your_food/"+name);
    })