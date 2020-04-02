const byId = (id) => document.getElementById(id);

function responsiveFooter() {
    if (window.innerWidth <= document.body.clientWidth) {
        byId('footer').class += ' fixed-bottom';
    }
}