document.addEventListener('DOMContentLoaded', () => {
    const boxes = document.querySelectorAll('.job-box');
    boxes.forEach((box, index) => {
        setTimeout(() => {
            box.classList.add('animated');
        }, index * 100);
    });
});