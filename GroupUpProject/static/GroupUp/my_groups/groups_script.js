
function getId(id) {
    return document.getElementById(id);
}

function handleNoGroups() {
    let containerElements = getId("content_container").children;
    let hasGroupCard = false;
    for (let i = 0; i < containerElements.length; i++) {
        let a_href = containerElements.children;
        for (let i = 0; i < a_href.length; i++) {
            if (containerElements[i].classList.contains('group_card')) {
                console.log("hei");
                hasGroupCard = true;
            }
        }
    }
    console.log(containerElements);

    console.log(hasGroupCard);
    if (!hasGroupCard) {
        const container = getId("content_container");
        container.style.display = "flex";
        const text = getId("noGroupText");
        text.style.display = "block";

    }
}

//old code:

/*

// Variables

let activeGroup = null;
let activeEditMember = null;
let groupList = new Array();

// Mock variables
const groupAmount = 20;
const memberAmount = 35;
const matchAmount = 20;

// "Classes"

//Member "class", use this to create a member object with "new member(string name, string id(email), int age, boolean isLeader)".
function member(memberName, memberId, memberAge, isLeader) {
    this.name = memberName;
    this.id = memberId;
    this.age = memberAge;
    this.isLeader = isLeader;
}

//Match "class", use this to create a match object (which belongs to a group) with "new match(string name, string interest, string contactInfo)".
function match(matchName, matchInterest, matchContact) {
    this.name = matchName;
    this.interest = matchInterest;
    this.contact = matchContact;
}

//Group "class", use this to create a group object with "new group(string name, string interest, string contactInfo, Array memberList, Array groupMatchList)".
function group(groupName, groupInterest, contactInfo, memberList, groupMatchList) {
   this.name = groupName;
   this.imageLink = null;
   this.interest = groupInterest;
   this.leader = null;
   this.minAge = null;
   this.maxAge = null;
   this.contact = contactInfo;
   this.members = memberList;
   this.matchList = groupMatchList;
   for (let i = 0; i < this.members.length; i++) {
       if ((this.minAge == null) || (this.minAge > memberList[i].age)) {
           this.minAge = memberList[i].age;
       }
       if ((this.maxAge == null) || (this.maxAge < memberList[i].age)) {
           this.maxAge = memberList[i].age;
       }
       if (memberList[i].isLeader) {
           this.leader = memberList[i];
       }
   }
}

// Functions

//function for creating fake group items to test/demonstrate how the gui displays items:
function initMockGroups() {
    for (let i = 0; i < groupAmount; i++) {
        let testMembers = new Array();
        for (let j = 0; j < memberAmount - 1; j++) {
            testMembers.push(new member("member" + j, "member" + j + "@mail.com", 20 + j, false));
        }
        testMembers.push(new member("testLeader", "leader@mail.com", 20, true));

        let matches = new Array();
        for (let j = 0; j < matchAmount; j++) {
            matches.push(new match("match" + j, "interest", "group" + j + "mail@mail.com"))
        }
        groupList.push(new group("group" + i, "An interest", "group" + i + "@mail.com", testMembers, matches));
    }
    groupList[0].imageLink = "https://d3t3ozftmdmh3i.cloudfront.net/production/podcast_uploaded/2768983/2768983-1575334973329-68d1c3ac9b5de.jpg";
}

//helper method


//function for adding html elements to display a list of the user's groups. This is displayed on the left of groups page.
//groups input is a list of group objects.
function addGroupsToList(groups) {
    let element = getId("groups_list");

    for (let i = 0; i < groups.length; i++) {
        let newGroupElement = document.createElement("div");
        newGroupElement.setAttribute("class", "group_list_element");
        newGroupElement.setAttribute("id", i.toString() + "_group_list_element");
        newGroupElement.setAttribute("onclick", "drawGroupPage(" + i + ")");

        let groupPicture = document.createElement("img");
        groupPicture.setAttribute("class", "group_list_image");
        if (groups[i].imageLink !== null) {
            groupPicture.setAttribute("src", groups[i].imageLink);
        } else {
            groupPicture.setAttribute("src", "https://static.vecteezy.com/system/resources/thumbnails/000/550/535/small/user_icon_007.jpg");
        }
        newGroupElement.appendChild(groupPicture);

        let groupTitle = document.createElement("p");
        let title = document.createTextNode(groups[i].name);
        groupTitle.setAttribute("class", "group_list_title");
        groupTitle.appendChild(title);
        newGroupElement.appendChild(groupTitle);

        element.appendChild(newGroupElement);
    }
}

//Function for drawing the groups matches on a groups page, this is displayed at the bottom of a group page.
//Input matches is a list of match objects to display.
function constructGroupMatchList(matches) {
    let matchList = getId("match_list");

    while (matchList.firstChild) {
        matchList.removeChild(matchList.firstChild);
    }

    for (let i = 0; i < matches.length; i++) {
        let newMatchElement = document.createElement("div");
        newMatchElement.setAttribute("class", "match_element");

        let matchTitleBox = document.createElement("div");
        matchTitleBox.setAttribute("class", "match_box");
        let matchTitle = document.createElement("p");
        matchTitle.setAttribute("class", "match_text");
        let title = document.createTextNode(matches[i].name);
        matchTitle.appendChild(title);
        matchTitleBox.appendChild(matchTitle);

        let matchInterestBox = document.createElement("div");
        matchInterestBox.setAttribute("class", "match_box");
        let matchInterest = document.createElement("p");
        matchInterest.setAttribute("class", "match_text");
        let interestText = document.createTextNode(matches[i].interest);
        matchInterest.appendChild(interestText);
        matchInterestBox.appendChild(matchInterest);

        let matchContactBox = document.createElement("div");
        matchContactBox.setAttribute("class", "match_box");
        let matchContact = document.createElement("p");
        matchContact.setAttribute("class", "match_text");
        let contactText = document.createTextNode(matches[i].contact);
        matchContact.appendChild(contactText);
        matchContactBox.appendChild(matchContact);

        newMatchElement.appendChild(matchTitleBox);
        newMatchElement.appendChild(matchInterestBox);
        newMatchElement.appendChild(matchContactBox);
        matchList.appendChild(newMatchElement);
    }
}

//Function to make the selected group element in the groups list (left on the groups page) highlighted
function changeGroupListElementColor(element) {
    if (activeGroup !== null) {
        activeGroup.classList.remove("active");
    }
    activeGroup = element;
    element.classList.add("active");

    let form = getId("edit_group_form").reset();
    setViewToGroupPage();
}

function editActiveEditMember(member) {
    let element = getId(member);
    if (activeEditMember !== null) {
        activeEditMember.classList.remove("active");
    }
    activeEditMember = element;
    element.classList.add("active");
    console.log(activeEditMember)
}

//Function to clear and display active groups member on members page.
function refreshGroupMembers(members) {
    let memberCount = getId("member_count");
    memberCount.innerText = members.length;
    let memberList = getId("group_members");

    //Removes members of previous group loaded from html
    while (memberList.firstChild) {
        memberList.removeChild(memberList.firstChild);
    }
    //Adds members for selected group to html list
    for (let i = 0; i < members.length; i++) {
        let groupMember = document.createElement("li");
        let text;
        if (members[i].isLeader) {
            text = document.createTextNode(members[i].name + " (Leader)");
        } else {
            text = document.createTextNode(members[i].name);
        }
        groupMember.appendChild(text);
        groupMember.setAttribute("class", "member_element")
        memberList.appendChild(groupMember);
    }
}

function refreshEditMembersList(members) {
    let editMemberList = getId("edit_members_list");

    while (editMemberList.firstChild) {
        editMemberList.removeChild(editMemberList.firstChild);
    }
    //Adds members for selected group to html list
    for (let i = 0; i < members.length; i++) {
        let groupMember = document.createElement("li");
        let text;
        if (members[i].isLeader) {
            text = document.createTextNode(members[i].name + " (Leader)");
        } else {
            text = document.createTextNode(members[i].name);
        }
        groupMember.appendChild(text);
        groupMember.setAttribute("class", "member_element");
        groupMember.setAttribute("id", "member_Edit_list_element_" + i.toString());
        groupMember.setAttribute("onclick", "editActiveEditMember(\"member_Edit_list_element_" + i.toString() + "\")");
        editMemberList.appendChild(groupMember);
    }
}

//Function for updating elements in the group page in gui.
function drawGroupPage(group_index) {
    let groupNr = group_index.valueOf();
    let groupElement = getId(group_index + "_group_list_element");
    let groupImage = getId("group_image")
    changeGroupListElementColor(groupElement);

    getId("group_name").innerHTML = groupList[groupNr].name;
    getId("interest_var").innerHTML = groupList[groupNr].interest;
    getId("age_min_var").innerHTML = groupList[groupNr].minAge;
    getId("age_max_var").innerHTML = groupList[groupNr].maxAge;
    getId("contact_var").innerHTML = groupList[groupNr].contact;

    if (groupList[groupNr].imageLink !== null) {
            groupImage.setAttribute("src", groupList[groupNr].imageLink);
        } else {
            groupImage.setAttribute("src", "https://static.vecteezy.com/system/resources/thumbnails/000/550/535/small/user_icon_007.jpg");
        }

    refreshGroupMembers(groupList[groupNr].members);
    refreshEditMembersList(groupList[groupNr].members);
    constructGroupMatchList(groupList[group_index].matchList);
}



function toggleEditPage() {
    const groupPage = getId("group_page");
    const editPage = getId("group_edit_page");
    groupPage.classList.toggle("active");
    editPage.classList.toggle("active");
}

function setViewToGroupPage() {
    const groupPage = getId("group_page");
    const editPage = getId("group_edit_page");
    groupPage.classList.remove("active");
    editPage.classList.add("active");
}

//Initialization function, run this as late as possible in html file.
function init() {
    setViewToGroupPage();
    initMockGroups();
    addGroupsToList(groupList);
    drawGroupPage("0");
}

*/