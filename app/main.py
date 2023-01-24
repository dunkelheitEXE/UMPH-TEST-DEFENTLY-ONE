from flask import Flask, render_template, request

# --- BOT PART ---
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('UPMH-V6')
words = [
    "Hola", "Hola, usuario!",
    "Me siento mal", "Contamos con una enfermeria en el edificio LT1",
    "Necesito ayuda emocional", "Puedes acudir con tus orientadores en su respectivo edificio",
    #Becas
    "¿Como puedo saber sobre becas", "Puedes acudir al edificio UD1 con la Lic. Elisa Acuña",
    "¿Que becas de movilidad hay?","Solo hay una beca de movilidad esta dirigida a estudiantes de escasos recursos, que no cuenten con ningún otro apoyo en efectivo o en especie y que colaboren en un servicio administrativo u operativo dentro de la Universidad.",
    "¿Por que no hay respuesta de jovenes escribiendo el futuro?","El encargados de la beca 'Jovenes Escribiendo El futuro' es gobierno del estado, no la universidad ",
    "¿Cuando son las fechas para las proximas becas?","Para la beca benito juarez podrar realizar el registro hasta el  de Diciembre del 2022,ingresa al sistema de citas. para mas informacion visita: ",
    "¿Cual es el proceso de tramite para becas?","El proseso para cada beca es diferente, el la sigiente lista puedes leer el proseso para cada beca o puedes acercarte a el departamento de becas ",
    "¿Cuales son las becas con las que cuenta la escuela?","'Lista de becas'",
    "¿Puedo tener mas de una beca?","No, Solo puedes tener una beca a la vez",
    "¿Como saber si soy beneficiario a una beca?","Pudes corroborar tu alta en el apartado de 'Becas' en Metronet",
    "¿Cuales son las fechas de los resultados de la beca?","Cada convocatoria tiene diferentes fechas, puedes consutalr esta informacion en http://www.upmh.edu.mx/ ",
    "¿Que pasa si mi beca fue rechazada?","Lo sentimos mucho. Puedes intentarlo la proxima vez en las proximas fechas",
    #Biblioteca
    "¿Tenemos biblioteca virtual?","No por el momento no se cuante con biblioteca virtual pero la escuela cuenta con convenios con paginas que te pueden ser utiles las cuale puedes encontrar en el siguiente link: https://www.upmetropolitana.edu.mx/centro-informacion/bibliotecas-digitales",
    "¿Es de libre acceso?","Si, el acceso es libre, solo ocupas tu credencial de estudiante de la UPMH ",
    "¿Cual es el proceso de registro para la biblioteca?","NR",
    #Servicios medicos
    "¿Puedo tener una consulta en servicio medico?","NR",
    "¿Donde se encuentra serivicio medico?","NR",
    "¿Que proporciona el servicio medico de la escuela?","NR",
    "¿Como se si ya estoy dado de alta en el serviocio medico?","NR",
    "¿Como hacer el tramite del servicio medico?","NR",
    "¿Cual es la fecha para terminar el proceso de inscripcion al servicio medico?","NR",
    "¿En caso de un posible caso de Covid 19?,¿cual es el protocolo de ermergencia?","NR",
    #Talleres
    "¿Que talleres hay?","Baile de salón, Danza folclórica, Baile Hip-Hop, Danza Jazz, Lirico, Caligrafía, Artes plásticas, Oratoria, Canto, Guitarra, Dibujo a lápiz, Teatro, Ballet Clásico, Voleibol Basquetbol, Futbol soccer, Futbol 7, Acondicionamiento físico, Ajedrez, Pilates, Porristas, Tae kwon Do, Futbol americano",
    "¿Para qué cuatrimestres estas disponibles los talleres?","Los talleres están habilitados para primero, segundo y tercer cuatrimestre",
    "¿Cuáles son las fechas de inscripción?", "Las fechas suelen ser la tercera semana de clase",
    "¿Cuál es el proceso de inscripción a los talleres?","Para cuando llegue la fecha un apartado en tu metrónet llamado 'talleres' aparecería en donde aparecerá una lista de los talleres para que puedas escoger y confirmar cual taller quiere",
    "¿Los talleres son obligatorios?", "Sí, así como acreditarlos es igualmente necesarios",
    "¿Solo puedo tomar un taller por cuatrimestres?", "No necesariamente puedes consultar con lic. Alma Delia Caballero para más información",
    "¿Puedo iniciar mi propio taller?", "Sí, pero hay todo un protocolo para poder crear uno, pregunta a lic. Alma Delia Caballero para más información",
    "¿Como puedo cambiar de taller?", "El cambio de taller esta hábil los primeros días que las actividades de taller empiecen, sin embargo, por situaciones extraordinarias es posible cambiar terminando un corte",
    "¿Se agregan más talleres?", "Por el momento no",
    "¿Como puedo abandonar mi taller?", "Solo en caso que te cambies de taller",
    "¿Puedo escoger un horario para los talleres?", "No, todos los talleres ya tienen un horario definido, así que escoge uno que no se cruce con tus clases",
    "¿Que pasaría si se cruzan los talleres con mis clases?","deberás solicitar un cambio de taller los primeros días, para que esto no afecte a tus clases. Intente escoger desde el inicio un taller que no se cruce con ninguna de tus clases ",

    #Cordinacion de Idiomas
    "¿Habra nuevos idiomas en un futuro?","NR",
    "¿Cuales son los idiomas disponibles?","NR",
    "¿Que es la cordinacion de idiomas?","NR",
    "¿Cuales son las funciones de la coordinacion de idiomas?","NR",
    "¿La coordnacion de idiomas hace los examenes parciales de ingles?","NR",
    #Control Escolar
    "¿Que funciones tiene el departamento de Control Escolar?","NR",
    "¿Que tramites puedo hacer en Control Escolar?","NR",
    #Otros
    "¿El examen iTEP funciona para titulacion?","NR",
    "¿Cuando estara dispnible el gym?","NR",
    "","",
    "","",
    "","",
    "","",
    "","",
]
#sdsa

trainer = ListTrainer(bot)
trainer.train(words)

# --- FIN BOT PART ---


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    usermess = request.form.get("message")
    response = bot.get_response(usermess)


    # DATA --- (Dictionary)
    data = {
        'usermess': usermess,
        'response': response
    }
    
    return render_template("index.html", data=data)
    #return render_template('hoja.html')

if __name__ == '__main__':
    app.run(debug=True)