$(document).ready(function () {
    function updateText(btn, newCount, verb) {
        btn.text(newCount + " " + verb)
        btn.attr("data-likes", newCount)
    }
    $("#like").click(function (e) {
        e.preventDefault()
        var this_ = $(this)
        var likeUrl = this_.attr("data-href")
        var likeCount = parseInt(this_.attr("data-likes")) | 0
        var addLike = likeCount + 1
        var removeLike = likeCount - 1
        if (likeUrl) {
            $.ajax({
                url: likeUrl,
                method: "GET",
                data: {},
                success: function (data) {
                    console.log(data)
                    if (data.liked) {
                        updateText(this_, addLike, "Likes")
                    } else {
                        updateText(this_, removeLike, "Likes")
                    }

                }, error: function (error) {
                    console.log(error)
                    console.log("error")
                }
            })
        }

    })
})
$(document).ready(function () {
    function updateText(btn, newCount, verb) {
        btn.text(newCount + " " + verb)
        btn.attr("data-likes", newCount)
    }
    $("#like1").click(function (e) {
        e.preventDefault()
        var this_ = $(this)
        var likeUrl = this_.attr("data-href")
        var likeCount = parseInt(this_.attr("data-likes")) | 0
        var addLike = likeCount + 1
        var removeLike = likeCount - 1
        if (likeUrl) {
            $.ajax({
                url: likeUrl,
                method: "GET",
                data: {},
                success: function (data) {
                    console.log(data)
                    if (data.liked) {
                        updateText(this_, addLike, "Likes")
                    } else {
                        updateText(this_, removeLike, "Likes")
                    }

                }, error: function (error) {
                    console.log(error)
                    console.log("error")
                }
            })
        }

    })
})


var element = document.getElementById('back-link');

// Provide a standard href to facilitate standard browser features such as
//  - Hover to see link
//  - Right click and copy link
//  - Right click and open in new tab
element.setAttribute('href', document.referrer);

// We can't let the browser use the above href for navigation. If it does,
// the browser will think that it is a regular link, and place the current
// page on the browser history, so that if the user clicks "back" again,
// it'll actually return to this page. We need to perform a native back to
// integrate properly into the browser's history behavior
element.onclick = function () {
    history.back();
    return false;
}





var CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/';
