const collapseContentButton = document.getElementById('chevron');
const content = document.getElementById('content')
 
if (collapseContentButton) {
    // Allow closed content to persist throughout pages (localStorage)
    let collapseContent = JSON.parse(localStorage.getItem("collapseContent"));
    if (collapseContent) {
        collapseContentButton.classList.toggle('closed', true);
        content.classList.toggle('closed', true);
    }
    
    collapseContentButton.addEventListener('click', () => {
        collapseContent = !collapseContent; // unset: !null => true
        localStorage.setItem("collapseContent", JSON.stringify(collapseContent));
        collapseContentButton.classList.toggle('closed', collapseContent);
        content.classList.toggle('closed', collapseContent);
    });
}
