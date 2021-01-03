$(function(){

    alert("am I working?")

    const $submitWord=$("#submit-word");
    const $wordGuess=$("#word-guess"); //want to send this value to the server (on a new route?)
    
    $("#submit-word").on("submit", async function(e){
        e.preventDefault()
        console.log('testing')

        // await axios.post('/word-guess')

        $('#word-guess').val()='' //clear out value
    })

})
