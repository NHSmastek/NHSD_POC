$(document).ready(function () {
    var $parentContainerForSelector = $("#typeSelector");

    var hideUnselectedPanels = function () {
        var tumorType = $(":radio:checked", $parentContainerForSelector).attr("data-type-selector");
        $("div[data-type-selector]").hide();
        $("div[data-type-selector=" + tumorType + "]").show();
    }
    $(":radio", $parentContainerForSelector).on("change", hideUnselectedPanels);

    // We need to fire this off now in order to hide the un-selected panels by default
    hideUnselectedPanels();

    $(function () {
        $("#downloadButton").on("click",
            function () {
                var dateFirstSeenChecked = $("#DateFirstSeen:checked").length > 0;
                var cancerTreatmentPeriodStartDateChecked = $("#CancerTreatmentPeriodStartDate:checked").length > 0;
                var treatmentStartDateCancerTreatmentProviderSearchChecked = $("#TreatmentStartDateCancerTreatmentProviderSearch:checked").length > 0;
                var treatmentSharedCareSearchChecked = $("#TreatmentStartDateCancerTreatmentSharedCareSearch:checked").length > 0;

                if (dateFirstSeenChecked ||
                    cancerTreatmentPeriodStartDateChecked ||
                    treatmentStartDateCancerTreatmentProviderSearchChecked ||
                    treatmentSharedCareSearchChecked)
                    return true;
                else {
                    alert("Please select at least one event type to filter by");
                    return false;
                }
            });

        $("#resetForm").on("click",
            function () {
                $("input[name='ReportingCategory.ReportingDiagnosisCategory']").attr('checked', false);
                $("input[value='Undefined']").prop('checked', true);
                $("#DateFirstSeen").prop('checked', true);
                $("#CancerTreatmentPeriodStartDate").prop('checked', false);
                $("#TreatmentStartDateCancerTreatmentProviderSearch").prop('checked', false);
                $("#TreatmentStartDateCancerTreatmentSharedCareSearch").prop('checked', false);
                $("div[data-type-selector]").hide();
            });
    });
});