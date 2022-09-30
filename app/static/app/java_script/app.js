$(document).ready(function () {
    $('button.but').click(function () {
        var audioElement = document.createElement("audio");
        var number = $(this).data('value');
        var idvalue = $(this).attr('id');
            if (idvalue == "one") {
                audioElement.src = "https://github.com/Vladimir-82/speach/blob/master/sounds_blr/one.wav?raw=true";
                } else if (idvalue == "two") {
                audioElement.src = "https://github.com/Vladimir-82/speach/blob/master/sounds_blr/two.wav?raw=true";
                } else if (idvalue == "three") {
                audioElement.src = "https://github.com/Vladimir-82/speach/blob/master/sounds_blr/three.wav?raw=true";
                } else if (idvalue == "four") {
                audioElement.src = "https://github.com/Vladimir-82/speach/blob/master/sounds_blr/four.wav?raw=true";
                } else if (idvalue == "five") {
                audioElement.src = "https://github.com/Vladimir-82/speach/blob/master/sounds_blr/five.wav?raw=true";
                } else if (idvalue == "six") {
                audioElement.src = "https://github.com/Vladimir-82/speach/blob/master/sounds_blr/six.wav?raw=true";
                } else if (idvalue == "seven") {
                audioElement.src = "https://github.com/Vladimir-82/speach/blob/master/sounds_blr/seven.wav?raw=true";
                } else if (idvalue == "eight") {
                audioElement.src = "https://github.com/Vladimir-82/speach/blob/master/sounds_blr/eight.wav?raw=true";
                } else if (idvalue == "nine") {
                audioElement.src = "https://github.com/Vladimir-82/speach/blob/master/sounds_blr/nine.wav?raw=true";
                } else if (idvalue == "zero") {
                audioElement.src = "https://github.com/Vladimir-82/speach/blob/master/sounds_blr/zero.wav?raw=true";
                } else if (idvalue == "minus") {
                audioElement.src = "https://github.com/Vladimir-82/speach/blob/master/sounds_blr/minus.wav?raw=true";
                } else if (idvalue == "plus") {
                audioElement.src = "https://github.com/Vladimir-82/speach/blob/master/sounds_blr/plus.wav?raw=true";
                } else if (idvalue == "multiply") {
                audioElement.src = "https://github.com/Vladimir-82/speach/blob/master/sounds_blr/multiply.wav?raw=true";
                } else if (idvalue == "divide") {
                audioElement.src = "https://github.com/Vladimir-82/speach/blob/master/sounds_blr/divide.wav?raw=true";
                }
        $('#meaning').val(function() {
        audioElement.play();
        return this.value + number;
    });
});
});



