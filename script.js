document.addEventListener('DOMContentLoaded', function() {
    //
    // Navbar
    //
    const navItems = document.querySelectorAll('.nav-item');
    const subMenus = document.querySelectorAll('.inner-nav')
    // close all submenus except for e.g. class "blog"
    const closeNavMenus = (except) => {
        navItems.forEach(navItem => {
            if (navItem.id !== except) navItem.classList.remove('active');
        });
        subMenus.forEach(subMenu => {
            if (!subMenu.classList.contains(except)) subMenu.classList.remove('active');
        });
    }

    navItems.forEach(navItem => {
        navItem.addEventListener('click', function(e) {
            e.preventDefault();

            closeNavMenus(navItem.id);
            navItem.classList.toggle('active');
            document.querySelector(`.inner-nav.${navItem.id}`)
                .classList.toggle('active');
        });
    });
    
    // Close submenus when clicking outside of them
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.nav-item, .inner-nav')) {
            closeNavMenus();
        }
    });

    //
    // Collapse file index contents in notebooks
    //
    const collapseContentButton = document.getElementById('chevron');
    const content = document.getElementById('content');
     
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

