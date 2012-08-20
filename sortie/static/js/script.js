/* Author: Nicolas Cadou <ncadou@cadou.ca>

*/


$(document).ready(function() {
    // Welcome search name form.
    var name = $('.form-search input#name');

    if (name) {
        var source = name.data('source');

        if (source) {
            name.typeahead({'ajax': {
                'url': source,
                'method': 'get',
                'displayField': 'name'
            }});
        }
        name.focus();
    }

    // Registration form.
    $('table.registration .event-popover').each(function() {
        var contentId = $(this).data('html-content'),
            eventId = contentId.split('-')[1];

        $(this).add('#date-' + eventId).popover({
            content: $('#' + contentId).html(),
            placement: 'bottom',
            title: $(this).data('title')
        });
    });

    $('table.registration input:checkbox').click(function() {
        var checkbox = this,
            args = $(checkbox).attr('name').split('-');

        if (args && args[0] == 'reg') {
            var url = window.location,
                eventId = args[1],
                personId = args[2],
                isChecked = $(checkbox).prop('checked'),
                postData = {
                    event_id: eventId,
                    person_id: personId,
                    active: isChecked};

            $(checkbox).parent().addClass('loading');
            $.post(url, postData, function(replyData, textStatus, jqXHR) {
                $('.server-error').not('.hidden').remove();
                $(checkbox).parent().removeClass('loading');
                updateRegistrationUI(eventId, personId, replyData.registered);
            }).error(function(jqXHR, textStatus, errorThrown) {
                var msg = $('.server-error');
                if (msg.length == 1)
                    msg.after(msg.clone().removeClass('hidden'));
                updateRegistrationUI(eventId, personId, !isChecked);
            });
        }
    });

    $('table.registration .tools a').click(function() {
        if ($(this).attr('disabled'))
            return;
    });

    function updateRegistrationUI(eventId, personId, registered) {
        var checkbox = $('input[name=reg-' + eventId + '-' + personId + ']');
        if (registered) {
            checkbox.prop('checked', true)
                    .parent().removeClass('not-registered')
                             .addClass('registered')
                             .find('.tools a').prop('disabled', false)
                                              .removeAttr('disabled');
        } else {
            checkbox.prop('checked', false)
                    .parent().removeClass('registered')
                             .addClass('not-registered')
                             .find('.tools a').prop('disabled', true)
                                              .attr('disabled', 'disabled');
        }
    }
});
