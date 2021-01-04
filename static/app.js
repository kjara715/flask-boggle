$(function(){
    
    $("#submit-word").on("submit", async function(e){
        e.preventDefault() //prevents page refresh
        console.log('testing')

        await axios.get('/word-guess') //want to send a post request to the server without refreshing the page

        // console.log($('#word-guess').val()) 
        // $('#word-guess').val('')
    })

})
