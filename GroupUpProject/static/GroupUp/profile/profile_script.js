
function getId(id) {
    return document.getElementById(id);
}

function open_delete_window() {
    console.log("hei")
    getId('delete_window_container').style.display = 'flex';
}

function close_delete_window() {
    getId('delete_window_container').style.display = 'none';
}