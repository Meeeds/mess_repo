// ==UserScript==
// @name         Send Message Script
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Send a message to game chat on online-go.com
// @author       You
// @match        https://online-go.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    // Wait until the page and chat input box is fully loaded

    // Global variable to store the last URL where the function was called
    let lastURL = '';
    let messageToSend = "Hello have fun";
    let myPlayerID = "680893";

    function checkAndSendMessage() {
        // If the function was already called on this URL, do nothing
        if (lastURL === window.location.href) {
            console.log("Url already checked: " + lastURL);
            return;
        }
        // Update the last URL
        lastURL = window.location.href;

        let messageAlreadySent = false;
        let checkCount = 0;
        let checkMessages = setInterval(function() {

            //check I am one of the players
            let blackPlayer = document.querySelector("#default-variant-container > div:nth-child(3) > div > div.right-col > div.players > div > div > div.white.player-name-container > span > a")
            let whitePlayer = document.querySelector("#default-variant-container > div:nth-child(3) > div > div.right-col > div.players > div > div > div.black.player-name-container > span > a")
            if( blackPlayer !== null && whitePlayer !== null){
                //console.log("players OK ["+ blackPlayer +"] ["+ whitePlayer+"]");
                if(blackPlayer.getAttribute('data-player-id')!==myPlayerID && whitePlayer.getAttribute('data-player-id')!==myPlayerID){
                    console.log("Not my game("+ window.location.href +") return now ["+ blackPlayer.getAttribute('data-player-id') +"] ["+ whitePlayer.getAttribute('data-player-id')+"]");
                    clearInterval(checkMessages); // stop checking
                    return;
                }
            }else{
                //console.log("one player is null["+ blackPlayer +"] ["+ whitePlayer+"]");
                clearInterval(checkMessages); // stop checking
                return;
            }

            let messages = document.querySelectorAll("#default-variant-container > div:nth-child(3) > div > div.right-col > div.GameChat > div.log-player-container > div > div > div > div.chat-line.main.chat-user-"+myPlayerID+" > span.body > span");
            console.log("checkMessages:" + checkCount + " messages:" + messages.length);
            if (messages.length > 0 || checkCount > 2) { // checking every 1000ms for 5sec
                clearInterval(checkMessages); // stop checking
                messages.forEach((message) => {
                    console.log("My messages : " +message.innerText);
                    if (message.innerText === messageToSend) {
                        messageAlreadySent = true;
                    }
                });
                let chatInputBox = document.querySelector("#default-variant-container > div:nth-child(3) > div > div.right-col > div.GameChat > div.chat-input-container.input-group > input");
                if ( messageAlreadySent ) {
                    console.log("message already sent:" + window.location.href);
                } else if (chatInputBox !== null) {
                    chatInputBox.focus(); // Focus on the input box
                    chatInputBox.value = messageToSend;
					// Create a new 'change' event
					var event = new Event('change');
					// Dispatch it.
					chatInputBox.dispatchEvent(event);
					// Send the message by simulating Enter key press

					chatInputBox.dispatchEvent(new KeyboardEvent('keypress', { bubbles: true, cancelable: true, keyCode: 13}));
                    console.log("Sending message to " + window.location.href);
                }else{
                    console.log("Weird issue " + chatInputBox + " messageAlreadySent:" + messageAlreadySent);
                }
            }else{
                console.log("If is false, wait 1sec len:" + messages.length + " checkCount:" + checkCount);
            }

            checkCount++;
        }, 1000);
    }


    // Create a function to observe a specific element
    function observeChat(chatElement) {
        // Create a mutation observer to watch for changes in the chat div
        let observer = new MutationObserver(function(mutations) {
            // If the URL contains '/game/', call the function to check and send the message
            if (window.location.href.includes('/game/')) {
                setTimeout( checkAndSendMessage(), 500); // Execute something() 500ms after
            }
        });

        // Start observing the chat for changes
        observer.observe(chatElement, { childList: true, subtree: true });
    }

    // Create an interval to check every 500ms if the chat div exists
    let checkChatExists = setInterval(function() {
        let chatElement = document.querySelector("div.GameChat");
        if(chatElement !== null) {
            // If the chat div exists, stop checking and start observing
            clearInterval(checkChatExists);
            checkAndSendMessage();
            observeChat(chatElement);
        }
    }, 500);

})();
