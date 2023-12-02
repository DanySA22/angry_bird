/* function myFunction() {
    document.getElementById("demo1").innerHTML = alert("Que bola");
} */


/*function Jump()  {
    document.getElementById("angry_bird").innerHTML =
    alert("Just testing");
}*/

var pipe = document.getElementById("pipe");
var hole = document.getElementById("hole");
var angry_bird = document.getElementById("angry_bird");
var jumping = 0;
var counter = 0;

hole.addEventListener('animationiteration', () => {
    var random = -((Math.random()*700)+400);
    hole.style.top = random + "px";
    counter++;
});
setInterval(function(){
    var angry_birdTop = parseInt(window.getComputedStyle(angry_bird).getPropertyValue("top"));
    if(jumping==0){
        angry_bird.style.top = (angry_birdTop+3)+"px";
    }
    var pipeLeft = parseInt(window.getComputedStyle(pipe).getPropertyValue("left"));
    var holeTop = parseInt(window.getComputedStyle(hole).getPropertyValue("top"));
    var cTop = -(1100-angry_birdTop);
    if((angry_birdTop>1050)||((pipeLeft<50)&&(pipeLeft>-50)&&((cTop<holeTop)||(cTop>holeTop+350)))){
        alert("Game over. Score: "+(counter-1));
        angry_bird.style.top = 500 + "px";
        counter=0;
    }
},10);

function jump(){
    jumping = 1;
    let jumpCount = 0;
    var jumpInterval = setInterval(function(){
        var angry_birdTop = parseInt(window.getComputedStyle(angry_bird).getPropertyValue("top"));
        if((angry_birdTop>20)&&(jumpCount<15)){
            angry_bird.style.top = (angry_birdTop-20)+"px";
        }
        if(jumpCount>20){
            clearInterval(jumpInterval);
            jumping=0;
            jumpCount=0;
        }
        jumpCount++;
    },10);
}