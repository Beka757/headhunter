let addExperience = $('#experience')[0];
let addEducation = $('#education')[0];
addExperience.addEventListener('click', () => {
    let workExperience = document.getElementById('work_div');
    workExperience.classList.remove('d-none')
});
addEducation.addEventListener('click', () => {
    let education = document.getElementById('education_div');
    education.classList.remove('d-none')
});
let workExperienceForm = $('#work_experience_form')[0];
workExperienceForm.addEventListener('submit', (e) => {
    e.preventDefault()

    let inputCompanyName = $('#company_name')[0];
    let inputWorkPosition = $('#work_position')[0];
    let inputResponsibilities = $('#responsibilities')[0];
    let inputStartWork = $('#start_work')[0];
    let inputFinishWork = $('#finish_work')[0];

    if (inputFinishWork.value) {
        $.ajax({
        url: 'http://127.0.0.1:8000/api-v1/summary/experience/create/',
        method: 'post',
        headers: {'Authorization': `Token ${localStorage.apiToken}`},
        data: JSON.stringify({
            "company_name": inputCompanyName.value,
            "work_position": inputWorkPosition.value,
            "responsibilities": inputResponsibilities.value,
            "start_work": inputStartWork.value,
            "finish_work": inputFinishWork.value
        }),
        dataType: 'json',
        contentType: 'application/json',
        success: (data) => {
            let inputWorkExperience = $('#work_experience')[0];
            inputWorkExperience.innerHTML += `<option selected value=${data.id}></option>`

            let workExperience = document.getElementById('work_div');
            workExperience.classList.add('d-none')

            $("#work_experience_form")[0].reset();
        },
        error: function(status){console.log(status);}
        });
    }
    else {
        $.ajax({
        url: 'http://127.0.0.1:8000/api-v1/summary/experience/create/',
        method: 'post',
        headers: {'Authorization': `Token ${localStorage.apiToken}`},
        data: JSON.stringify({
            "company_name": inputCompanyName.value,
            "work_position": inputWorkPosition.value,
            "responsibilities": inputResponsibilities.value,
            "start_work": inputStartWork.value
        }),
        dataType: 'json',
        contentType: 'application/json',
        success: (data) => {
            let inputWorkExperience = $('#work_experience')[0];
            inputWorkExperience.innerHTML += `<option selected value=${data.id}></option>`

            let workExperience = document.getElementById('work_div');
            workExperience.classList.add('d-none')

            $("#work_experience_form")[0].reset();
        },
        error: function(status){console.log(status);}
        });
    }
});
let educationForm = $('#education_form')[0];
educationForm.addEventListener('submit', (e) => {
    e.preventDefault()

    let inputEducationalCenter = $('#educational_center')[0];
    let inputSpeciality = $('#speciality')[0];
    let inputStartEducation = $('#start_education')[0];
    let inputFinishEducation = $('#finish_education')[0];


    if (inputFinishEducation.value) {
        $.ajax({
        url: 'http://127.0.0.1:8000/api-v1/summary/education/create/',
        method: 'post',
        headers: {'Authorization': `Token ${localStorage.apiToken}`},
        data: JSON.stringify({
            "educational_center": inputEducationalCenter.value,
            "speciality": inputSpeciality.value,
            "start_education": inputStartEducation.value,
            "finish_education": inputFinishEducation.value
        }),
        dataType: 'json',
        contentType: 'application/json',
        success: (data) => {
            let inputWorkEducation = $('#education_work')[0];
            inputWorkEducation.innerHTML += `<option selected value=${data.id}></option>`

            let workEducation = document.getElementById('education_div');
            workEducation.classList.add('d-none')

            $("#education_form")[0].reset();
        },
        error: function(status){console.log(status);}
        });
    }
    else {
        $.ajax({
        url: 'http://127.0.0.1:8000/api-v1/summary/education/create/',
        method: 'post',
        headers: {'Authorization': `Token ${localStorage.apiToken}`},
        data: JSON.stringify({
            "educational_center": inputEducationalCenter.value,
            "speciality": inputSpeciality.value,
            "start_education": inputStartEducation.value
        }),
        dataType: 'json',
        contentType: 'application/json',
        success: (data) => {
            let inputWorkEducation = $('#education_work')[0];
            inputWorkEducation.innerHTML += `<option selected value=${data.id}></option>`

            let workEducation = document.getElementById('education_div');
            workEducation.classList.add('d-none')

            $("#education_form")[0].reset();
        },
        error: function(status){console.log(status);}
        });
    }
})
