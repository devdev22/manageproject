

var modal = document.getElementById('taskModal');
var btnModal = document.getElementById('btnModal');
var btnClose =document.getElementById('btnClose');

btnModal.addEventListener('click', openModal);

btnClose.addEventListener('click', closeModal);

window.addEventListener('click', clickOutside);

function openModal(e){
   modal.style.display = 'block';
   e.preventDefault();
}

function closeModal(){
    modal.style.display = 'none';
}


function clickOutside(e){
    if(e.target==modal){
        modal.style.display = 'none';
    }
    
}

