/*This script is for implementing the mobile fix for resources. See 
https://github.com/The-Domecode/domecode-opensource/issues/3#issuecomment-685106802
for more info. */


// polyfill "String.includes" function. required for bowsers without ES6 support, like Internet Explorer.
if (!String.prototype.includes) {
    String.prototype.includes = function(search, start) {
        'use strict';
        if (typeof start !== 'number') {
            start = 0;
        }
  
        if (start + search.length > this.length) {
            return false;
        } else {
            return this.indexOf(search, start) !== -1;
        }
    };
}

var all = document.getElementsByTagName("*");

var name;
var elements = [];

// loop through all elements on page to find all the iframes
for (var i=0, max=all.length; i < max; i++) {
    // get element name
    var el = all[i];
    var name = el.nodeName.toLowerCase();
    console.log(name);
    if (name == "iframe") {
        // if it's an iframe, push it to the list.
        elements.push(el);
    }
}

// loop through all the iframes we found
for (var i=0, max=elements.length; i < max; i++) {
    // get the frame to work on
    var frame = elements[i];
    // Skip trinket python editor
    if(frame.src.includes("trinket")) {
        continue;
    }
    console.log(frame.src);
    // Wrap the video inside the video-wrapper class
    
    // get the frame's current parent
    var parent = frame.parentNode;
    // create the wrapper div and set its class
    var wrapper = document.createElement("div");
    wrapper.className = "video-container"

    // set the wrapper as the parent's child instead of the frame
    parent.replaceChild(wrapper, frame);
    // set the frame as the child of the wrapper
    wrapper.appendChild(frame);
}