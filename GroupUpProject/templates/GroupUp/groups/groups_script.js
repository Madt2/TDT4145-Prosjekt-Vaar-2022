
/* Variables */

let activeGroup = null;
let groupList = new Array();

/* Mock variables */
const groupAmount = 5;
const memberAmount = 15;
const matchAmount = 10;

/* "Classes" */

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

/* Functions */

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
}

//helper method
function getId(id) {
    return document.getElementById(id);
}

//function for adding html elements to display a list of the user's groups. This is displayed on the left of groups page.
//groups input is a list of group objects.
function addGroupsToList(groups) {
    /* Some function to get list of groups from database */


    let element = getId("groups_list");

    for (let i = 0; i < groups.length; i++) {
        let newGroupElement = document.createElement("div");
        newGroupElement.setAttribute("class", "group_list_element");
        newGroupElement.setAttribute("id", i.toString() + "_group_list_element");
        newGroupElement.setAttribute("onclick", "drawGroupPage(" + i + ")");

        let groupPicture = document.createElement("img");
        groupPicture.setAttribute("class", "group_list_image");
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
    element.classList.add("active");
    activeGroup = element;
}

//Function to clear and display active groups member on members page.
function refreshGroupMembers(members) {
    let memberCount = getId("member_count");
    memberCount.innerText = members.length;
    //Removes members of previous group loaded from html
    let memberList = getId("group_members");
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
        memberList.appendChild(groupMember);
    }
}

//Function for updating elements in the group page in gui.
function drawGroupPage(group_index) {
    let groupNr = group_index.valueOf();
    let groupElement = getId(group_index + "_group_list_element");
    changeGroupListElementColor(groupElement);

    getId("group_name").innerHTML = groupList[groupNr].name;
    getId("interest_var").innerHTML = groupList[groupNr].interest;
    getId("age_min_var").innerHTML = groupList[groupNr].minAge;
    getId("age_max_var").innerHTML = groupList[groupNr].maxAge;
    getId("contact_var").innerHTML = groupList[groupNr].contact;
    refreshGroupMembers(groupList[groupNr].members)
    constructGroupMatchList(groupList[group_index].matchList)
}

//Initialization function, run this as late as possible in html file.
function init() {
    initMockGroups()
    addGroupsToList(groupList);
    drawGroupPage("0");
}