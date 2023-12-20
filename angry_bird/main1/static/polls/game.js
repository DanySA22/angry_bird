var pipe = document.getElementById("pipe");
var hole = document.getElementById("hole");
var angry_bird = document.getElementById("angry_bird");
var jumping = 0;
var counter = 0;

hole.addEventListener('animationiteration', () => {
    var random = -((Math.random()*700)+400);
    hole.style.top = random + "px";
    counter++;  //means that with each hole iteration the top position will randomly change from -400px to -1100px
});
setInterval(function(){
    var angry_birdTop = parseInt(window.getComputedStyle(angry_bird).getPropertyValue("top"));
    if(jumping==0){
        angry_bird.style.top = (angry_birdTop + 3)+"px"; //This determinate going down you can increase that 3 number to make it go down faster in a harder level.
    }
    var pipeLeft = parseInt(window.getComputedStyle(pipe).getPropertyValue("left"));
    var holeTop = parseInt(window.getComputedStyle(hole).getPropertyValue("top"));
    var cTop = -(1100-angry_birdTop);
    if((angry_birdTop>1050)||((pipeLeft<50)&&(pipeLeft>-50)&&((cTop<holeTop)||(cTop>holeTop+350)))){
        alert("Game over. Score: "+(counter-1));
        angry_bird.style.top = 500 + "px";
        counter=0;
    }
},10);   //the function inside the interval will be executed every 10 msec and all his variable information get
// updated in that frame of time

function jump(){
    jumping = 1; //this means that the jumping variable is always equal to 0 unless the jump() function is currently running 
    let jumpCount = 0;  //keep track of how many times this interval is run because we don’t want to be jumping forever. We want to jump and then go down
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