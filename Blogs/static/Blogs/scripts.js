function start(click){
    // var e=document.querySelector("#click");
    if(document.querySelector("."+('container1'+"-"+click)).classList.contains("active")){
        document.querySelector("."+('container1'+"-"+click)).classList.remove("active")
        document.querySelector("."+('container1'+"-"+click)).classList.add("inactive")

    }
    else{
        document.querySelector("."+('container1'+"-"+click)).classList.remove("inactive")
        var check=document.querySelector("."+('container1'+"-"+click)+"active");
        var e1=document.querySelector("."+('container1'+"-"+click));
        e1.classList.add('active');

        // console.log(e1);
        console.log(e1);
    }
}