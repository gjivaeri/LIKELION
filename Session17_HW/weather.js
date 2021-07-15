const input = document.querySelector('#city')
const button = document.querySelector('#submit')
const weatherBox = document.querySelector('#weatherBox')

const API_KEY = "cb11443d43507c6b6f8387a17051c3f9";

button.addEventListener('click', async()=>{
  const city = input.value;

try{
const forecast = await axios.get(
  `https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${API_KEY}`);
console.log(forecast);

for (let i = 0; i < 40; i ++){
const { main, description, icon } = forecast.data.list[i].weather[0];
const temp = Math.round(forecast.data.list[0].main.temp - 273.15);
const date = forecast.data.list[i].dt_txt
const humidity = forecast.data.list[i].main.humidity

const content = 
     `<br><div class="content">
     <div class="date">${date}</div>
     <img class="icon" src="http://openweathermap.org/img/w/${icon}.png">
     <div class="main">${main}</div>
     <div class="description">${description}</div>
     <div class="temp">${temp}°C</div>
     <div class="humidity">${humidity}%</div>
     </div>`

weatherBox.insertAdjacentHTML('beforeend', content);
    }
  }catch (error) { 
  console.log(error);
}
weatherBox.classList.add('weatherStyle')

});

