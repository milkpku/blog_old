<div id="comments"></div>
<link rel="stylesheet" href="https://imsun.github.io/gitment/style/default.css">
<script src="https://imsun.github.io/gitment/dist/gitment.browser.js"></script>
<script>
  var gitment = new Gitment({
    id: '${data["title"]}',
    owner: 'milkpku',
    repo: 'blog',
    oauth: {
      client_id: '81e1fd6c525e8019860e',
      client_secret: 'f27b35427bb21b651b0c59e60209405b3425ab06',
    },
  })
  gitment.render('comments')
</script>