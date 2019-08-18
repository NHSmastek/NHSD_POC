var overlay = '<div id="overlay"><div id="imgholder"><div id="loading"></div></div></div>';

(function ($) {

    $(document).ready(function () {

        $('.input-group.date').datepicker({
            format: "dd/mm/yyyy",
            autoclose: true,
            todayBtn: "linked"
        });

        // Replace the builtin US date validation with UK date validation
        $.validator.addMethod(
            "date",
            function (value, element) {
                var bits = value.match(/([0-9]+)/gi), str;
                if (!bits)
                    return this.optional(element) || false;
                str = bits[1] + '/' + bits[0] + '/' + bits[2];
                return this.optional(element) || !/Invalid|NaN/.test(new Date(str));
            },
            "Please enter a date in the format dd/mm/yyyy"
        );

        /*********************** Set up chosen dropdowns *************************/
        $(".chosen").chosen();

    });

})(jQuery);
