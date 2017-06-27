(function($){
	$(function () {
		$('.button-collapse').sideNav();
    });
    $(function () {
        $('select').material_select();
    });
    $(function () {
        $('.datepicker').pickadate({
            selectMonths: true,
            selectYears: 50,
        });
    });
})(jQuery);
