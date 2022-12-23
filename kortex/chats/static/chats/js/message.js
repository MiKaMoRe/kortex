class Message{
  constructor(data){
    this.text = data["text"]
    this.created_at = data["created_at"]
    this.author = data["author"]
  }

  generate(){
    const message = $('#message-example').clone() // Clone message template
    const date = new Date(this.created_at)

    $(message)
      .removeClass('d-none') // Makes message visible
      .removeAttr('id')
    $(message)
      .find(".time")
      .append(date.getHours() + ":" + ("0" + date.getMinutes()).slice(-2)) // Add date of message
    $(message)
      .find(".text")
      .append(this.text) // Add text of message
    $(message)
      .find(".name")
      .attr('href', '/' + this.author["slug"]) // Add authors link
      .append(this.author["first_name"] + " ") // Add authors name
      .append(this.author["last_name"] + " ")
  
    return message
  }
}