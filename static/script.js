function createPost() {
    document.getElementById("createPostContainer").style.display = "block";
    document.getElementById("contentList").style.display = "none";
    document.getElementById("logContent").style.display = "none";
    return true;
}

function closePost() {
    document.getElementById("createPostContainer").style.display = "none";
    document.getElementById("contentList").style.display = "block";
    document.getElementById("logContent").style.display = "block";
}