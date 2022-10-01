$(document).ready(function () {
    $('button.but').click(function () {
        var audioElement = document.createElement("audio");
        var number = $(this).data('value');
        var idvalue = $(this).attr('id');
            if (idvalue == "one") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/one.mp3?raw=true";
                } else if (idvalue == "two") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/two.mp3?raw=true";
                } else if (idvalue == "three") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/three.mp3?raw=true";
                } else if (idvalue == "four") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/four.mp3?raw=true";
                } else if (idvalue == "five") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/five.mp3?raw=true";
                } else if (idvalue == "six") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/six.mp3?raw=true";
                } else if (idvalue == "seven") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/seven.mp3?raw=true";
                } else if (idvalue == "eight") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/eight.mp3?raw=true";
                } else if (idvalue == "nine") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/nine.mp3?raw=true";
                } else if (idvalue == "zero") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/zero.mp3?raw=true";
                } else if (idvalue == "minus") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/minus.mp3?raw=true";
                } else if (idvalue == "plus") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/plus.mp3?raw=true";
                } else if (idvalue == "multiply") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/multiply.mp3?raw=true";
                } else if (idvalue == "divide") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/divide.mp3?raw=true";
                } else if (idvalue == "dot") {
                audioElement.src = "https://github.com/Vladimir-82/" +
                    "speach/blob/master/sounds/dot.mp3?raw=true";
                }
        $('#meaning').val(function() {
        audioElement.play();
        return this.value + number;
    });
});
});



