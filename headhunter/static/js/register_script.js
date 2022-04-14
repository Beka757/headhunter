let btnradio1 = $('#btnradio1')[0];
let btnradio2 = $('#btnradio2')[0];
let usernameLabel = $('#usernameLabel')[0];


btnradio1.addEventListener('click', (e) => {
    usernameLabel.innerHTML = 'Имя пользователя <span style="color: red;">*</span>'
})


btnradio2.addEventListener('click', (e) => {
    usernameLabel.innerHTML = 'Имя кампании <span style="color: red;">*</span>'
})

