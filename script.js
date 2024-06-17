function openNav() {
    document.getElementById("myMenu").style.height = "100%";
}
  
/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
    document.getElementById("myMenu").style.height = "0";
}
  
function toggle_ls() {
    let button = document.getElementById("ls-button");
    if (button.textContent == "condense") {
        button.textContent = "expand"
        document.getElementById("long").style.display = "none";
        document.getElementById("short").style.display = "block";
    } else {
        button.textContent = "condense"
        document.getElementById("long").style.display = "block";
        document.getElementById("short").style.display = "none";
    }
}