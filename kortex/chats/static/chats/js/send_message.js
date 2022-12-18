$(document).ready(() => {
  $('#send_message').submit((e) => {
    e.preventDefault();

    let form = $('#send_message')
    let actionUrl = form.attr('action')

    $.ajax({
      type: "POST",
      url: actionUrl,
      data: form.serialize(), // serializes the form's elements.
      success: data => {
        $('#id_text').val('') // Clear input area

        let message = $('#message-example').clone() // Clone message template
        let text = data["message"]["text"]
        let slug = data["message"]["author_slug"]
        let first_name = data["message"]["author_first_name"]
        let last_name = data["message"]["author_last_name"]

        $(message).removeClass('d-none').removeAttr('id') // Makes message visible
        $(message).find(".name").attr('href', '/' + slug) // Add authors link
        $(message).find(".name").append(first_name + " " + last_name + " ") // Add authors name
        $(message).find(".text").append(text) // Add text of message

        $('#message-list').append(message) // Add message
        $('#message-list').animate({
          scrollTop: $('#message-list')[0].scrollHeight
        }, 1000) // Scroll to last message
      }
    })
  })
})