const userAction = async (endpoint) => {
    const response = await fetch(endpoint);
    const myJson = await response.json(); //extract JSON from the http response
    return myJson;
}

function get_info(brand) {
    brand = String(brand).replace(/\s/g, '');
    const endpoint = "https://cryptic-badlands-22652.herokuapp.com/https://sustainable-style.herokuapp.com/" + brand;
    myJson = userAction(endpoint);
    console.log(brand);
    document.getElementById("header").innerHTML = String(brand);
    document.getElementById("scores").innerHTML = myJson;
}

document.addEventListener("DOMContentLoaded", function(){ load(); }, false);
function load() {
    console.log("hey")
    chrome.tabs.query({currentWindow: true, active: true}, function (tabs){
        var activeTab = tabs[0];
        chrome.tabs.sendMessage(activeTab.id, {type: "getText"}, function(response) {
            get_info(response.value);
    }); 
})};
