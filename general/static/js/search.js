let formHeader = document.querySelector(".submit");
formHeader.addEventListener("click", function (event) {
    event.preventDefault();
    let nameHeader = document.querySelector(".search").value;
    window.location.replace("/your_food/"+nameHeader);
    })

let form = document.querySelector(".submit1");
form.addEventListener("click", function (event) {
    event.preventDefault();
    let name = document.querySelector(".search1").value;
    window.location.replace("/your_food/"+name);
    })
