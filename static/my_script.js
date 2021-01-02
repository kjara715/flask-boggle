console.log("test")
const $submitWord = $("submit-word")
const $wordGuess=$("word-guess")

$submitWord.on("submit", async function(e){
    e.preventDefault() //prevents page refresh
    const res = await axios.get("http://127.0.0.1:5000/")
    console.log(res)
    // const word = $wordGuess.val()
    // console.log(word)
}
)

