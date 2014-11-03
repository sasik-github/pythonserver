$(document).ready(function(){
    $('[id^=id_borndate]').on('change', function(){
        getAge();
    });
    $('#id_age').on('change', function(){
        getBorndate();
    });
});

function getAge(){
    var year = $('#id_borndate_year').val();
    var month = $('#id_borndate_month').val();
    var day = $('#id_borndate_day').val();
    var dateObj = new Date(year, month - 1, day);
    var today = new Date();
    var userAge = today.getFullYear() - dateObj.getFullYear();
    $('#id_age').val(userAge);
}

function getBorndate() {
    var userAge = $('#id_age').val();
    var today = new Date();
    var year = today.getFullYear() - userAge;
    $('#id_borndate_year').val(year);
}