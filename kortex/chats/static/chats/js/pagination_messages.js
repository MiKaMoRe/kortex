$(document).ready(() => {
  $('#message-list').animate({
    scrollTop: $('#message-list')[0].scrollHeight
  }, 0)
  
  let pageNumber = 2

  $('#message-list').scroll(e => {
    if (e.target.scrollTop != 0){
      return false
    }

    let oldScrollHeight = e.target.scrollHeight

    $.ajax({
      type: "GET",
      url: "?page=" + pageNumber,
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      success: data => {
        data["messages"].forEach(messageData => {
          const message = new Message(messageData).generate()
          $('#message-list').prepend(message) // Add message
        });

        pageNumber += 1
        
        $('#message-list').animate({
          scrollTop: e.target.scrollHeight - oldScrollHeight
        }, 0)
      }
    })
  })
})