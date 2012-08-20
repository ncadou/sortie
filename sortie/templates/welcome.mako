<%inherit file="base.mako" />

<%block name="title">
  ${_('Welcome!')}
</%block>

<%block name="content">
  <div class="hero-unit">
    <h1>${title()}</h1>

    <p>
      ${_('This is the event registration site for %s.') % h.schoolname()}
      ${_('Please enter your name to continue.')}
    </p>

    <form action="${path('user-welcome')}" method="post" class="form-search">
      <input type="text" id="name" name="name" autocomplete="off"
             class="input-large search-query" value="${name or ''}"
             placeholder="${_('Enter your name')}">
##             data-source="${path('user-autocomplete')}">
      <input type="submit" name="submit" value="${_('Continue')}"
             class="btn btn-primary btn-large">
    </form>
  </div>
</%block>
