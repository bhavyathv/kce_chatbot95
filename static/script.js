const input = document.getElementById("messageInput");
const chatArea = document.getElementById("chatArea");
const sendButton = document.getElementById("sendButton");


function getTime() {

    const now = new Date();

    return now.toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });

}


/* =====================================================
   USER MESSAGE
===================================================== */

function addUserMessage(message) {

    const row = document.createElement("div");

    row.className = "message-row user-row";

    row.innerHTML = `

        <div class="user-bubble">

            ${escapeHTML(message)}

            <span class="user-time">
                ${getTime()}
            </span>

        </div>

    `;

    chatArea.appendChild(row);

    scrollToBottom();
}


/* =====================================================
   TYPING INDICATOR
===================================================== */

function showTyping() {

    const row = document.createElement("div");

    row.className = "message-row bot-row";

    row.id = "typingMessage";

    row.innerHTML = `

        <div class="avatar">
            K
        </div>

        <div class="bubble bot-bubble">

            <div class="bot-name">
                KCE Assistant
            </div>

            <div class="typing">

                <span></span>
                <span></span>
                <span></span>

            </div>

        </div>

    `;

    chatArea.appendChild(row);

    scrollToBottom();
}


/* =====================================================
   REMOVE TYPING
===================================================== */

function removeTyping() {

    const typing = document.getElementById("typingMessage");

    if (typing) {

        typing.remove();

    }

}


/* =====================================================
   BOT MESSAGE
===================================================== */

const input = document.getElementById("messageInput");
const chatArea = document.getElementById("chatArea");
const sendButton = document.getElementById("sendButton");


function getTime() {

    const now = new Date();

    return now.toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });

}


/* =====================================================
   USER MESSAGE
===================================================== */

function addUserMessage(message) {

    const row = document.createElement("div");

    row.className = "message-row user-row";

    row.innerHTML = `

        <div class="user-bubble">

            ${escapeHTML(message)}

            <span class="user-time">
                ${getTime()}
            </span>

        </div>

    `;

    chatArea.appendChild(row);

    scrollToBottom();
}


/* =====================================================
   TYPING INDICATOR
===================================================== */

function showTyping() {

    const row = document.createElement("div");

    row.className = "message-row bot-row";

    row.id = "typingMessage";

    row.innerHTML = `

        <div class="avatar">
            K
        </div>

        <div class="bubble bot-bubble">

            <div class="bot-name">
                KCE Assistant
            </div>

            <div class="typing">

                <span></span>
                <span></span>
                <span></span>

            </div>

        </div>

    `;

    chatArea.appendChild(row);

    scrollToBottom();
}


/* =====================================================
   REMOVE TYPING
===================================================== */

function removeTyping() {

    const typing = document.getElementById("typingMessage");

    if (typing) {

        typing.remove();

    }

}


/* =====================================================
   BOT MESSAGE
===================================================== */

function addBotMessage(message) {

    const row = document.createElement("div");

    row.className = "message-row bot-row";

    const safeMessage = escapeHTML(message);

    const formattedMessage = safeMessage
        .replace(/\n/g, "<br>")
        .replace(
            /(https?:\/\/[^\s<]+)/g,
            '<a href="$1" target="_blank" class="chat-link">$1</a>'
        );

    row.innerHTML = `

        <div class="avatar">
            K
        </div>

        <div class="bubble bot-bubble">

            <div class="bot-name">
                KCE Assistant
            </div>

            <div class="message-text">
                ${formattedMessage}
            </div>

            <div class="message-time">
                ${getTime()}
            </div>

        </div>

    `;

    chatArea.appendChild(row);

    scrollToBottom();
}


/* =====================================================
   SEND MESSAGE
===================================================== */

async function sendMessage() {

    const message = input.value.trim();

    if (!message) {

        return;

    }


    addUserMessage(message);

    input.value = "";

    sendButton.disabled = true;

    showTyping();


    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                message: message

            })

        });


        const data = await response.json();


        setTimeout(() => {

            removeTyping();

            addBotMessage(data.response);

            sendButton.disabled = false;

            input.focus();

        }, 700);


    }

    catch (error) {

        removeTyping();

        addBotMessage(
            "I'm having trouble connecting right now. Please try again. 🙂"
        );

        sendButton.disabled = false;

    }

}


/* =====================================================
   QUICK BUTTON
===================================================== */

function quickMessage(message) {

    input.value = message;

    sendMessage();

}


/* =====================================================
   ENTER KEY
===================================================== */

input.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {

        sendMessage();

    }

});


/* =====================================================
   SCROLL
===================================================== */

function scrollToBottom() {

    chatArea.scrollTo({

        top: chatArea.scrollHeight,

        behavior: "smooth"

    });

}


/* =====================================================
   SECURITY
===================================================== */

function escapeHTML(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;

}

/* =====================================================
   SEND MESSAGE
===================================================== */

async function sendMessage() {

    const message = input.value.trim();

    if (!message) {

        return;

    }


    addUserMessage(message);

    input.value = "";

    sendButton.disabled = true;

    showTyping();


    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                message: message

            })

        });


        const data = await response.json();


        setTimeout(() => {

            removeTyping();

            addBotMessage(data.response);

            sendButton.disabled = false;

            input.focus();

        }, 700);


    }

    catch (error) {

        removeTyping();

        addBotMessage(
            "I'm having trouble connecting right now. Please try again. 🙂"
        );

        sendButton.disabled = false;

    }

}


/* =====================================================
   QUICK BUTTON
===================================================== */

function quickMessage(message) {

    input.value = message;

    sendMessage();

}


/* =====================================================
   ENTER KEY
===================================================== */

input.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {

        sendMessage();

    }

});


/* =====================================================
   SCROLL
===================================================== */

function scrollToBottom() {

    chatArea.scrollTo({

        top: chatArea.scrollHeight,

        behavior: "smooth"

    });

}


/* =====================================================
   SECURITY
===================================================== */

function escapeHTML(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;

}