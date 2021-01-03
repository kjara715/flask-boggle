$(function(){

    alert("am I working?")

    const $submitWord=$("#submit-word");
    const $wordGuess=$("#word-guess");
    
    $("#submit-word").on("submit", async function(e){
        e.preventDefault()
        console.log('testing')
        // await axios.post('/word-guess')
    })

})
