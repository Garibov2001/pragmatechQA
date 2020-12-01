function actions(id, user, type, vote) {
  $.ajax({
    type: "POST",
    url: `${window.location.href}`,
    data: { action_type: vote, id: id, user: user, type: type, csrfmiddlewaretoken: window.CSRF_TOKEN },
    dataType: "json",
    success: function (response) {
      if (vote == "dislike") {
        if (response.disliked == "True") {
          console.log('bobobo');
          count = $(".dislike_" + id + "_count").html();
          $(".dislike_" + id + "_count").html(parseInt(count) - 1);
          $(".dislike_" + id).css("fill", "#666f74");
          
        } else {
          count = $(".dislike_" + id + "_count").html();
          $(".dislike_" + id + "_count").html(parseInt(count) + 1);
          $(".dislike_" + id).css("fill", "#2c62a0");
          if (response.liked == "True"){
            console.log('bobobo');
            count = $(".like_" + id + "_count").html();
            $(".like_" + id + "_count").html(parseInt(count) - 1);
            $(".like_" + id).css("fill", "#666f74");
          }
        }
      }
      else if (vote == "like"){
        if (response.liked == "True") {
          console.log('bobobo');
          count = $(".like_" + id + "_count").html();
          $(".like_" + id + "_count").html(parseInt(count) - 1);
          $(".like_" + id).css("fill", "#666f74");
          
        } else {
          count = $(".like_" + id + "_count").html();
          $(".like_" + id + "_count").html(parseInt(count) + 1);
          $(".like_" + id).css("fill", "#2c62a0");
          if (response.disliked == "True"){
            console.log('bobobo');
            count = $(".dislike_" + id + "_count").html();
          $(".dislike_" + id + "_count").html(parseInt(count) - 1);
          $(".dislike_" + id).css("fill", "#666f74");
          }
        }
      }
    },
  });
}
