function openChatWindow() {
    document.getElementById("chatBox").style.display = "block";
    localStorage.setItem("chatOpen", "true"); /* Stores status of chatwindow */
}

function closeChatWindow() {
    document.getElementById("chatBox").style.display = "none";
    localStorage.setItem("chatOpen", "false"); /* Stores status of chatwindow */
}
