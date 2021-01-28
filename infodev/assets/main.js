let form = document.getElementById('filter');
let devicesContainer = document.querySelector('.devices');
let paginationContainer = document.querySelector('.pagination');
const token = 'e9c70d6bbedfcdfda63befa4029134c1e35175e9';
let render_data = (items) => {
    devicesContainer.innerHTML = '';
    if (items.length > 0) {
        for (let item of items) {
            devicesContainer.insertAdjacentHTML('afterbegin', `
                <div class="devices__item device">
                    <div class="device__name">
                        Название: ${item.name}
                    </div>
                    <div class="device__type">
                        Тип: ${item.device_type}
                    </div>
                    <div class="device__location">
                        Адрес: ${item.location_address}
                    </div>
                    <div class="device__latitude">
                        Широта: ${item.latitude}
                    </div>
                    <div class="device__longitude">
                        Долгота: ${item.longitude}
                    </div>
                    <div class="device__radius">
                        Радиус покрытия: ${item.zone_radius}
                    </div>
                 </div>
                `);
        }
    } else {
        devicesContainer.insertAdjacentHTML('afterbegin', '<p>Ничего не найдено, попробуйте изменить параметры фильтрации</p>');
    }
}

let render_pagination = (prev, next, number_pages) => {
    paginationContainer.innerHTML = '';
    if (prev) {
        paginationContainer.insertAdjacentHTML('afterbegin',
            `<a href="${prev}" class="page-controller prev-page">Предыдущая</a>`)
    }
    if (next) {
        paginationContainer.insertAdjacentHTML('beforeend',
            `<a href="${next}" class="page-controller next-page">Следующая</a>`)
    }
}

let clickPagination = (event) => {
    event.preventDefault();
    let href = event.target.href;
    axios.get(href, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    })
        .then(function (response) {
            let items = response.data.results;
            render_data(items);
            let next = response.data.next;
            let prev = response.data.previous;
            render_pagination(prev, next, null);
            let pageControllers = document.querySelectorAll('.page-controller');
            for (let pageController of pageControllers) {
                pageController.addEventListener('click', clickPagination);
            }
        })
}

axios.get('/api/devices/', {
    headers: {
            Authorization: `Bearer ${token}`
        }
})
    .then(function (response) {
        let next = response.data.next;
        let prev = response.data.previous;
        render_pagination(prev, next, null);
        let pageControllers = document.querySelectorAll('.page-controller');
        for (let pageController of pageControllers) {
            pageController.addEventListener('click', clickPagination);
        }
    })

let submitForm = (event) => {
    event.preventDefault();
    let data = new FormData(event.target);
    let params = {};
    for (let pair of data.entries()) {
        params[pair[0]] = pair[1];
    }
    axios.get('/api/devices', {
        headers: {
            Authorization: `Bearer ${token}`
        },
        params: params
    })
        .then(function (response) {
            let items = response.data.results;
            render_data(items);
            let next = response.data.next;
            let prev = response.data.previous;
            render_pagination(prev, next, null);
            let pageControllers = document.querySelectorAll('.page-controller');
            for (let pageController of pageControllers) {
                pageController.addEventListener('click', clickPagination);
            }
        })
        .catch(function (error) {
            console.log(error);
        })
}

form.addEventListener('submit', submitForm);