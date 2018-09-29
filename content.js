// content.js
console.log("Hello from your Chrome extension!");

// content.js
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "clicked_browser_action" ) {
      console.log("Clicked on browser");
    }
  }
);
