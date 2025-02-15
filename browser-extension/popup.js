document.getElementById("getSuggestion").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.tabs.sendMessage(tabs[0].id, { action: "get_last_message" }, (response) => {
        if (response && response.lastMessage) {
          fetch("http://localhost:8000/generate-reply", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: response.lastMessage, chat_history: [] })
          })
            .then(res => res.json())
            .then(data => {
              document.getElementById("response").innerText = "AI Suggestion: " + data.reply;
            })
            .catch(console.error);
        }
      });
    });
  });
  