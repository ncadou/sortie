<!doctype html>
<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js lt-ie9" lang="en"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

  <title>
    ${_('Sortie')}
    ${h.schoolname()}
    <%block name="title" />
  </title>

  <meta name="description" content="">
  <meta name="author" content="">

  <meta name="viewport" content="width=device-width">

  <link rel="stylesheet" href="${static_path('/css/bootstrap.min.css')}">
  <style>
  body {
    padding-top: 60px;
    padding-bottom: 40px;
  }
  </style>
  <link rel="stylesheet" href="${static_path('/css/bootstrap-responsive.min.css')}">
  <link rel="stylesheet" href="${static_path('/css/style.css')}">

  <script src="${static_path('/js/libs/modernizr-2.5.3-respond-1.1.0.min.js')}"></script>
</head>
<body>
<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->

    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="#">${_('Sortie')}</a>
          <a class="brand" href="#">${h.schoolname()}</a>
          <a class="brand" href="#">${self.title()}</a>
          ## <div class="nav-collapse">
            ## <ul class="nav">
              ## <li class="active"><a href="#">Home</a></li>
              ## <li><a href="#about">About</a></li>
              ## <li><a href="#contact">Contact</a></li>
            ## </ul>
          ## </div>
        </div>
      </div>
    </div>

    <div class="container">
      <%block name="content" />

      ## <!-- Example row of columns -->
      ## <div class="row">
        ## <div class="span4">
          ## <h2>Heading</h2>
           ## <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
          ## <p><a class="btn" href="#">View details &raquo;</a></p>
        ## </div>
        ## <div class="span4">
          ## <h2>Heading</h2>
           ## <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
          ## <p><a class="btn" href="#">View details &raquo;</a></p>
       ## </div>
        ## <div class="span4">
          ## <h2>Heading</h2>
          ## <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
          ## <p><a class="btn" href="#">View details &raquo;</a></p>
        ## </div>
      ## </div>

      <hr>

      <footer>
        <p>&copy; Company 2012</p>
      </footer>

    </div> <!-- /container -->
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script>window.jQuery || document.write('<script src="${static_path('/js/libs/jquery-1.7.2.min.js')}"><\/script>')</script>

<script src="${static_path('/js/libs/bootstrap/bootstrap.min.js')}"></script>
<script src="${static_path('/js/libs/bootstrap/typeahead.js')}"></script>

<script src="${static_path('/js/plugins.js')}"></script>
<script src="${static_path('/js/script.js')}"></script>
<script>
  var _gaq=[['_setAccount','UA-XXXXX-X'],['_trackPageview']];
  (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
  g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
  s.parentNode.insertBefore(g,s)}(document,'script'));
</script>

</body>
</html>
