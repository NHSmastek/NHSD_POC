var $periodSelectors = $("#periodSelector");
var $laterPeriodSelector = $("#periodSelector .later-period");
var $earlierPeriodSelector = $("#periodSelector .earlier-period");
var statisticsPeriods = [];


$(document).ready(function () {

    if (!$periodSelectors.length)
        return;

    if (!$laterPeriodSelector.length)
        return;

    if (!$earlierPeriodSelector.length)
        return;

    statisticsPeriods = window.cwtPeriodPicker.statisticsPeriods;

    configurePeriodSelectors();
});

var configurePeriodSelectors = function () {

    if (statisticsPeriods.length > 0) {
        populateSubmissionStatisticsPeriodSelector($laterPeriodSelector, statisticsPeriods[0].PeriodDate);

        populateSubmissionStatisticsPeriodSelector($earlierPeriodSelector,
                            statisticsPeriods.length > 1 ? statisticsPeriods[1].PeriodDate : statisticsPeriods[0].PeriodDate);
    }
}

var populateSubmissionStatisticsPeriodSelector = function ($periodSelector, defaultValue) {

    for (var i = 0; i < statisticsPeriods.length; i++) {

        var period = statisticsPeriods[i];
        $periodSelector.append(createOption(period.DisplayText, period.PeriodDate));
    }

    $periodSelector.val(defaultValue);
};

createOption = function (label, value) {
    var option = $("<option />").val(value).text(label);
    return option;
}

