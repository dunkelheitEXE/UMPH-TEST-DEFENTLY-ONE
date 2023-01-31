from flask import Flask, render_template, request

# --- BOT PART ---
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('UPMH-V6')
words = [
    "Hola", "Hola! ¿Como puedo ayudarte?",
    "Me siento mal", "Contamos con una enfermeria en el edificio LT1. En este edifico podras encontrar al enfermero o enfermera que podra atender tu malestar o recetarte algo para atenderlo lo mas pronto posible. ¿O te refieres mas a un malestar emocional?",
    "Mal emocionalmente", "Puedes acudir con tus orientadores en su respectivo edificio. Puedes consultar en metronet quien es tu orientador de turno, ademas de que en cada cuatrimestre, este se presentara y te brindara la información y apoyo que necesites al respecto",
    "Necesito ayuda emocional", "Puedes acudir con tus orientadores en su respectivo edificio. Puedes consultar en metronet quien es tu orientador de turno, ademas de que en cada cuatrimestre, este se presentara y te brindara la información y apoyo que necesites al respecto",
    # Preguntas informales
    "¿Que eres?", "Soy una IA en camino de desarrollo. Mis creadores, unos estudiantes con buen potencial, de han hecho de herramientas, estudio e información para crearme. A pesar de ello, y como se puede ver, soy capaz de responder a ciertas preguntas. En breves palabras, estoy aqui para ayudarte con lo que necesites",
    "Hablame de ti", "Soy una IA en camino de desarrollo. Mis creadores, unos estudiantes con buen potencial, de han hecho de herramientas, estudio e información para crearme. A pesar de ello, y como se puede ver, soy capaz de responder a ciertas preguntas o consultas, pues podria responderte de muchas maneras aunque aun estoy en desarrollo. En breves palabras, estoy aqui para ayudarte con lo que necesites",
    # Preguntas sobre la Institución ---
    "¿Que es la UPMH?", "La Universidad Politecnica Metropolitan de Hidalgo, es una escuela hubicada en el municipio de Tolcayuca, dentro del estado de Hidalgo, en México, pais de norteamerica. La Universidad Politécnica Metropolitana de Hidalgo con base en el Decreto de Creación emitido por el Ejecutivo del Estado de Hidalgo, de fecha del 17 de noviembre de 2008 opera como Organismo Descentralizado de la Administración Pública del Estado de Hidalgo, con personalidad jurídica y patrimonio propio, teniendo como objeto impartir educación superior en los niveles de licenciatura, ingeniería, especialización tecnológica y otros estudios de posgrado, así como cursos de actualización en sus diversas modalidades, para preparar profesionales con una sólida formación científica, tecnológica y en valores cívicos y éticos, conscientes del contexto nacional en lo económico, político y social; Llevar a cabo investigación aplicada y desarrollo tecnológico, pertinentes para el desarrollo económico y social de la región, del Estado y de la Nación; Difundir el conocimiento de la cultura a través de la extensión universitaria y la formación a lo largo de toda la vida; Prestar servicios tecnológicos y de asesoría, que contribuyan a mejorar el desempeño de las empresas y otras organizaciones de la región y del Estado principalmente; Impartir programas de educación continua con orientación a la capacitación para el trabajo y al fomento a la cultura tecnológica de la región, en el Estado y en el País.\nFuente. Decreto de creación UPMH",
    #Becas
    "¿Como puedo saber sobre becas", "Puedes acudir al edificio UD1 con la Lic. Elisa Acuña. Ella podra ayudarte a atender tus dudas respecto a cualquier beca de forma presencial. Por otro lado, yo podria ayudarte tambien. Preguntame lo que quieras.",
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
    "¿Cual es el proceso de registro para la biblioteca?","Para ingresar a la biblioteca solo necesitas tu credencial que será escaneada para macar tu entrada  salida",
    #Servicios medicos
    "¿Puedo tener una consulta en servicio medico?","NR",
    "¿Donde se encuentra serivicio medico?","NR",
    "¿Que proporciona el servicio medico de la escuela?","NR",
    "¿Como se si ya estoy dado de alta en el serviocio medico?","NR",
    "¿Como hacer el tramite del servicio medico?","NR",
    "¿Cual es la fecha para terminar el proceso de inscripcion al servicio medico?","NR",
    "¿En caso de un posible caso de Covid 19?,¿cual es el protocolo de ermergencia?","NR",
    #Talleres
    "¿Que talleres hay?", "Baile de salón, Danza folclórica, Baile Hip-Hop, Danza Jazz, Lirico, Caligrafía, Artes plásticas, Oratoria, Canto, Guitarra, Dibujo a lápiz, Teatro, Ballet Clásico, Voleibol Basquetbol, Futbol soccer, Futbol 7, Acondicionamiento físico, Ajedrez, Pilates, Porristas, Tae kwon Do, Futbol americano",
    "¿Para qué cuatrimestres estas disponibles los talleres?", "Los talleres están habilitados para primero, segundo y tercer cuatrimestre",
    "¿Cuáles son las fechas de inscripción?", "Las fechas suelen ser la tercera semana de clase",
    "¿Cuál es el proceso de inscripción a los talleres?", "Para cuando llegue la fecha un apartado en tu metrón llamado 'talleres' aparecería en donde aparecerá una lista de los talleres para que puedas escoger y confirmar cual taller quiere",
    "¿Los talleres son obligatorios?", "Sí, así como acreditarlos es igualmente necesarios",
    "¿Solo puedo tomar un taller por cuatrimestres?", "No necesariamente puedes consultar con XX para más información",
    "¿Puedo iniciar mi propio taller?", "Sí, pero hay todo un protocolo para poder crear uno, pregunta a XX para más información",
    "¿Como puedo cambiar de taller?", "El cambio de taller esta hábil los primeros días que las actividades de taller empiecen, sin embargo, por situaciones extraordinarias es posible cambiar terminando un corte",
    "¿Se agregan más talleres?", "Por el momento no",
    "¿Como puedo abandonar mi taller?", "Solo en caso que te cambies de taller",
    "¿Puedo escoger un horario para los talleres?", "No, todos los talleres ya tienen un horario definido, así que escoge uno que no se cruce con tus clases",
    "¿Que pasaría si se cruzan los talleres con mis clases?", "Deberás solicitar un cambio de taller los primeros días, para que esto no afecte a tus clases. Intente escoger desde el inicio un taller que no se cruce con ninguna de tus clases ",

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

def initialMes(firs):
    res = bot.get_response(firs)
    return res

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def index():

    try:
        usermess = request.form.get("message")
        response = bot.get_response(usermess)


        # DATA --- (Dictionary)
        data = {
            'usermess': usermess,
            'response': response,

        }
        
        return render_template("index.html", data=data)
        #return render_template('hoja.html')
    except ChatBot.ChatBotException:
        usermess = "Hola"
        response = bot.get_response(usermess)


        # DATA --- (Dictionary)
        data = {
            'usermess': usermess,
            'response': response,

        }

        return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)