let buttonPublicationFalse = $('#publication_false')[0];
buttonPublicationFalse.addEventListener('click', (e) => {
    e.preventDefault()
    let vacancy = $('#publication_false').data('vacancy-id');
    $.ajax({
        url: `http://127.0.0.1:8000/api-v1/vacancy/${vacancy}/publication/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({publication: 'True'}),
        dataType: "json",
        contentType: "application/json",
        success: () => {
            let fPublication = $('#publication_false')[0];
            fPublication.style.display = 'none'
            let tPublication = $('#publication_true')[0];
            tPublication.style.display = 'inline'
        },
        error: function (response, status) {
            console.log(response.responseJSON.error);
        }
    });
});
let buttonPublicationTrue = $('#publication_true')[0];
buttonPublicationTrue.addEventListener('click', (e) => {
    e.preventDefault()
    let vacancy = $('#publication_true').data('vacancy-id');
    $.ajax({
        url: `http://127.0.0.1:8000/api-v1/vacancy/${vacancy}/publication/`,
        method: 'PATCH',
        headers: {Authorization: "Token " + localStorage.getItem("apiToken")},
        data: JSON.stringify({publication: 'False'}),
        dataType: "json",
        contentType: "application/json",
        success: () => {
            let tPublication = $('#publication_true')[0];
            tPublication.style.display = 'none'
            let fPublication = $('#publication_false')[0];
            fPublication.style.display = 'inline'
        },
        error: function (response, status) {
            console.log(response.responseJSON.error);
        }
    });
});
