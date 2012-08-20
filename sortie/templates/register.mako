<%inherit file="base.mako" />
<%!
    from sortie.api import event as event_api
%>

<%block name="title">
  ${_('Registration')}
</%block>

<%block name="content">
  <h1>${title()}</h1>

  <div class="alert alert-error hidden server-error">
    <a class="close" data-dismiss="alert" href="#">×</a>
    ${_("Can't save data: there was a problem with the server.")}
  </div>

  <table cellspacing="0" class="registration">
    <tr>
      <th>&nbsp;</th>

      % for event in events:
        <th>
          <a href="#" id="date-${event.id}" class="btn btn-inverse btn-large"
            >${event.date}</a><br>
          <span class="event-popover" data-title="${event.name}"
                data-html-content="event-${event.id}">${event.name}</span>
          <div class="hidden" id="event-${event.id}">${event.description}</div>
        </th>
      % endfor

    </tr>

    % for person in family:
      <tr>
        <td>
          ${person.fullname}<br>
          <span class="role">
            % if person.student:
              ${_('Student')}
              (${person.student.class_.name})
            % else:
              ${_('Family')}
            % endif
          </span>
        </td>

        % for event in events:
          <td class="center ${'not-' if person not in event else ''}registered">
            % if event_api.has_access(event, person):
              <input type="checkbox" name="reg-${event.id}-${person.id}"
                     class="reg" ${'checked' if person in event else ''}>
              <i class="icon-time"></i>

              <div class="info">info</div>

              % if event.options:
                <div class="tools">
                  <a href="#opt-${event.id}-${person.id}" class="btn options"
                     ${'disabled' if person not in event else ''}
                     data-toggle="modal">${_('Options')}</a>
                </div>

                <div class="modal hide" id="opt-${event.id}-${person.id}">
                  <div class="modal-header">
                    <button type="button" class="close"
                            data-dismiss="modal">×</button>
                    <h3>${person.fullname} – ${event.name} (${event.date})</h3>
                  </div>
                  <div class="modal-body">
                    <p>One fine body…</p>
                  </div>
                  <div class="modal-footer">
                    <a href="#" class="btn" data-dismiss="modal"
                      >${_('Close')}</a>
                    <a href="#" class="btn btn-primary save-reg"
                      >${_("Save changes")}</a>
                  </div>
                </div>
              % endif
            % endif
          </td>
        % endfor

      </tr>
    % endfor

  </table>
</%block>
