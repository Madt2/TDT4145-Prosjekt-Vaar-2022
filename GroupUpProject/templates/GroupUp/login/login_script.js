
function getId(id) {
    return document.getElementById(id);
}

function show_register_overlay() {
    getId('login').style.display = 'none';
    getId('register_user').style.display = 'block';
}

function show_login_overlay() {
    getId('register_user').style.display = 'none';
    getId('login').style.display = 'block';
}