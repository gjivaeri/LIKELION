const textCount = document.querySelector("#content")
function cal(){
    document.getElementById('result').value = 
    document.getElementById('content').value.length;
}

textCount.addEventListener('keyup', cal)

let menuAll = document.querySelector(".menuAll");
let menu = document.querySelector(".menu");

menu.addEventListener("mouseout", function(){
    menuAll.style.display = "none";
    menu.textContent="MENU"
    menu.style.fontSize ="50px"
  })
menu.addEventListener("mouseover", function(){
    menuAll.style.display = "block";
    menu.textContent=''
})