/*This script is for implementing the mobile fix for resources. See 
https://github.com/The-Domecode/domecode-opensource/issues/3#issuecomment-685106802
for more info. */


// polyfill "String.includes" function. 
// Required for bowsers without ES6 support, like Internet Explorer.
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

// Polyfill HTMLCollection.forEach from Array.forEach
if (!HTMLCollection.prototype.forEach) HTMLCollection.prototype.forEach = Array.prototype.forEach;


// List of elements to work on. To add new types of elements, just add mroe tag names to this array.
const elements = ["IFRAME", "IMG"];
let frames = [];

// Grab all the elements
elements.forEach((element) => {
    frames = frames.concat(Array.from(document.getElementsByTagName(element)));
});

// Apply our modifications
frames.forEach((frame) => {
    // Get the frame's parent
    let parent = frame.parentNode;
    // Create the wrapper div and set its class
    let wrapper = document.createElement("div");
    wrapper.className = "video-container";

    // Wrap the frame in the wrapper
    parent.replaceChild(wrapper, frame);
    wrapper.appendChild(frame);
})