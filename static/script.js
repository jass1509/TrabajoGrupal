
document.addEventListener('DOMContentLoaded', function() {
    inicializarSistemaComentarios();
    
    marcarPaginaActiva();
    
    inicializarAnimaciones();
    
    inicializarFormularioContacto();
});

function inicializarSistemaComentarios() {
    const formularios = ['formComentarioFortnite', 'formComentarioGTA5', 'formComentarioDota', 'formComentarioMinecraft', 'formComentarioPou', 'formComentarioLeft', 'formComentarioMasJugados'];

    formularios.forEach(formId => {
        const form = document.getElementById(formId);
        if (form) {
            form.addEventListener('submit', function(e) {
                enviarComentario(form);
            });
        }
    });
}

function enviarComentario(form) {
    const nombre = form.querySelector('input[type="text"]').value;
    const texto = form.querySelector('textarea').value;
    
 
    fetch('tu_archivo_bd.php', {
        method: 'POST',
        body: new FormData(form) 
    })
    .then(res => {
        if(res.ok) {
            alert("Comentario guardado");
            location.reload();
        }
    });
}
// NAVEGACIÓN ACTIVA 
function marcarPaginaActiva() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('nav a');
    
    navLinks.forEach(link => {
        const linkPage = link.getAttribute('href');
        const isHome = (currentPage === '' || currentPage === 'index.html') && linkPage === 'index.html';
        const isMatch = linkPage === currentPage;
        
        if (isHome || isMatch) {
            link.classList.add('active');
        }
    });
}

// ANIMACIONES DE CARGA 
function inicializarAnimaciones() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    });
    
    document.querySelectorAll('section').forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });
}

document.addEventListener('DOMContentLoaded', function() {
 
    inicializarCarrito(); 

    inicializarSocialSidebar(); 

    inicializarFormularioContacto();
});


// FORMULARIO DE CONTACTO 

function inicializarFormularioContacto() {
    const formContacto = document.querySelector('form[action="{{ url_for("contacto") }}"]');
    if (!formContacto) return;

    formContacto.addEventListener('submit', function(e) {


        const nombre = formContacto.querySelector('#nombre');
        const correo = formContacto.querySelector('#correo');
        const mensaje = formContacto.querySelector('#mensaje');
        const terminos = formContacto.querySelector('[name="terminos"]');

        if (!nombre.value.trim() || !correo.value.trim() || !mensaje.value.trim() || !terminos.checked) {
            alert('Por favor, completa todos los campos obligatorios y acepta los términos.');
            e.preventDefault(); 
            return;
        }

    });
}


//RULETA DE IMÁGENES
const lista = document.querySelector('.game-list');
const items = document.querySelectorAll('.game-item');
let pos = 0;

document.querySelector('.next-arrow')?.addEventListener('click', () => {
    pos = (pos + 1) % items.length;
    lista.style.transform = `translateX(-${pos * 300}px)`;
});

document.querySelector('.prev-arrow')?.addEventListener('click', () => {
    pos = (pos - 1 + items.length) % items.length;
    lista.style.transform = `translateX(-${pos * 300}px)`;
});

// Sistema calificacion
function calificar(puntos) {
    console.log("calificar llamada con puntos:", puntos);  

    
    const estrellas = document.querySelectorAll('.estrellas-basicas span');
    estrellas.forEach((estrella, index) => {
        if (index < puntos) {
            estrella.textContent = '★';
            estrella.style.color = 'gold';
        } else {
            estrella.textContent = '☆';
            estrella.style.color = 'gray';
        }
    });

    const resultado = document.getElementById('resultado-rating');
    if (resultado) {
        resultado.textContent = `Enviando ${puntos} ★...`;
    }

    fetch(window.location.pathname, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `calificacion=${puntos}`
    })
    .then(response => {
        console.log("Respuesta del servidor:", response.status);
        if (response.ok) {
            location.reload(); 
        } else {
            console.error("Error:", response.statusText);
            alert('Error al enviar calificación (status ' + response.status + ')');
        }
    })
    .catch(error => {
        console.error("Error en fetch:", error);
        alert('Error de conexión');
    });
}
// Script para pagina random
    const API_KEY = "54552e32968d44a79ff88f6e58629b21";

