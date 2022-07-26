var socket = io();

socket.on('connect', ()=>{
    socket.emit('user_connected', uname);
});

socket.on('user_connected', (data)=>{
    var alert = $("<p></p>").text(`${data}`);
    alert.addClass("connected-message");
    $("#chatroom").append(alert);
});

socket.on('user_message', (data)=>{

    var item = $("<div></div>");
    if (data['user'] === uname){
        item.addClass("sent-message message");
    }else{
        item.addClass("received-message message");
    }
    var usr = $("<p></p>");
    usr.addClass("message-header");
    usr.text(`${data['user']}`);
    var msg = $("<p></p>");
    msg.addClass("message-content");
    msg.text(`${data['message']}`);
    item.append(usr);
    item.append(msg);
    $("#chatroom").append(item);
});

$("#send-message-button").click(()=>{
    var message = $("#message-input-box").val();
    socket.emit('user_message', {'user': uname, 'message': message});
})

