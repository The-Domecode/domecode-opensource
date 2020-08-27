"use strict";

$(document).ready(function () {
  function updateText(btn, newCount, verb) {
    btn.text(newCount + " " + verb);
    btn.attr("data-likes", newCount);
  }

  $("#like").click(function (e) {
    e.preventDefault();
    var this_ = $(this);
    var likeUrl = this_.attr("data-href");
    var likeCount = parseInt(this_.attr("data-likes")) | 0;
    var addLike = likeCount + 1;
    var removeLike = likeCount - 1;

    if (likeUrl) {
      $.ajax({
        url: likeUrl,
        method: "GET",
        data: {},
        success: function success(data) {
          console.log(data);

          if (data.liked) {
            updateText(this_, addLike, "Likes");
          } else {
            updateText(this_, removeLike, "Likes");
          }
        },
        error: function error(_error) {
          console.log(_error);
          console.log("error");
        }
      });
    }
  });
});
$(document).ready(function () {
  function updateText(btn, newCount, verb) {
    btn.text(newCount + " " + verb);
    btn.attr("data-likes", newCount);
  }

  $("#like1").click(function (e) {
    e.preventDefault();
    var this_ = $(this);
    var likeUrl = this_.attr("data-href");
    var likeCount = parseInt(this_.attr("data-likes")) | 0;
    var addLike = likeCount + 1;
    var removeLike = likeCount - 1;

    if (likeUrl) {
      $.ajax({
        url: likeUrl,
        method: "GET",
        data: {},
        success: function success(data) {
          console.log(data);

          if (data.liked) {
            updateText(this_, addLike, "Likes");
          } else {
            updateText(this_, removeLike, "Likes");
          }
        },
        error: function error(_error2) {
          console.log(_error2);
          console.log("error");
        }
      });
    }
  });
});
var element = document.getElementById('back-link'); // Provide a standard href to facilitate standard browser features such as
//  - Hover to see link
//  - Right click and copy link
//  - Right click and open in new tab

element.setAttribute('href', document.referrer); // We can't let the browser use the above href for navigation. If it does,
// the browser will think that it is a regular link, and place the current
// page on the browser history, so that if the user clicks "back" again,
// it'll actually return to this page. We need to perform a native back to
// integrate properly into the browser's history behavior

element.onclick = function () {
  history.back();
  return false;
};

function showPreview() {
  var htmlCode = document.getElementById("htmlCode").value;
  var cssCode = "<style>" + document.getElementById("cssCode").value + "</style>";
  var jsCode = "<scri" + "pt>" + document.getElementById("jsCode").value + "</scri" + "pt>";
  var frame = document.getElementById("preview-window").contentWindow.document;
  frame.open();
  frame.write(htmlCode + cssCode + jsCode);
  frame.close();
}

function ytpreview() {
  var ytcode = document.getElementById("ytcode").value;
  var ytframe = document.getElementById("ytvideo").contentWindow.document;
  ytframe.open();
  ytframe.write(ytcode);
  ytframe.close();
}

var CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/';
