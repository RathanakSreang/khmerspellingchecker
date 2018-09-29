// background.js

console.log("Clicked on browser");
// Called when the user clicks on the browser action.
chrome.browserAction.onClicked.addListener(function(tab) {
  // Send a message to the active tab
    console.log("Clicked on browser");
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    console.log("Clicked on browser");
    var activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, {"message": "clicked_browser_action"});
  });
});
