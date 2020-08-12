function popup(mylink, windowname) {
    if (!window.focus) return true;
    var href;
    if (typeof (mylink) == 'string') href = mylink;
    else href = mylink.href;
    window.open(href, windowname, 'width=632,height=500,scrollbars=no');
    return false;
}