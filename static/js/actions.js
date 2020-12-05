function vote_actions(type, id, color, value, label){
  count = $(type + id + "_count" + '[label=\''+ label + '\']').html();
  $(type + id + "_count" + '[label=\''+ label + '\']').html(parseInt(count) + value);
  $(type + id + '[label=\''+ label + '\']').css("fill", color);
  console.log($(type + id + "_count" + '[label=\''+ label + '\']')[0])
  console.log($(type + id + '[label=\''+ label + '\']')[0])
}

function actions(id, user, type, vote, post_type, comment_id = null) {

  if(comment_id == null)
  {
    $.ajax({
      type: "POST",
      url: `${window.location.href}`,
      data: { 
        'post_type': post_type,
        'action_type': vote, 
        'id': id, 
        'user': user, 
        'type': type, 
        'csrfmiddlewaretoken': window.CSRF_TOKEN },
      dataType: "json",
      success: function (response) {
        console.log('qaqa question')
        if (vote == "dislike") {
          if (response.disliked == "True") 
          {
            vote_actions(".dislike_",id, "#666f74", - 1, 'question');
          } 
          else 
          {
            vote_actions(".dislike_",id, "#2c62a0", 1, 'question');
            if (response.liked == "True")
            {
              vote_actions(".like_",id, "#666f74", - 1, 'question');
            }
          }
        }
        else if (vote == "like")
        {
          if (response.liked == "True") 
          {
            vote_actions(".like_",id, "#666f74", - 1, 'question');
          } 
          else 
          {
            vote_actions(".like_",id, "#2c62a0", 1, 'question');
            if (response.disliked == "True"){
              vote_actions(".dislike_",id, "#666f74", - 1, 'question');
            }
          }
        }
      },
    });
  }
  else
  {
    $.ajax({
      type: "POST",
      url: `${window.location.href}`,
      data: { 
        'post_type': post_type,
        'action_type': vote, 
        'id': id, 
        'comment_id' : comment_id,
        'user': user, 
        'type': type, 
        'csrfmiddlewaretoken': window.CSRF_TOKEN },
      dataType: "json",
      success: function (response) {
        console.log('qaqa comment')
        if (vote == "dislike") 
        {
          if (response.disliked == "True") 
          {
            vote_actions(".dislike_",comment_id, "#666f74", - 1, 'comment');
          } 
          else 
          {
            vote_actions(".dislike_",comment_id, "#2c62a0", 1, 'comment');
            if (response.liked == "True")
            {
              vote_actions(".like_",comment_id, "#666f74", - 1, 'comment');
            }
          }
        }
        else if (vote == "like"){
          if (response.liked == "True") {
            vote_actions(".like_",comment_id, "#666f74", - 1, 'comment');
          } else {
            vote_actions(".like_",comment_id, "#2c62a0", 1, 'comment');
            if (response.disliked == "True"){
              vote_actions(".dislike_",comment_id, "#666f74", - 1, 'comment');
            }
          }
        }
      },
    });
  }

}


function check_answer(question_id, comment_id) 
{
    $.ajax({
      type: "POST",
      url: `${window.location.href}`,
      data: { 
        'question_id': parseInt(question_id), 
        'comment_id': parseInt(comment_id), 
        'post_type': 'select_answer',
        'csrfmiddlewaretoken': window.CSRF_TOKEN },

      dataType: "json",
      success: function (response) 
      {
        myList = document.querySelectorAll('[label="label_comment_id"]')
        
        // console.log(myList)
        for(var i = 0; i < myList.length;  i++)
        {
            if($(myList[i]).val() == comment_id)
            {
              console.log(response.fill_green)
              if(response.fill_green)
              {
                $(myList[i]).closest('.tt-item').find('.select_answer').css('fill','#48A868')
                $(myList[i]).closest('.tt-item').addClass('tt-wrapper-success')
                console.log($(myList[i]).closest('.tt-item'))

              }              
              else
              {
                $(myList[i]).closest('.tt-item').find('.select_answer').css('fill','#aeb3b4')
                $(myList[i]).closest('.tt-item').removeClass('tt-wrapper-success')
              }
            }
            else
            {
              $(myList[i]).closest('.tt-item').find('.select_answer').css('fill','#aeb3b4')
              $(myList[i]).closest('.tt-item').removeClass('tt-wrapper-success')

            }
          
          // console.log(i)
          // if($(myList[i]))

        }
        
        
      },
    });
  
}



