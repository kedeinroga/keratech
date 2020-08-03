$(document).ready(function() {
    // Le damos el valor del número de diapositivas a una variable.
    var imgItems = $('.slider li').length;
    // Creamos una variable para guardar la posición de la imagen presente.
    var imgPos = 1;
    // Agregamos código html de los puntos.
    for (i = 1; i <= imgItems; i++) {
        $('.pagination').append('<li><span class="fa fa-circle"></span></li>');
    }
    // Llamamos a todas las diapositivas del slider y las escondemos.
    $('.slider li').hide();
    // Mostramos la primera diapositiva.
    $('.slider li:first').show();
    // Cambiamos el color del primer botón.
    $('.pagination li:first').css({ 'color': 'var(--gris)' });
    // Ejecutamos todas las funciones (botones y flechas):
    $('.pagination li').click(pagination);
    $('.right span').click(nextSlider);
    $('.left span').click(prevSlider);

    setInterval(function() {
        nextSlider();
    }, 4000);

    // Funciones:
    function pagination() {
        // Posición de la paginación seleccionada.
        var paginationPos = $(this).index() + 1;
        // Ocultamos todos los slides.
        $('.slider li').hide();
        // Mostramos el slide seleccionado.
        $('.slider li:nth-child(' + paginationPos + ')').fadeIn();
        // Le damos estilos a la paginación seleccionada.
        $('.pagination li').css({ 'color': 'var(--blanco)' });
        $(this).css({ 'color': 'var(--gris)' });

        imgPos = paginationPos;
    }

    function nextSlider() {
        if (imgPos >= imgItems) {
            imgPos = 1;
        } else {
            imgPos++;
        }
        $('.pagination li').css({ 'color': 'var(--blanco)' });
        $('.pagination li:nth-child(' + imgPos + ')').css({ 'color': 'var(--gris)' });
        // Ocultamos todos los slides.
        $('.slider li').hide();
        // Mostramos el slide seleccionado.
        $('.slider li:nth-child(' + imgPos + ')').fadeIn();
    }

    function prevSlider() {
        if (imgPos <= 1) {
            imgPos = imgItems;
        } else {
            imgPos--;
        }
        $('.pagination li').css({ 'color': 'var(--blanco)' });
        $('.pagination li:nth-child(' + imgPos + ')').css({ 'color': 'var(--gris)' });
        // Ocultamos todos los slides.
        $('.slider li').hide();
        // Mostramos el slide seleccionado.
        $('.slider li:nth-child(' + imgPos + ')').fadeIn();
    }
});