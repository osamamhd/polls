const click = document.querySelector('#click');
const show = document.querySelector('#show');

click.addEventListener('click', () => {
    if(show.classList.contains('hidden')) {
        show.classList.remove('hidden');
    } else {
        show.classList.add('hidden');
    }
})