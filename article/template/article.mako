<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">

    <!-- Font Awesome -->
    <link href="https://use.fontawesome.com/releases/v5.0.6/css/all.css" rel="stylesheet">

    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-115451279-1"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'UA-115451279-1');
    </script>

    <!-- My own style -->
    <link rel="stylesheet" href="../../src/custom/css/base.css">
    <link rel="stylesheet" href="../../src/custom/css/sidebar.css">
    <link rel="stylesheet" href="../../src/custom/css/post-header.css">
    <link rel="stylesheet" href="../../src/custom/css/article.css">

    <!-- title -->
    <title> ${data['head']} | Li-Ke's blog </title>
    <meta name="Keywords" content="template">

  </head>

  <body>

    <%include file="../../widget/side-navbar.html"/>

    <div class="post-header">
      <div class="post-header-img" style="background-image: url(${data['title_img']})">
        </div>
        <div class="post-header-text text-white">
          <h1> ${data['title']} </h1>
          <p> ${data['author']}</p>
        </div>
    </div>

    <div class="article-content">

        <div class="article-info"> 
          by ${data['author']}, ${data['date']}
        </div>

        <%include file="${data['content_ref']}"/>

    </div>


    <!-- jQuery first, then Bootstrap JS. -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>

    <!-- mathjax -->
    <script type="text/x-mathjax-config">
      MathJax.Hub.Config({
        tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
      });
    </script>
    <script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML"></script>

    <!-- sidebar control js -->
    <script src="../../src/custom/js/sidebarCollapse.js"></script>

    <!-- navbar auto hiding -->
    <script src="../../src/custom/js/autohidingnavbar.min.js"></script>
    <script>
      $(document).ready(function(){
        $("#navbar .navbar").autoHidingNavbar();
      })
    </script>
  </body>
</html>
