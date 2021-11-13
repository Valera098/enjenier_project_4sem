window.addEventListener('DOMContentLoaded', (e) => {
  const arrowRightElement = document.querySelector('.arrowRight')
  const arrowLeftElement = document.querySelector('.arrowLeft')
  arrowRightElement.addEventListener('click', () => {
    turnSlide('right')
  })
  arrowLeftElement.addEventListener('click', () => {
    turnSlide('left')
  })
});
const turnSlide = (direction) => {
  const currentSlide = document.querySelector('.slide.active');
  const container = document.querySelector('.slider');
  const nextSlide = getNextSlide(container, currentSlide, direction);
  toggleClasses(currentSlide, 'prevSlide', direction)
  toggleClasses(nextSlide, 'nextSlide', direction)
}
const toggleClasses = (slide, className, direction) =>{
  slide.classList.toggle(className)
  slide.classList.toggle(direction)
  slide.classList.toggle('active')
  slide.addEventListener('animationend', ()=>{
    slide.classList.toggle(className)
    slide.classList.toggle(direction)
  }, {once:true})

}
const getNextSlide = (container, currentSlide, direction) => {
  const slides = Array.from(container.children);
  const currentSlideIndex = slides.findIndex((slide) => slide.classList.contains('active'));
  let nextSlideIndex;
  switch (direction) {
    case 'right':
      nextSlideIndex = currentSlideIndex + 1;
      if (nextSlideIndex === slides.length) nextSlideIndex = 0;
      break;
    case 'left':
      nextSlideIndex = currentSlideIndex - 1;
      if (nextSlideIndex === -1) nextSlideIndex = slides.length-1;
      break;
  }
  return slides[nextSlideIndex];
}

