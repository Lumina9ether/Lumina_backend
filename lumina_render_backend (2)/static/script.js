const micButton = document.getElementById("mic-button");
const subtitles = document.getElementById("subtitles");
const orb = document.getElementById("orb");

let recognizing = false;
let recognition;

function setupRecognition() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();
    recognition.interimResults = false;
    recognition.lang = "en-US";

    recognition.onstart = () => {
        recognizing = true;
        orb.className = "thinking";
    };

    recognition.onresult = (event) => {
        const text = event.results[0][0].transcript;
        subtitles.innerText = text;
        sendTextToBackend(text);
    };

    recognition.onend = () => {
        recognizing = false;
        orb.className = "idle";
    };
}

micButton.addEventListener("click", () => {
    if (!recognition) setupRecognition();
    if (recognizing) {
        recognition.stop();
    } else {
        recognition.start();
    }
});

function sendTextToBackend(text) {
    fetch("/process-text", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text: text})
    })
    .then(res => res.json())
    .then(data => {
        subtitles.innerText = data.reply;
        orb.className = "speaking";
        const synth = window.speechSynthesis;
        const utter = new SpeechSynthesisUtterance(data.reply);
        utter.onend = () => {
            orb.className = "idle";
        };
        synth.speak(utter);
    });
}
