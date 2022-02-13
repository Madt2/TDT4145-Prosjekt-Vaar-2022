
function getId(id) {
    return document.getElementById(id);
}

function addGroupsToList() {
    /* Some function to get list of groups from database */
    const testList = ["test1", "test2", "test3",
                      "test4", "test5", "test6",
                      "test7", "test8", "test9",
                      "test10", "test11", "test12"];

    let element = document.getElementById("groups_list");

    for (let i = 0; i < testList.length; i++) {
        let newGroupElement = document.createElement("div");
        newGroupElement.setAttribute("class", "group_element");
        newGroupElement.setAttribute("id", i.toString());
        newGroupElement.setAttribute("onclick", "drawGroupPage(" + i + ")");

        let groupPicture = document.createElement("img")
        groupPicture.setAttribute("class", "group_image");
        newGroupElement.appendChild(groupPicture);

        let groupTitle = document.createElement("p");
        let title = document.createTextNode("title");
        groupTitle.setAttribute("class", "group_title");
        groupTitle.appendChild(title);
        newGroupElement.appendChild(groupTitle);

        element.appendChild(newGroupElement);
    }
}

function drawGroupPage(group_index) {
    let groupNr = group_index.valueOf();
    let groupElement = getId(group_index);
    groupElement.getAttribute("background-color")
    console.log(groupElement.getAttribute("background-color"));
    groupElement.setAttribute("background-color", "blue");
}