const getWeather = async (city) => {
    try {
        cityName.innerHTML = city;
        const url = `https://weather-by-api-ninjas.p.rapidapi.com/v1/weather?city=${city}`;
        const options = {
            method: 'GET',
            headers: {
                'X-RapidAPI-Key': '0c1bf18d84msh44749a25d7dd5c8p17c67ejsn9620656e60a2',
                'X-RapidAPI-Host': 'weather-by-api-ninjas.p.rapidapi.com'
            }
        };

        const response = await fetch(url, options);
        const result = await response.json(); // Parse response as JSON
        console.log(result);

        // Update HTML elements with weather data
        cloud_pct.innerHTML = result.cloud_pct;
        temp.innerHTML = result.temp;
        feels_like.innerHTML = result.feels_like;
        humidity.innerHTML = result.humidity;
        min_temp.innerHTML = result.min_temp;
        max_temp.innerHTML = result.max_temp;
        wind_speed.innerHTML = result.wind_speed;
        wind_degrees.innerHTML = result.wind_degrees;
        sunrise.innerHTML = result.sunrise;
        sunset.innerHTML = result.sunset;
    } catch (error) {
        console.error(error);
    }
};

// Assuming you have HTML elements with corresponding IDs
const cityName = document.getElementById('cityName');
const cloud_pct = document.getElementById('cloud_pct');
const temp = document.getElementById('temp');
const feels_like = document.getElementById('feels_like');
const humidity = document.getElementById('humidity');
const min_temp = document.getElementById('min_temp');
const max_temp = document.getElementById('max_temp');
const wind_speed = document.getElementById('wind_speed');
const wind_degrees = document.getElementById('wind_degrees');
const sunrise = document.getElementById('sunrise');
const sunset = document.getElementById('sunset');
const submit = document.getElementById('submit');
const cityInput = document.getElementById('city');

submit.addEventListener("click", (e) => {
    e.preventDefault(); // Prevent default form submission
    getWeather(cityInput.value);
});
getWeather('Delhi');