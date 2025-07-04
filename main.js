// Variable global para almacenar el mapa
let mapa;

// Objeto para guardar los marcadores de los pozos, con su ID como clave
let marcadores = {};

// Función que inicializa el mapa
function inicializarMapa() {
  // Coordenadas centrales del mapa (San Miguel de Tucumán)
  const centro = { lat: -26.8241, lng: -65.2226 };

  // Crear el mapa y asignarlo al elemento con id="mapa"
  mapa = new google.maps.Map(document.getElementById("mapa"), {
    center: centro, // Centro del mapa
    zoom: 13,        // Nivel de zoom inicial
  });

  // Llamar a la función para cargar los pozos por primera vez
  actualizarPozos();

  // Configurar una actualización automática cada 10 segundos
  setInterval(actualizarPozos, 10000);
}

// Función para obtener y actualizar los datos de los pozos en el mapa
function actualizarPozos() {
  // Cargar el archivo JSON con los datos de los pozos
  // Se agrega un parámetro "nocache" con el tiempo actual para evitar que el navegador use una versión cacheada
  fetch("datos.json?nocache=" + new Date().getTime())
    .then(response => response.json()) // Convertir la respuesta en JSON
    .then(pozos => {
      // Recorrer cada pozo recibido en el archivo
      pozos.forEach(pozo => {
        const id = pozo.nombre; // Usar el nombre del pozo como identificador único

        // Determinar el color del marcador según el estado del pozo
        let color = "green"; // Estado por defecto: activo
        switch (pozo.estado) {
          case "En mantenimiento":
            color = "yellow";
            break;
          case "Inactivo":
            color = "red";
            break;
          case "Emergencia":
            color = "orange";
            break;
          default:
            color = "green";
        }

        // URL del ícono del marcador basado en el color
        const icono = `https://maps.google.com/mapfiles/ms/icons/${color}-dot.png`;

        // Contenido que se mostrará en la ventana emergente al hacer clic en el marcador
        const nuevoContenido = `<strong>${pozo.nombre}</strong><br>Estado: ${pozo.estado}`;

        // Si el marcador ya existe en el mapa
        if (marcadores[id]) {
          const marcadorExistente = marcadores[id].marker;
          const infoExistente = marcadores[id].info;

          // Actualizar el ícono si cambió el estado
          if (marcadorExistente.getIcon() !== icono) {
            marcadorExistente.setIcon(icono);
          }

          // Actualizar el contenido de la InfoWindow si cambió
          if (infoExistente.getContent() !== nuevoContenido) {
            infoExistente.setContent(nuevoContenido);
          }

        } else {
          // Si el marcador no existe, crearlo y agregarlo al mapa
          const marcador = new google.maps.Marker({
            position: { lat: pozo.lat, lng: pozo.lng }, // Posición del marcador
            map: mapa,                                  // Mapa donde se mostrará
            title: pozo.nombre,                         // Texto al pasar el mouse
            icon: icono                                 // Ícono determinado por el estado
          });

          // Crear una ventana de información para el marcador
          const info = new google.maps.InfoWindow({
            content: nuevoContenido
          });

          // Asignar un evento para mostrar la InfoWindow al hacer clic en el marcador
          marcador.addListener("click", () => {
            info.open(mapa, marcador);
          });

          // Guardar el marcador y su InfoWindow en el objeto "marcadores"
          marcadores[id] = {
            marker: marcador,
            info: info
          };
        }
      });
    })
    .catch(error => {
      // En caso de error al cargar o procesar el archivo JSON
      console.error("Error al actualizar los pozos:", error);
    });
}
