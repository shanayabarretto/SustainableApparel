chrome.runtime.onMessage.addListener((msg, sender, response) => {
    console.log("recieved")
    let brand = document.querySelector('table tbody .po-brand td:nth-child(2) span');
    //getInfo();
    console.log(brand.textContent);
    response({value: brand.textContent}); 
});