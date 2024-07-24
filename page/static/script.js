const openExplanationButtons = document.querySelectorAll('[data-explanation-target]')
const closeExplanationButtons = document.querySelectorAll('[data-close-button]')
const overlay = document.getElementById('overlay')

openExplanationButtons.forEach(button => {
    button.addEventListener('click', () => {
        const explanation = document.querySelector(button.dataset.explanationTarget)
        openExplanation(explanation)
    })
})

closeExplanationButtons.forEach(button => {
    button.addEventListener('click', () => {
        const explanation = button.closest('.explanation')
        closeExplanation(explanation)
    })
})

function openExplanation(explanation) {
    if (explanation == null) return
    explanation.classList.add('active')
    overlay.classList.add('active')
}

function closeExplanation(explanation) {
    if (explanation == null) return
    explanation.classList.remove('active')
    overlay.classList.remove('active')
}