$(document).ready(() => {
  $('#send_message').submit((e) => {
    e.preventDefault();

    $.ajax({
      type: "POST",
      url: $('#send_message').attr('action'),
      data: $('#send_message').serialize(), // serializes the form's elements.
      success: data => {
        const message = new Message(data["message"]).generate()

        $('#id_text').val('') // Clear input area
        $('#message-list').append(message) // Add message
        $('#message-list').animate({
          scrollTop: $('#message-list')[0].scrollHeight
        }, 1000) // Scroll to last message
      }
    })
  })
})