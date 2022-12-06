function volume(){
    var vol;
    var lenght = Number(document.getElementById("lenght").value);
    var width = Number(document.getElementById("width").value);
    var height = Number(document.getElementById("height").value);
    vol = lenght*width*height/1000;
    document.getElementById("vol").innerHTML = vol;
    return vol;
}

function values(){
    var vol = volume();
    var val;
    if(vol > 5){
        val = (vol-5)*5.5+55;
    }else val = 55;
        document.getElementById("val").innerHTML = val;
return val;
}

function logist(){
    var val = values();
    var proc = Number(document.getElementById("proc").value);
    log = (val+(100-proc)/100*33)/(1-(100-proc)/100);
    document.getElementById("log").innerHTML = log.toFixed(2);
}