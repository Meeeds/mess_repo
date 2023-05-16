// ==UserScript==
// @name         Send Message Script
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Send a message to game chat on online-go.com
// @author       You
// @match        https://online-go.com/game/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    // Wait until the page and chat input box is fully loaded

    // Global variable to store the last URL where the function was called
    let lastURL = '';
    let messageToSend = "Hello have fun";

    function checkAndSendMessage() {
        // If the function was already called on this URL, do nothing
        if (lastURL === window.location.href) {
            console.log("Url already checked: " + lastURL);
            return;
        }
        // Update the last URL
        lastURL = window.location.href;

        let chatInputBox = document.querySelector("#default-variant-container > div:nth-child(3) > div > div.right-col > div.GameChat > div.chat-input-container.input-group > input");

        let messageAlreadySent = false;
        let checkCount = 0;
        let checkMessages = setInterval(function() {
            let messages = document.querySelectorAll("#default-variant-container > div:nth-child(3) > div > div.right-col > div.GameChat > div.log-player-container > div > div > div > div.chat-line.main.chat-user-680893 > span.body > span");

            if (messages.length > 0 || checkCount > 4) { // checking every 1000ms for 5sec
                clearInterval(checkMessages); // stop checking
                messages.forEach((message) => {
                    console.log("My messages : " +message.innerText);
                    if (message.innerText === messageToSend) {
                        messageAlreadySent = true;
                    }
                });
                if ( messageAlreadySent ) {
                    console.log("message already sent:" + window.location.href);
                }
                if (!messageAlreadySent && chatInputBox !== null) {
                    chatInputBox.focus(); // Focus on the input box
                    chatInputBox.value = messageToSend;
					// Create a new 'change' event
					var event = new Event('change');
					// Dispatch it.
					chatInputBox.dispatchEvent(event);
					// Send the message by simulating Enter key press

					chatInputBox.dispatchEvent(new KeyboardEvent('keypress', { bubbles: true, cancelable: true, keyCode: 13}));
                    console.log("Sending message to " + window.location.href);
                }
            }else{
                console.log("If is false, wait 1sec len:" + messages.length + " checkCount:" + checkCount);
            }

            checkCount++;
        }, 1000);
    }
    // Create a mutation observer to watch for changes in the body of the page
    let observer = new MutationObserver(function(mutations) {
        // If the URL contains '/game/', call the function to check and send the message
        if (window.location.href.includes('/game/')) {
            setTimeout( checkAndSendMessage(), 500); // Execute something() 500ms after
        }
    });

    // Start observing the body for changes
    observer.observe(document.body, { childList: true, subtree: true });
})();
