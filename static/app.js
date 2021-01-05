

$(async function(){
    let score=0;
    let count=60;
    
    $("#submit-word").on("submit", async function(e){
        e.preventDefault() //prevents page refresh
        console.log('testing')


        const wordGuess=$('#word-guess').val()
        const response = await axios.get('/word-guess', {params:{
            word: wordGuess
        }
    })
        
        if(response.data.result === "not-word"){
            $(".message").text(`${wordGuess} is not an english word`)
        } else if (response.data.result === "not-on-board"){
            $(".message").text(`${wordGuess} is not on this board`)
        } else {
            $(".message").text(`${wordGuess} is a valid word on this board`)
            score+=wordGuess.length;
            $(".score").text(`${score}`)
        }

        $('#word-guess').val('')
    }) //want to send a post request to the server without refreshing the page
    
    
    let timer = setInterval( async function(){
        count--
        $(".timer").text(`${count}`)
        if(count === 0){
            alert(`Your time is up! Your final score is ${score}`)
            clearInterval(timer)
            $('#submit-word').off()
            const response =  await axios.post('/score',  {
                currentScore: score
            })
    
            if(response.data.brokeRecord){
                console.log(`New record is ${score}`);
            } else {
                console.log(`Your score is ${score}`);
            }
        }
    }, 1000)
    
}
)

