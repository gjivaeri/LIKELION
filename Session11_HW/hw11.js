//hw1
const getRandomHexaColor = () => {
    // const hexa = '0123456789abcdef'
        var randomnum = 0;
        randomnum = Math.random()*0xffffff; //랜덤하게 16진수뽑기
        randomnum = parseInt(randomnum); //문자열 string타입의 숫자를 int타입으로 전환. 정수변환
    //  randomnum = Math.floor(Math.random()*0xffffff); //반버림으로 정수변환.
        randomnum = randomnum.toString(16); //객체정보를 문자열로리턴. 파라미터 16진수로
        return "#"+randomnum;
    };
    
        setInterval(() => {
            document.querySelector('body').style.backgroundColor = getRandomHexaColor();
        }, 100); //()이므로 파라미터 없다. 첫번째 인자의 함수를 100밀리세컨드 후에 실행 (return)


//hw2
const clockContent = document.querySelector('.now');

const getCurrentTime = () =>{
    const date = new Date();
    const month = date.getMonth()+1;
    const day = date.getDate();
    const year = date.getFullYear();
    const hour = date.getHours();
    const minutes = date.getMinutes();
    const seconds = date.getSeconds();
    const time = `${year}년 ${month<10?'0'+month:month}월 ${day<10?'0'+day:day}일 ${hour<10?'0'+hour:hour}시${minutes<10?'0'+minutes:minutes}분${seconds<10?'0'+seconds:seconds}초`
    clockContent.textContent = time;         
}   

const initClock = () => {
    getCurrentTime();
    setInterval(getCurrentTime, 1000);
}

initClock();