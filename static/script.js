function createPost() {
    document.getElementById("createPostContainer").style.display = "block";
    return true;
}

function closePost() {
    document.getElementById("title_input").value = "";
    document.getElementById("content_input").value = "";
    document.getElementById("createPostContainer").style.display = "none";
}