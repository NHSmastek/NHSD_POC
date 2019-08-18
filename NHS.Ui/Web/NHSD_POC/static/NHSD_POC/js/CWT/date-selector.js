var $parentContainerForSelector = $("#dateSelector");

var reportingPeriods = [];
var allowIncompleteQuarters = false;

var datePicker = {
    common: {},
    dateRange: {},
    yearOnly: {},
    quarter: {},
    monthOnly: {}
}

datePicker.common.createOption = function (label, value) {
    var option = $("<option />").val(value).text(label);
    return option;
}

datePicker.common.doesValueExistInDropdown = function ($dropdownList, value) {
    return $($dropdownList).find("option:contains('" + value + "')").length;
}

datePicker.common.getLongMonthName = function (monthInt) {
    var monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];

    return monthNames[monthInt - 1];
}

datePicker.dateRange.populateFromYearsOnDateRangeSelector = function () {
    var $fromYear = $("#dateRangeSelector .from-year");
    datePicker.common.populateYears($fromYear, 0);
}

datePicker.dateRange.populateToYearsOnDateRangeSelector = function () {
    var $fromYear = $("#dateRangeSelector .from-year");
    var $toYear = $("#dateRangeSelector .to-year");
    datePicker.common.populateYears($toYear, $fromYear.val());
}

datePicker.monthOnly.populateYearsOnMonthOnlySelector = function () {
    var $year = $("#monthOnlySelector .year");
    datePicker.common.populateYears($year, 0);
}

datePicker.common.populateYears = function ($year, earliestYearToPopulate, maximumYearToPopulate) {
    var value = $year.val();
    $year.find('option').remove();

    maximumYearToPopulate = maximumYearToPopulate || 9999;

    for (var i = 0; i < reportingPeriods.length; i++) {
        var period = reportingPeriods[i];
        if (!datePicker.common.doesValueExistInDropdown($year, period.Year) && period.Year >= earliestYearToPopulate && period.Year <= maximumYearToPopulate)
            $year.append(datePicker.common.createOption(period.Year, period.Year));
    }

    if (!$year.val()) {
        $year.val(value);
    }
}

datePicker.quarter.populateQuarters = function ($existingValue) {
    var $year = $("#yearQuarterSelector .year");
    var $quarters = $("#yearQuarterSelector .first-month-in-quarter");
    $quarters.find('option').remove();

    var allQuarters = datePicker.quarter.getAllQuarters();

    for (var i = 0; i < allQuarters.length; i++) {
        var quarter = allQuarters[i];

        if ($year.val() == quarter.year) {
            $quarters.prepend(datePicker.common.createOption(quarter.quarterLabel, quarter.firstMontInQuarter));
        }
    }

    if ($existingValue)
        $quarters.val($existingValue);

    $quarters.val($existingValue);

    if (!$quarters.val()) {
        $quarters[0].selectedIndex = $("option", $quarters[0]).length - 1;
    }
}

datePicker.quarter.getAllQuarters = function () {
    var quarters = [];

    for (var i = 0; i < reportingPeriods.length; i++) {
        var period = reportingPeriods[i];

        if (period.Month % 3 == 1) {
            var quarterName = "";
            var doesAllMonthsExistInReportingPeriods = true;

            for (var q = 0; q < 3; q++) {
                var month = reportingPeriods[i - q];
                if (month == null || month.Year != period.Year || (month.Month != (period.Month + q)))
                    doesAllMonthsExistInReportingPeriods = false;

                if (q > 0)
                    quarterName += "/";
                quarterName += datePicker.common.getLongMonthName(period.Month + q);
            }

            if (allowIncompleteQuarters || doesAllMonthsExistInReportingPeriods)
                quarters.push({
                    quarterLabel: quarterName,
                    year: period.Year,
                    firstMontInQuarter: period.Month
                });
        }
    }

    return quarters;
}

datePicker.quarter.yearQuarterYearChanged = function () {
    var $year = $("#yearQuarterSelector .year");
    var $quarters = $("#yearQuarterSelector .first-month-in-quarter");
    datePicker.quarter.populateQuarters($quarters.val());
}

datePicker.dateRange.fromYearChangedOnDateRangeSelector = function () {
    var $fromYear = $("#dateRangeSelector .from-year");
    var $toYear = $("#dateRangeSelector .to-year");

    var $fromMonth = $("#dateRangeSelector .from-month");
    var $toMonth = $("#dateRangeSelector .to-month");

    datePicker.dateRange.updateDateRange($fromYear, $fromMonth, 0);

    if ($fromYear.val() > $toYear.val()) {
        $toYear.val($fromYear.val());
    }
    datePicker.dateRange.populateToYearsOnDateRangeSelector();

    datePicker.dateRange.updateDateRange($toYear, $toMonth, $fromMonth.val());
}

datePicker.dateRange.fromMonthChanged = function () {
    var $fromYear = $("#dateRangeSelector .from-year");
    var $toYear = $("#dateRangeSelector .to-year");

    var $fromMonth = $("#dateRangeSelector .from-month");
    var $toMonth = $("#dateRangeSelector .to-month");

    if ($fromYear.val() == $toYear.val()) {
        datePicker.dateRange.updateDateRange($toYear, $toMonth, $fromMonth.val(), $fromMonth.val());
    }
}

