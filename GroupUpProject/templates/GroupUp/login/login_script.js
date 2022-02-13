
function getId(id) {
    return document.getElementById(id);
}

function show_register_overlay() {
    getId('login_module').style.display = 'none';
    getId('register_module').style.display = 'block';
}

function show_login_overlay() {
    getId('register_module').style.display = 'none';
    getId('login_module').style.display = 'block';
}

