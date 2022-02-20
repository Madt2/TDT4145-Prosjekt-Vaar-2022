
function getId(id) {
    return document.getElementById(id);
}

function loadInfoContainer() {
    let infoContainer = getId("group_info_form_container");
    let addMemberContainer = getId("group_member_form_container");
    infoContainer.classList.remove("active");
    addMemberContainer.classList.add("active");
}

function loadAddMemberContainer() {
    let infoContainer = getId("group_info_form_container");
    let addMemberContainer = getId("group_member_form_container");
    infoContainer.classList.add("active");
    addMemberContainer.classList.remove("active");
}

function init() {
    loadInfoContainer()
}