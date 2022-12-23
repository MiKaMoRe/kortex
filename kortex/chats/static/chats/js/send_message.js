$(document).ready(() => {
  const action = $('#send_message').attr("action")
  const url = `ws://${window.location.host}/ws${action}`
  const chatSocket = new WebSocket(url)

  chatSocket.onmessage = (e) => {
    const data = JSON.parse(e.data)
    const message = new Message(data["message"]).generate()

    $('#message-list').append(message) // Add message
    $('#message-list').animate({
      scrollTop: $('#message-list')[0].scrollHeight
    }, 1000) // Scroll to last message
  }

  $('#send_message').submit((e) => {
    e.preventDefault();

    $.ajax({
      type: "POST",
      url: $('#send_message').attr('action'),
      data: $('#send_message').serialize(), // serializes the form's elements.
      success: data => {
        chatSocket.send(JSON.stringify({
          'message': data["message"]
        }))

        $('#id_text').val('') // Clear input area
      }
    })
  })
})