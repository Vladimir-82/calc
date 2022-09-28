$(document).ready(function () {
    $('button.but').click(function () {
        var number = $(this).data('value');
        $('#meaning').val(function() {
        return this.value + number;
    });
});
});