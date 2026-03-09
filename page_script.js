const startButton = document.getElementById("start");
const stopButton = document.getElementById("stop");
const undoButton = document.getElementById("undo");
const output = document.getElementById("output");

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();

recognition.continuous = true;
recognition.lang = "en-US";
recognition.interimResults = false;

let sentences = [];
let isListening = false;

startButton.onclick = function () {

    isListening = true;
    recognition.start();
};

stopButton.onclick = function () {

    isListening = false;
    recognition.stop();
};

recognition.onresult = function (event) {

    let transcript = event.results[event.results.length - 1][0].transcript;
    sentences.push(transcript);
    output.innerHTML = sentences.join(". ") + ".";
};

undoButton.onclick = function () {
    sentences.pop();
    output.innerHTML = sentences.join(". ") + ".";

};

recognition.onend = function () {

    if (isListening) {
        recognition.start();
    }
};