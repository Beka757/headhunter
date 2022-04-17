let messageInput = $('#messageInput')[0];
let messageSentBtn = $('#messageSentBtn')[0];

let responseId = messageSentBtn.dataset.responseId;
let userId = messageSentBtn.dataset.userId;

messageSentBtn.addEventListener('click', (e) => {
    $.ajax({
        method: 'post',
        url: `http://127.0.0.1:8000/api-v1/response/${responseId}/chat/`,
        headers: {'Authorization': `Token ${localStorage.apiToken}`},
        data: JSON.stringify({
            user: userId,
            response: responseId,
            text: messageInput.value
        }),
        dataType: 'json',
        contentType: 'application/json',
        success: function (data) {
            location.reload();
        },
        error: function (response) {
            console.log(response)
        }
    });
})

