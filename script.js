document.addEventListener('DOMContentLoaded', function() {
    const collapseContentButton = document.getElementById('chevron');
    const content = document.getElementById('content')
     
    if (collapseContentButton) {
        const applyCollapse = () => {
            // Allow closed content option to persist throughout pages (localStorage)
            let collapseContent = JSON.parse(localStorage.getItem("collapseContent"));
            collapseContentButton.classList.toggle('closed', Boolean(collapseContent));
            content.classList.toggle('closed', Boolean(collapseContent));   
        }
        
        collapseContentButton.addEventListener('click', () => {
            collapseContent = !JSON.parse(localStorage.getItem("collapseContent")); // case local storage empty: !null => true
            localStorage.setItem("collapseContent", JSON.stringify(collapseContent));
            applyCollapse();
        });
        window.addEventListener('pageshow', applyCollapse); // Rerun if e.g. page loaded from cache

        applyCollapse();
    }
});

