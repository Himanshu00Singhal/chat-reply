console.log("Chat Assistant running...");

function getLastMessage() {
  let messages = document.querySelectorAll("div.message-in, div.message-out");
  if (messages.length > 0) {
    return messages[messages.length - 1].innerText;
  }
  return "";
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "get_last_message") {
    let message = getLastMessage();
    sendResponse({ lastMessage: message });
  }
});