datePicker.dateRange.toYearChanged = function () {
    var $toYear = $("#dateRangeSelector .to-year");

    var $fromMonth = $("#dateRangeSelector .from-month");
    var $toMonth = $("#dateRangeSelector .to-month");

    datePicker.dateRange.updateDateRange($toYear, $toMonth, $fromMonth.val(), $fromMonth.val());
}

datePicker.monthOnly.yearChanged = function () {
    var $year = $("#monthOnlySelector .year");

    var $month = $("#monthOnlySelector .month");

    datePicker.monthOnly.populateMonths($year, $month);
}

datePicker.monthOnly.populateMonths = function ($year, $month) {
    datePicker.dateRange.updateDateRange($year, $month, 0);
}

datePicker.dateRange.updateDateRange = function ($year, $month, earliestMonthToAdd, defaultValue) {

    var valueBeforeChange = $month.val();
    $month.find("option").remove();

    for (var i = 0; i < reportingPeriods.length; i++) {
        var period = reportingPeriods[i];

        if ($year.val() == period.Year) {
            if (period.Month >= earliestMonthToAdd && !datePicker.common.doesValueExistInDropdown($month, period.Month))
                $month.prepend(datePicker.common.createOption(datePicker.common.getLongMonthName(period.Month), period.Month));

            // If this is the earliest non-complete month then we want it to be the default.
            //  Because we now allow multiple open months on the datepicker but we want it to default to the open submission period, not the calendar month.
            else
                $month.find("option[value='" + period.Month + "']");
        }

    }

    $month.val(valueBeforeChange);
    if (!$month.val() && defaultValue) {
        $month.val(defaultValue);
    }
    else if (!$month.val() && !defaultValue) {
        var currentSubmissionMonth = getCurrentOpenSubmissionPeriodMonth($year.val());
        $month.val(currentSubmissionMonth);
    }
}

var getCurrentOpenSubmissionPeriodMonth = function (currentYear) {
    var currentMonthToDisplay = null;
    for (var i = 0; i < reportingPeriods.length; i++) {
        var period = reportingPeriods[i];

        // If this is an earlier month that is still uncompleted then we want this to be the default as this is the 'open' submission period.
        if (currentMonthToDisplay == null || (currentYear == period.Year && !period.IsComplete && currentMonthToDisplay > period.Month)) {
            currentMonthToDisplay = period.Month;
        }
    }

    return currentMonthToDisplay;
}

var hideUnselectedPanels = function () {
    var dateEntryMethod = $(":radio:checked", $parentContainerForSelector).attr("data-date-selector");
    $("div[data-date-selector]").hide();
    $("div[data-date-selector=" + dateEntryMethod + "]").show();
}

var configureDateRangeSelector = function () {
    if (!$("#dateRangeSelector").length)
        return;

    $(":input[id*='FromYear']", $("#dateRangeSelector")).on("change", datePicker.dateRange.fromYearChangedOnDateRangeSelector);
    $(":input[id*='FromMonth']", $("#dateRangeSelector")).on("change", datePicker.dateRange.fromMonthChanged);
    $(":input[id*='ToYear']", $("#dateRangeSelector")).on("change", datePicker.dateRange.toYearChanged);


    datePicker.dateRange.populateFromYearsOnDateRangeSelector();
    datePicker.dateRange.fromYearChangedOnDateRangeSelector();
}

var configureYearQuarterSelector = function () {
    if (!$("#yearQuarterSelector").length)
        return;

    $(":input[id*='Year']", $("#yearQuarterSelector")).on("change", datePicker.quarter.yearQuarterYearChanged);

    var maximumYearForQuarters = _.max(datePicker.quarter.getAllQuarters(), function (quarter) { return quarter.year; }).year;
    datePicker.common.populateYears($("#yearQuarterSelector .year"), 0, maximumYearForQuarters);
    datePicker.quarter.populateQuarters();
}

var configureMonthOnlySelector = function () {
    if (!$("#monthOnlySelector").length)
        return;

    $(":input[id*='Year']", $("#monthOnlySelector")).on("change", datePicker.monthOnly.yearChanged);
    datePicker.common.populateYears($("#monthOnlySelector .year"), 0, 9999);
    datePicker.monthOnly.yearChanged();
}

var configureYearOnlySelector = function () {
    if (!$("#yearOnlySelector").length)
        return;

    datePicker.common.populateYears($(":input[id*='Year']", $("#yearOnlySelector")), 0);
}

$(document).ready(function () {

    if (!$parentContainerForSelector.length)
        return;

    reportingPeriods = window.cwtDatePicker.reportingPeriods;
    allowIncompleteQuarters = window.cwtDatePicker.allowIncompleteQuarters || false;

    $(":radio", $parentContainerForSelector).on("change", hideUnselectedPanels);
    // We need to fire this off now in order to hide the un-selected panels by default
    hideUnselectedPanels();

    configureDateRangeSelector();
    configureYearQuarterSelector();
    configureYearOnlySelector();
    configureMonthOnlySelector();
});