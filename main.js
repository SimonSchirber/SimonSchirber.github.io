//get initial variables
var questions = JSON.parse(localStorage.getItem('questions'))
var flags = JSON.parse(localStorage.getItem('flags'))
var category = JSON.parse(localStorage.getItem('category'))
var associated_img = JSON.parse(localStorage.getItem('associated_img'))

document.getElementById('question_text').innerHTML = questions[0]

//initialize buttons
var elems = document.getElementById('center_questions')
for (var buttons = 0; buttons< questions.length; buttons++){
    var question = buttons + 1
    elems.insertAdjacentHTML('beforeend', `<button id = '${question}' class="question_unanswered" onclick = 'question_click("${question}")'>Question #${question}  <br> Category: ${category[buttons]}<br> Points: ${points[buttons]}<br></button>`) 
}
question_click(1)
if (localStorage.getItem('correct') !== null){
    var correct = JSON.parse(localStorage.getItem('correct'))
    calc_and_display_points(correct)
    for (var i = 0; i<correct.length; i++){
        var id_el = i+ 1
        if (correct[i] == 'True'){
            document.getElementById(`${id_el}`).style.background = 'green' 
        }
    }
}

