(function ($) {

    $(document).ready(function () {

        addDataFileUploadHandlers();
        addDownloadHandler();

        $('[data-toggle="tooltip"]').tooltip();

        addTestDataClickHandler();

        $("body").on("change", "#CollectionId, #OrganisationId", function () {
            $("#ReportingPeriodId").val(null);
        });

        $("body").on("change", "#CollectionId, #OrganisationId, #ReportingPeriodId", function () {
            $.ajax({
                    url: urlBase + "Submission/Submit",
                    data: $("#submit-submission").serialize(),
                    beforeSend: function () {
                        $(overlay).appendTo("body");
                    }
                })
                .done(function (result) {
                    $("#submit-submission").empty().append($(result).find("#submit-submission").html());
                    $("#download-proforma").empty().append($(result).find("#download-proforma").html());
                    $("#legend-replaceable").empty().append($(result).find("#legend-replaceable").html());
                    addTestDataClickHandler();
                })
                .always(function () {
                    addDataFileUploadHandlers();
                    $("#overlay").remove();
                    if ($("#ReportingPeriodId").val() === "" && $("#ReportingPeriodId").attr("disabled") === undefined) {
                        $("#DownloadButton").attr("disabled", "disabled");
                    }
                });
        });
    });

    function addTestDataClickHandler() {
        $("#IsTest").click(function () {

            if ($("#IsTest").prop("checked") === true) {
                $("#TestDataWarning").fadeIn();
            } else {
                $("#TestDataWarning").fadeOut();
            }
        });
    }

    function addDataFileUploadHandlers() {
        $("#DataFile").change(function () {
            $("#js-text").val($(this).val().replace(/C:\\fakepath\\/i, ""));
        });
    }

    function addDownloadHandler() {

        $("#download-proforma").on("submit", function (e) {
            e.preventDefault();

            var proformaIdHiddenField = 'input:hidden[name="ProformaId"]';

            // Get the ProformaId in Submission form into the Download form.
            var $submissionForm = $(this).siblings("#submit-submission");
            var proformaIdInSubmissionForm = $submissionForm.find(proformaIdHiddenField);

            var $downloadForm = $("#download-proforma");
            var proformaIdInDownloadForm = $downloadForm.find(proformaIdHiddenField);

            proformaIdInDownloadForm.val(proformaIdInSubmissionForm.val());

            $downloadForm.unbind().submit();
        });

    }

    //function setDataStandardValue() {

    //    var $dataStandardId = $("#DataStandardId");
    //    var options = $dataStandardId.children("option");

    //    if (options.length > 2) {
    //        $("#DataStandardId").val(0).change();
    //        return $dataStandardId.attr("disabled", false);
    //    }

    //    $("#DataStandardId").val(1).change();
    //    return $dataStandardId.attr("disabled", true);

    //}
    
    $(document).ready(function () {
        $('.break-glass-view-link.show-modal').click(function (event) {

            var link = $(event.currentTarget);
            var confirmUrl = link.attr('data-confirm-url');
            $('#confirm-break-glass-true').attr('href', confirmUrl);
            $('#confirm-break-glass').modal('show');

            event.preventDefault ? event.preventDefault() : event.returnValue = false;
        });
    });


})(jQuery);
