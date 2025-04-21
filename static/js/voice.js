// // function startVoice() {
// //     const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
// //     recognition.lang = 'en-US';
// //     recognition.start();
  
// //     recognition.onresult = function(event) {
// //       const result = event.results[0][0].transcript;
// //       document.getElementById("user-input").value = result;
// //       sendMessage();
// //     };
// //   }
  
// //   function speak(text) {
// //     const synth = window.speechSynthesis;
// //     const utter = new SpeechSynthesisUtterance(text);
// //     synth.speak(utter);
// //   }
  
// function sendMessage() {
//     const input = document.getElementById("user-input");
//     const message = input.value.trim();
//     if (!message) return;
  
//     addMessage(message, "user");
//     input.value = "";
  
//     fetch("/chat", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({ message }),
//     })
//       .then((res) => res.json())
//       .then((data) => {
//         if (data.response) {
//           addMessage(data.response, "bot");
//           speakResponse(data.response);
//         }
//       });
//   }
  
//   function addMessage(text, sender) {
//     const chatBox = document.getElementById("chat-box");
//     const messageRow = document.createElement("div");
//     messageRow.classList.add("message-row", sender);
  
//     const avatar = document.createElement("img");
//     avatar.src =
//       sender === "user"
//         ? "https://cdn-icons-png.flaticon.com/512/1144/1144760.png"
//         : "https://cdn-icons-png.flaticon.com/512/4712/4712027.png";
//     avatar.classList.add("avatar");
  
//     const messageBubble = document.createElement("div");
//     messageBubble.classList.add("message", sender);
//     messageBubble.innerHTML = text;
  
//     if (sender === "user") {
//       messageRow.appendChild(messageBubble);
//       messageRow.appendChild(avatar);
//     } else {
//       messageRow.appendChild(avatar);
//       messageRow.appendChild(messageBubble);
//     }
  
//     chatBox.prepend(messageRow);
//   }
  
//   function startVoiceTyping() {
//     const recognition = new webkitSpeechRecognition() || new SpeechRecognition();
//     recognition.lang = 'en-US';
//     recognition.interimResults = false;
//     recognition.maxAlternatives = 1;
  
//     recognition.onresult = function (event) {
//       document.getElementById("user-input").value = event.results[0][0].transcript;
//       sendMessage();
//     };
//     recognition.start();
//   }
  
//   function speakResponse(text) {
//     const utterance = new SpeechSynthesisUtterance(text);
//     window.speechSynthesis.speak(utterance);
//   }
  
//   document.getElementById("user-input").addEventListener("keypress", function (e) {
//     if (e.key === "Enter") sendMessage();
//   });

let isVoiceInput = false;

function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  addMessage(message, "user");
  input.value = "";

  fetch("/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.response) {
        addMessage(data.response, "bot");
        if (isVoiceInput) {
          speakResponse(data.response);
          isVoiceInput = false; // reset after speaking
        }
      }
    });
}

function addMessage(text, sender) {
  const chatBox = document.getElementById("chat-box");
  const messageRow = document.createElement("div");
  messageRow.classList.add("message-row", sender);

  const avatar = document.createElement("img");
  avatar.src =
    sender === "user"
      ? "https://cdn-icons-png.flaticon.com/512/1144/1144760.png"
      : "https://cdn-icons-png.flaticon.com/512/4712/4712027.png";
  avatar.classList.add("avatar");

  const messageBubble = document.createElement("div");
  messageBubble.classList.add("message", sender);
  messageBubble.innerHTML = text;

  if (sender === "user") {
    messageRow.appendChild(messageBubble);
    messageRow.appendChild(avatar);
  } else {
    messageRow.appendChild(avatar);
    messageRow.appendChild(messageBubble);
  }

  chatBox.prepend(messageRow);
}

function startVoiceTyping() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-US";
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  recognition.onresult = function (event) {
    document.getElementById("user-input").value = event.results[0][0].transcript;
    isVoiceInput = true;
    sendMessage();
  };

  recognition.onerror = function (event) {
    alert("Voice recognition error: " + event.error);
  };

  recognition.start();
}

function speakResponse(text) {
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "en-US";
  speechSynthesis.speak(utterance);
}

document.getElementById("user-input").addEventListener("keypress", function (e) {
  if (e.key === "Enter") sendMessage();
});
