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


// Gather all video frames
var frames = $("iframe").map(function() {
    if (this.src.includes("trinket")) {
        // This is a trinket frame, skip
        return;
    } else {
        // This is not a trinket frame, return this
        return this;
    }
});

// Loop over each frame we got
frames.each(function() {
    // Create our wrapper div and wrap the frame
    $("<div/>", {"class": "video-container"}).wrap($(this));

});