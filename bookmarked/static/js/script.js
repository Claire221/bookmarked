document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);


    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);

    console.log(elems)
});
