var idx = 1;
function changeImage(){
    idx++;
    if(idx>3){
        idx=1;
    }
    location.reload(true);
}