let updateButton = $('#button_update')[0];
updateButton.addEventListener('click', (e) => {
    e.preventDefault()
    let summary = $('#button_update').data('summary-id')
    let position = $('#button_update').data('position')
    $.ajax({
        url: `http://127.0.0.1:8000/api-v1/summary/${summary}/update/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({summary_position: position}),
        dataType: "json",
        contentType: "application/json",
        success: function () {
            $.ajax({
                url: `http://127.0.0.1:8000/api-v1/summary/${summary}/update/`,
                method: 'GET',
                headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
                dataType: "json",
                contentType: "application/json",
                success: (data) => {
                    let updatedAt = document.getElementById('update_date');
                    var options = {
                        day: 'numeric',
                        month: 'numeric',
                        year: 'numeric',
                        hour: 'numeric',
                        minute: 'numeric'
                    }

                    function getDate(str) {
                        var date = new Date(str);
                        return date.toLocaleString('ru', options)
                    }

                    updatedAt.innerHTML = `${getDate(data.updated_at)}`
                },
                error: function (response, status) {
                    console.log(response.responseJSON.error);
                },
            });
        },
        error: function (response, status) {
            console.log(response.responseJSON.error);
        }
    });
})