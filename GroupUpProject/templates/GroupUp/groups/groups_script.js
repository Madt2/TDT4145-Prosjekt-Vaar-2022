
/* Variables */

let activeGroup = null;
const testList = ["group1", "group2", "group3",
                      "group4", "group5", "group6",
                      "group7", "group8", "group9",
                      "group10", "group11", "group12"];

const testMembers = ["member1", "member2", "member3", "member4", "member5"];

/* Functions */

function getId(id) {
    return document.getElementById(id);
}

function addGroupsToList() {
    /* Some function to get list of groups from database */


    let element = document.getElementById("groups_list");

    for (let i = 0; i < testList.length; i++) {
        let newGroupElement = document.createElement("div");
        newGroupElement.setAttribute("class", "group_element");
        newGroupElement.setAttribute("id", i.toString());
        newGroupElement.setAttribute("onclick", "drawGroupPage(" + i + ")");

        let groupPicture = document.createElement("img");
        groupPicture.setAttribute("class", "group_image");
        newGroupElement.appendChild(groupPicture);

        let groupTitle = document.createElement("p");
        let title = document.createTextNode(testList[i]);
        groupTitle.setAttribute("class", "group_title");
        groupTitle.appendChild(title);
        newGroupElement.appendChild(groupTitle);

        element.appendChild(newGroupElement);
    }
}

function changeGroupListElementColor(element) {
    if (activeGroup !== null) {
        activeGroup.classList.remove("active");
    }
    element.classList.add("active");
    activeGroup = element;
}

function drawGroupPage(group_index) {
    let groupNr = group_index.valueOf();
    let groupElement = getId(group_index);
    changeGroupListElementColor(groupElement);
    console.log(activeGroup);

    getId("group_name").innerHTML = testList[groupNr];
    let memberList = getId("group_members");
    while (memberList.firstChild) {
        parent.removeChild(parent.firstChild);
    }
    for (i = 0; i < testMembers.length; i++) {
        let groupMember = document.createElement("li");
        let text = document.createTextNode(testMembers[i]);
        groupMember.appendChild(text);
        memberList.appendChild(groupMember);
    }
}

function init() {
    addGroupsToList();
    drawGroupPage("0");
}