async function juegoAleatorio() {
    const resultado = document.getElementById("resultado");
    resultado.innerHTML = "Cargando...";

    try {
 
        const res = await fetch(`https://api.rawg.io/api/games?key=${API_KEY}`);
        const data = await res.json();

 
        const juegos = data.results;
        const random = juegos[Math.floor(Math.random() * juegos.length)];

  
        resultado.innerHTML = `
            <h3>${random.name}</h3>
            <img src="${random.background_image}" width="250">
            <p>Rating: ${random.rating}</p>
            <p>Fecha de lanzamiento: ${random.released}</p>
        `;
    } catch (error) {
        resultado.innerHTML = "Error al cargar juego";
    }
}
// Mostrar/Ocultar íconos de redes sociales
document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.getElementById('toggleSocial');
    const icons = document.getElementById('socialIcons');

    if (toggleBtn && icons) {
        toggleBtn.addEventListener('click', function() {
            icons.classList.toggle('active');
            // Cambia el texto del botón + / ×
            toggleBtn.textContent = icons.classList.contains('active') ? '×' : '+';
        });
    }
});


// Carrito 
let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

// Función para actualizar la vista del carrito
function actualizarCarrito() {
    const carritoLista = document.getElementById('carrito-lista');
    const carritoVacio = document.getElementById('carrito-vacio');
    const totalPrecio = document.getElementById('total-precio');

    if (carritoLista && carritoVacio) {
        carritoLista.innerHTML = '';
        let total = 0;

        if (carrito.length === 0) {
            carritoVacio.style.display = 'block';
        } else {
            carritoVacio.style.display = 'none';
            carrito.forEach((item, index) => {
                total += parseFloat(item.precio || 0);
                const div = document.createElement('div');
                div.className = 'item-carrito';
                div.innerHTML = `
                    <img src="${item.imagen}" alt="${item.nombre}">
                    <div class="info">
                        <strong>${item.nombre}</strong>
                        <p class="precio">S/ ${parseFloat(item.precio).toFixed(2)}</p>
                    </div>
                    <button class="btn btn-danger quitar-item" data-index="${index}">Quitar</button>
                `;
                carritoLista.appendChild(div);
            });
        }

        if (totalPrecio) totalPrecio.textContent = `S/ ${total.toFixed(2)}`;
    }
}

// Agregar juego desde cualquier página
document.querySelectorAll('.agregar-carrito').forEach(btn => {
    btn.addEventListener('click', () => {
        const nombre = btn.dataset.nombre;
        const imagen = btn.dataset.imagen;
        const precio = parseFloat(btn.dataset.precio) || 0;

        carrito.push({ nombre, imagen, precio });
        localStorage.setItem('carrito', JSON.stringify(carrito));
        actualizarCarrito();
        alert(`${nombre} agregado al carrito!`);
    });
});

// Quitar un item individual
document.addEventListener('click', function(e) {
    if (e.target && e.target.classList.contains('quitar-item')) {
        const index = parseInt(e.target.dataset.index);
        if (!isNaN(index)) {
            carrito.splice(index, 1); // Elimina ese item
            localStorage.setItem('carrito', JSON.stringify(carrito));
            actualizarCarrito();
            alert('Juego quitado del carrito');
        }
    }
});

// Vaciar todo el carrito
const vaciarBtn = document.getElementById('vaciar-carrito');
if (vaciarBtn) {
    vaciarBtn.addEventListener('click', () => {
        carrito = [];
        localStorage.removeItem('carrito');
        actualizarCarrito();
        alert('Carrito vaciado completamente');
    });
}

// Cargar carrito al abrir cualquier página (especialmente carrito.html)
window.addEventListener('load', actualizarCarrito);


function enviarWhatsApp() {
    const telefono = "51950736331"; 
    
   
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    
    if (carrito.length === 0) {
        alert("El carrito está vacío");
        return;
    }

    //  construir el mensaje
    let mensaje = "¡Hola GamerStore! \nQuiero comprar los siguientes productos:\n\n";
    let total = 0;

    carrito.forEach((producto, index) => {
        mensaje += `${index + 1}. *${producto.nombre}* - $${producto.precio}\n`;
        total += producto.precio;
    });

    mensaje += `\n*Total a pagar: $${total}*`;

    
    const mensajeCodificado = encodeURIComponent(mensaje);

    const urlWhatsApp = `https://wa.me/${telefono}?text=${mensajeCodificado}`;
    window.open(urlWhatsApp, '_blank');
}