<div class="card">
  <!--Card image-->
    <img class="card-img" src="${data['card_img']}" alt="Card image cap">

    <!--Card content-->
    <div class="card-body">
      <!-- link to article page -->
      <a class="card-link-cover" href="${data['article_path']}"></a>

      <!-- title of card -->
      <h3 class="card-title"> ${data['title']} </h3>

      <!-- abstract/introduction -->
      <p> ${data['abstract']} </p>

      <!-- tags -->
      <span class="badge badge-pill badge-info"> ${data['tag']} </span>
    </div>
</div>
