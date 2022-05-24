const sendBt = document.querySelector('#send')
const room = document.querySelector('.room')
    //when send bt is clicked, let the message box appear
class msgBox {
    constructor(room) {
        const msginp = document.querySelector('#messagebox')
        this.room = room
        var template = document.querySelector('template');
        this.msg_box_node = template.content.cloneNode(true)
        this.msg_box = this.msg_box_node.querySelector('.messagebox')
        this.msg = this.msg_box_node.querySelector('.msg')
        this.msg.textContent = msginp.value
    }
    show_msg() {
        this.room.appendChild(this.msg_box_node)

    }
}
sendBt.addEventListener('click', () => {
    msg = new msgBox(room)
    msg.show_msg()
})