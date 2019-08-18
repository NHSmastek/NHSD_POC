$(document).ready(function () {
    var $container;
    var toggleSelectAllButtonText = function (setToSelectAll) {
        var $this = $("#selectAllContainer");

        if (setToSelectAll) {
            $this.text("Select All");
        }
        else {
            $this.text("Deselect All");
        }
    }

    $(document).on('click', ':checkbox', function () {
        var isAllSelected = areAnyCheckboxesUnchecked();
        toggleSelectAllButtonText(isAllSelected);
    });
    $(document).on('click', '.report-tab', function () {
        var isAllSelected = areAnyCheckboxesUnchecked();
        toggleSelectAllButtonText(isAllSelected);
    });
    $(document).on('click', '.report-type-selector', function () {
        var isAllSelected = areAnyCheckboxesUnchecked();
        toggleSelectAllButtonText(isAllSelected);
    });

    var areAnyCheckboxesUnchecked = function () {
        $container = $("#" + $("#selectAllContainer").attr("data-select-all-toggle-target"));
        var $allCheckboxes = $(":enabled:checkbox", $container);
        var $checkboxesChecked = $(":checkbox:checked", $container);
        var areAnyUnselected = $allCheckboxes.length != $checkboxesChecked.length;

        return areAnyUnselected;
    }

    $(document).on('click', '#selectAllContainer',
        function () {
            $container = $("#" + $(this).attr("data-select-all-toggle-target"));

            var $checkboxes = $(":enabled:checkbox", $container);
            var areAnyUnchecked = areAnyCheckboxesUnchecked($container);

            if (areAnyUnchecked) {
                $checkboxes.prop("checked", true);
                toggleSelectAllButtonText(false);
            }
            else {
                $checkboxes.prop("checked", false);
                toggleSelectAllButtonText(true);
            }
        });
});