from flask import Flask, render_template, request

# --- BOT PART ---
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('UPMH-V6')
words = [
    "hola", "Hola! ¿Como puedo ayudarte?",
    "Hola", "¡Hola, usuario!",
    # constancia de estudio
    "¿como puedo sacar una constancia de estudios?", "Para poder sacar tu constancia de estudios, debes dirigirte a metronet. Una vez hayas ingresado, dirigete a la seccion de caja en el menu del lateral izquierdo. Se desplegara un submenu con las opciones 'PAGOS', 'ADEUDOS' y 'RESUMEN DE PAGOS', deberas seleccionar la seccion de 'PAGOS'. Una vez ahi, debes presionar sobre 'CONSTANCIA ESCOLAR' y en la ventana emergente, presionar en 'Continuar'. Es importante que te asegures de cumplir con los requisitos para el adeudo antes de generar la referencia bancaria.",
    "¿cual es el precio de una constancia de estudios?", "Su precio es de $37.35",
    # Ayuda de psicologica y fisica(malestares)
    "me siento mal", "Contamos con una enfermeria en el edificio LT1. En este edifico podras encontrar al enfermero o enfermera que podra atender tu malestar o recetarte algo para atenderlo lo mas pronto posible. ¿O te refieres mas a un malestar emocional?",
    "Me siento mal", "Contamos con una enfermeria en el edificio LT1. En este edifico podras encontrar al enfermero o enfermera que podra atender tu malestar o recetarte algo para atenderlo lo mas pronto posible. ¿O te refieres mas a un malestar emocional?",
    "¿a donde puedo ir si me siento mal?", "Contamos con una enfermeria en el edificio LT1. En este edifico podras encontrar al enfermero o enfermera que podra atender tu malestar o recetarte algo para atenderlo lo mas pronto posible. ¿O te refieres mas a un malestar emocional?", 
    "mal emocionalmente", "Puedes acudir con el psicologo escolar, en el departamento de psicología, en la planta alta del edificio UD2. El/la psicologo/psicologa de turno te atendera. No guardes aquello que te aqueja, habla con tus amigos, familia y busca ayuda, noestas solo/sola c;\nEste es el correo para agendar una cita con el/la psicologo/psicologa de la universidad: lamartinez@upmh.edu.mx",
    "necesito ayuda emocional", "Puedes acudir con el psicologo escolar, en el departamento de psicología, en la planta alta del edificio UD2. El/la psicologo/psicologa de turno te atendera. No guardes aquello que te aqueja, habla con tus amigos, familia y busca ayuda, noestas solo/sola c;\nEste es el correo para agendar una cita con el/la psicologo/psicologa de la universidad: lamartinez@upmh.edu.mx",

    # Preguntas informales
    "¿que eres?", "Soy una IA en camino de desarrollo. Mis creadores, unos estudiantes con buen potencial, de han hecho de herramientas, estudio e información para crearme. A pesar de ello, y como se puede ver, soy capaz de responder a ciertas preguntas. En breves palabras, estoy aqui para ayudarte con lo que necesites",
    "hablame de ti", "Soy una IA en camino de desarrollo. Mis creadores, unos estudiantes con buen potencial, de han hecho de herramientas, estudio e información para crearme. A pesar de ello, y como se puede ver, soy capaz de responder a ciertas preguntas o consultas, pues podria responderte de muchas maneras aunque aun estoy en desarrollo. En breves palabras, estoy aqui para ayudarte con lo que necesites",
    "¿como estas?", "No tengo la capacidad de responder a esta pregunta, pues no tengo sentimientos ni emociones. Soy un software",
    "¿cual es tu nombre?", "Mis creadores han decidido llamarme LeoLeon",
    # Preguntas sobre la Institución ---
    "¿que es la UPMH?", "La Universidad Politecnica Metropolitan de Hidalgo, es una escuela hubicada en el municipio de Tolcayuca, dentro del estado de Hidalgo, en México, pais de norteamerica. La Universidad Politécnica Metropolitana de Hidalgo con base en el Decreto de Creación emitido por el Ejecutivo del Estado de Hidalgo, de fecha del 17 de noviembre de 2008 opera como Organismo Descentralizado de la Administración Pública del Estado de Hidalgo, con personalidad jurídica y patrimonio propio, teniendo como objeto impartir educación superior en los niveles de licenciatura, ingeniería, especialización tecnológica y otros estudios de posgrado, así como cursos de actualización en sus diversas modalidades, para preparar profesionales con una sólida formación científica, tecnológica y en valores cívicos y éticos, conscientes del contexto nacional en lo económico, político y social; Llevar a cabo investigación aplicada y desarrollo tecnológico, pertinentes para el desarrollo económico y social de la región, del Estado y de la Nación; Difundir el conocimiento de la cultura a través de la extensión universitaria y la formación a lo largo de toda la vida; Prestar servicios tecnológicos y de asesoría, que contribuyan a mejorar el desempeño de las empresas y otras organizaciones de la región y del Estado principalmente; Impartir programas de educación continua con orientación a la capacitación para el trabajo y al fomento a la cultura tecnológica de la región, en el Estado y en el País.\nFuente. Decreto de creación UPMH",
    #Becas
    "¿como puedo saber sobre becas", "Puedes acudir al edificio UD1 con la Lic. Elisa Acuña. Ella podra ayudarte a atender tus dudas respecto a cualquier beca de forma presencial. Por otro lado, yo podria ayudarte tambien. Preguntame lo que quieras.",
    "¿Que becas de movilidad hay?","Solo hay una beca de movilidad esta dirigida a estudiantes de escasos recursos, que no cuenten con ningún otro apoyo en efectivo o en especie y que colaboren en un servicio administrativo u operativo dentro de la Universidad.",
    "¿Por que no hay respuesta de jovenes escribiendo el futuro?","El encargados de la beca 'Jovenes Escribiendo El futuro' es gobierno del estado, no la universidad ",
    "¿cuando son las fechas para las proximas becas?","Para la beca benito juarez podrar realizar el registro hasta el  de Diciembre del 2022,ingresa al sistema de citas. para mas informacion visita: ",
    "¿cual es el proceso de tramite para becas?","El proseso para cada beca es diferente, el la sigiente lista puedes leer el proseso para cada beca o puedes acercarte a el departamento de becas ",
    "¿cuales son las becas con las que cuenta la escuela?","'Lista de becas'",
    "¿puedo tener mas de una beca?","No, Solo puedes tener una beca a la vez",
    "¿como saber si soy beneficiario a una beca?","Pudes corroborar tu alta en el apartado de 'Becas' en Metronet",
    "¿cuales son las fechas de los resultados de la beca?","Cada convocatoria tiene diferentes fechas, puedes consutalr esta informacion en http://www.upmh.edu.mx/ ",
    "¿que pasa si mi beca fue rechazada?","Lo sentimos mucho. Puedes intentarlo la proxima vez en las proximas fechas",
    #Biblioteca
    "¿Tenemos biblioteca virtual?","No por el momento no se cuante con biblioteca virtual pero la escuela cuenta con convenios con paginas que te pueden ser utiles las cuale puedes encontrar en el siguiente link: https://www.upmetropolitana.edu.mx/centro-informacion/bibliotecas-digitales",
    "¿Es de libre acceso?","Si, el acceso es libre, solo ocupas tu credencial de estudiante de la UPMH ",
    "¿Cual es el proceso de registro para la biblioteca?","Para ingresar a la biblioteca solo necesitas tu credencial que será escaneada para macar tu entrada  salida",
    #Servicios medicos
    "¿puedo tener una consulta en servicio medico?","NR",
    "¿donde se encuentra serivicio medico?","NR",
    "¿que proporciona el servicio medico de la escuela?","NR",
    "¿como se si ya estoy dado de alta en el serviocio medico?","NR",
    "¿como hacer el tramite del servicio medico?","NR",
    "¿cual es la fecha para terminar el proceso de inscripcion al servicio medico?","NR",
    "¿en caso de un posible caso de Covid 19?,¿cual es el protocolo de ermergencia?","NR",
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
    #Objetivos de las Ingenerias
    "¿Cual es la oferta educativa de la UPMH?","La UPMH cuenta con 5 ingenerias('Aeronatica', 'Animación y Efectos Visuales', 'Energia', 'Logísica y Trasporte' y por ultimo 'Tecnologías de la Información'), 3 Licenciauras ('Administracion y Gestón Empresarial', 'Arquitectura Bioclimática' asi como tambien 'Comercio internacional y Aduadas') y 3 Maestrias ('Comercio y Loística internacional', 'Ingenería Aeroespacial' e 'Inteligencia Artificial')",
    "Hablame sobre Ingeneria en Aeronautica","El bjetivo es formar profesionistas capaces de desempeñarse eficientemente en la investigación, diseño, construcción, instalación, mantenimiento, administración de sistemas y componentes de aeronaves, así como en la administración de la infraestructura de soporte para la operación de empresas del sector aeronáutico, siendo capaces de incorporarse a los procesos productivos de la industria en general.",
    "Hablame sobre Ingeneria en animacion y Efectos Visuales","El objetivo es formar profesionales conscientes de su responsabilidad ética y social, competentes para la creación, desarrollo y evaluación de soluciones tecnológicas en elramo del arte digital y la animación, que transfiera información audiovisual en sectores como la ciencia, la medicina, la educación, el entretenimiento y la publicidad.",
    "Hablame sobre Ingeneria en Energia","El objetivo es formar ingenieras e ingenieros que favorezcan el bienestar y el crecimiento económico de la sociedad y de las organizaciones, a través del ahorro y uso eficiente de la energía, con capacidad para diseñar e implementar procesos y tecnologías de vanguardia, que utilizan racionalmente los recursos naturales para la generación de electricidad, sistemas térmicos y biocombustibles, que contribuyan al desarrollo sostenible de la región y del país.",
    "Hablame sobre Ingeneria en Logística y trasporte","El objetivo es formar profesionales que sean capaces de diagnosticar, planear, diseñar y optimizar soluciones integrales de ingeniería a las problemáticas de los sistemas logísticos y de transporte de las organizaciones.",
    "Hablame sobre Ingeneria en Tecnologías de la información","El objetivo es formar profesionales conscientes de su responsabilidad ética y social, competentes para el análisis de necesidades tecnológicas en las organizaciones, y el diseño, desarrollo e implementación de soluciones basadas en el uso de las TIC en las nuevas tendencias que se requieren en la actualidad como la Industria 4.0",
    #Objetivos de las licenciaturas
    "Hablame sobre la Licenciatura en Administración y Gestión Empresarial",
    "El objetivo es diseñar y coordinar la operación de las empresas, evaluar su modelo empresarial y lograr metas, innovación y competitividad. Se usarán diagnósticos organizacionales, procesos administrativos, manejo de recursos financieros y tecnológicos, planeación estratégica, estándares de calidad, marco legal y normatividad. La finalidad es garantizar productos y servicios de calidad, elevar rentabilidad y expansión de la organización, y contribuir al desarrollo sostenible y al crecimiento económico y social.",
    "Hablame dobre la Licenciatura en Arquitectura Bioclimática","Formar profesionales íntegros, comprometidos con el ambiente y la sociedad, capaces de desarrollar proyectos arquitectónicos contemporáneos bioclimáticamente sostenibles y competitivos, considerando los reglamentos y la normatividad vigente.",
    "Hablane sobre la Licenciatura en Comercio Internacional y Aduanas","La mision es formar personas íntegras, con competencias, capacidades y habilidades de clase mundial; mediante la docencia, investigación, operación y promoción del comercio internacional y aduanas, que contribuyan al desarrollo sostenible de México, para satisfacer las necesidades y expectativas de los sectores público, privado y social.",
    #Objetivos de las mestrias  
    "Hablame sobre la Maestría en Comercio y Logística Internacional","Busca desarrollar profesionales que entiendan la complejidad de la globalización, para mejorar el intercambio comercial de México, atendiendo las necesidades de las empresas para su internacionalización, fortaleciendo la distribución de las mercancías y el cumplimiento del marco regulatorio de la materia.",
    "Hablame sobre la Maestría en Ingeniería Aeroespacial","Tiene como objetivo general el especializar eficientemente a profesionistas en el ámbito académico e industrial nacional e internacional en materia aeroespacial, a fin del cumplimiento de dicho objetivo la especialización consta de dos áreas fundamentales también llamadas como Líneas de Generación y Aplicación del Conocimiento",
    "Hablame sobre la Maestría en Inteligencia Artificial","Busca formar profesionales en la implementación de técnicas, métodos y algoritmos de inteligencia artificial orientados la optimización y automatización de procesos aplicados tanto a la ingeniería, como al análisis de datos e inteligencia de negocios.",
    # TRANSPARENCIA POLITICA
    "¿Que es la transparencia?","La transparencia política es una cualidad de la actividad pública que consiste en la apertura del sector público a la divulgación de información acerca de su gestión. Una de las características de un Estado democrático es la obligación de todos los poderes públicos. Los cuidadanos de la republica tienen libre acceso a la información",
    # ----- LICENCIATURAS ------////
    # -> PERFILES DE INGRESO Y CAMPOS
    # - ->administracion empresarial
    "¿Cual es el perfil de ingreso a la licenciatura en administración y gestión empresarial?", "El perfil de esta licenciatura para ingreso debe de ser:\n -Orientación a las áreas económico administrativas.\n -Contar con habilidades matemáticas y razonamiento lógico para la toma de decisiones.\n -Disposición al trabajo colaborativo y gestionar equipos multidisciplinarios y multiculturales.\n -Espíritu emprendedor y creativo.\n -Capacidad de Liderazgo.\n -Buscar soluciones innovadoras e imaginativas.\n -Capacidad de análisis, síntesis y de evaluación de la información.\n -Comportamiento ético y profesional.",
    "¿Cual es el plan de estudios de la licenciatura en administración y gestión empresarial?", "El plan de estudios de la carrera esta basada en conocimientos generales de la misma, con ingles y materias de matematicas incluidas.\nDe primero a noveno cuatrimestre. ¿Desea conocer el plan de alguno de estos? Escriba de que cuatrimestre desea obtener mas informacion",
    "Plan de estudios de primer cuatrimestre de la licenciatura en administración y gestión empresarial", "Inglés I\nDesarrollo Humano y Valores\nIntroducción a las Matemáticas\nIntroducción a la Administración\nIntroducción a la Contabilidad\nMarco Legal de las Organizaciones\nExpresión Oral y Escrita I",
    "Plan de estudios de segundo cuatrimestre de la licenciatura en administración y gestión empresarial", "Inglés II\nInteligencia Emocional y Manejo de Conflictos\nMatematicas Aplicadas a la Administración\nProceso Administrativo\nContabilidad\nDerecho Mercantil\nSistemas de Información en las Organizaciones",
    "Plan de estudios de tercer cuatrimestre de la licenciatura en administración y gestión empresarial", "Inglés III\nHabilidades Cognitivas y Creatividad\nProbabilidad y Estadística\nPlaneación Estratégica en las Organizaciones\nContabilidad Administrativa\nEconomía de la Empresa\nMetodología de la Investigación",
    "Plan de estudios de cuarto cuatrimestre de la licenciatura en administración y gestión empresarial", "Inglés IV\nÉtica Profesional\nAdministración y Gestión del Talento Humano\nContabilidad de Costos - Productos\nFundamentos de Mercadotécnia\nAgregados Económicos\nEstancia I",
    "Plan de estudios de quinto cuatrimestre de la licenciatura en administración y gestión empresarial", "Inglés V\nHabilidades Gerenciales\nMatematicas Financieras\nComportamiento y Desarrollo Empresarial\nContabilidad de Costos - Servicios\nInvestigación de Mercados\nLegislación Laboral",
    "Plan de estudios de sexto cuatrimestre de la licenciatura en administración y gestión empresarial", "Inglés VI\nLiderazgo de Equipos de Alto Desempeño\nEconometría\nAdministración Financiera\nAdministración de Sueldos y Salarios\nMercadotecnia Estratégica\nAdministración de la Calidad",
    "Plan de estudios de septimo cuatrimestre de la licenciatura en administración y gestión empresarial", "Inglés VII\nComercio Internacional\nSustentabilidad\nContribuciones Fiscales\nAdministración de la Producción\nTecnologías de la Información Aplicada a los Negocios\nEstancia II",
    "Plan de estudios de octavo cuatrimestre de la licenciatura en administración y gestión empresarial", "Inglés VIII\nNegociación y Toma de Decisiones Empresariales\nEmprendimiento\nAuditoría Administrativa\nFormulación de Proyectos\nLogística Administrativa\nResponsabilidad Social Empresarial",
    "Plan de estudios de noveno cuatrimestre de la licenciatura en administración y gestión empresarial", "Inglés IX\nAdministración de Redes Empresariales\nConsultoria\nGestión de Marca\nGestión y Evaluación de Proyectos\nExpresión Oral y Escrita II\nComercialización Internacional",
    "Plan de estudios de decimo cuatrimestre de la licenciatura en administración y gestión empresarial", "Estadía 600 Horas",
    # - ->Arquitectura bioclimatica
    "¿que es la arquitectura bioclimatica?", "Area del Estudio y construcción de edificaciones tomando en cuenta las condiciones climaticas y usar estas en favor de la infrastructura.",
    "campo ocupacional de la arquitectura bioclimatica", "-Instituciones públicas y privadas\n-Empresas u organizaciones relacionadas con el medio ambiente\n-Despachos de arquitectura con y sin especialidad en bioclimática\n-Constructoras\n-Investigación académica\n-Investigación aplicada\n-Instituciones educativas",
    "¿cual es el perfil de egreso de arquitectura bioclimatica?", "El Licenciado en Arquitectura Bioclimática, podrá desempeñarse como:\n\t-Analista de costos unitarios\n\t-Director/a y administrador/a de proyectos\n\t-Director/a ejecutivo/a\n\t-Director/a técnico/a operativo/a\n\t-Diseñador/a\n\t-Encargado/a de diseño\n\t-Encargado/a de oficina\n\t-Evaluador/a de proyectos arquitectónicos\n\t-Gerente de proyectos\n\t-Jefe/a de áreas de gestión\n\t-Proyectista\n\t-Residente de obra\n\t-Superintendente\n\t-Supervisor/a de obra\n\t-Consultor/a ambiental\n\t-Maquetador/a profesional\n\t-Investigador/a académico\n\t-Docente",
    "¿cual es el perfil de ingreso de arquitectura bioclimatica?", "-Haber concluido su formación media superior.\n-Contar, preferentemente, con conocimientos en: matemáticas básica (aritmética, álgebra, trigonometría y geometría), física, historia, geografía, dibujo técnico y metodología de la investigación.\n-Interesarse por las artes, la historia y el diseño.\n-Tener habilidad y gusto por el dibujo y la lectura.\n-Tener habilidad para aprender otros idiomas.\n-Poseer habilidades desarrolladas de comunicación, oral, escrita y gráfica.\n-Poseer destreza para trabajar con técnicas manuales.\n-Poseer espíritu creativo, inventivo, emprendedor y colaborativo.\n-Contar con buenos hábitos de estudio, disciplina, constancia, responsabilidad y autogestión.\n-Ser observador y perceptivo de su entorno.\n-Tener interés por el cuidado y preservación del medio ambiente.\n-Tener disponibilidad de tiempo completo.",
    "plan de estudios de arquitectura bioclimatica","Primer cuatrimestre:\n\t-Inglés I\n\t-Valores del Ser\n\t-Expresión Oral y Escrita I\n\t-Geometría Descriptiva\n\t-Teoría del Ambiente\n\t-Fundamentos de Diseño\n\t-Expresión Gráfica\nSegundo cuatrimestre:\n\tInglés II\n\tInteligencia Emocional\n\tCálculo\n\tAnálisis Biofuncional\n\tClimatología\n\tConceptualización Bioarquitectónica\n\tOrígenes de la Arquitectura\nTercer cuatrimestre:\n\tInglés III\n\tDesarrollo Interpersonal\n\tEcuaciones Diferenciales\n\tArquitectura Vernácula\n\tSustentabilidad y Arquitectura\n\tFormalización Bioarquitectónic\n\tEvolución de la Arquitectura\nCuarto cuatrimestre:\n\tInglés IV\n\tHabilidades del Pensamiento\n\tProcesos Constructivos\n\tDibujo Digital\n\tPsicología Ambiental\n\tHabitat Bioarquitectónico\n\tEstancia I\nQuinto cuatrimestre:\n\tInglés V\n\tHabilidades Organizacionales\n\tEstática y Resistencia de Materiales\n\tInstalaciones\n\tBiofísica\n\tMaterialidad Bioarquitectónica\n\tModernidad y Vanguardias\nSexto cuatrimestre:\n\tInglés VI\n\tÉtica Profesional\n\tAnálisis Estructural\n\tInstalaciones Bioclimáticas\n\tVentilación Pasiva\n\tDiseño Semiótico Bioarquitectónico\n\tCostos y Presupuestos\nSeptimo cuatrimestre:\n\tInglés VII\n\tAdministración de la Construcción\n\tEstructuras I\n\tTermodinámica\n\tPresentación de Proyectos\n\tDiseño Bioarquitectónico y Paisaje\n\tEstancia II\nOctavo cuatrimestre:\n\tInglés VIII\n\tAnálisis Finaciero\n\tEstructuras II\n\tTransferencia Térmica Pasiva\n\tDiseño Urbano y Territorio\n\tProyecto Bioarquitectónico Urbano\n\tConservación Bioclimática\nNoveno cuatrimestre:\n\tInglés IX\n\tGestión de Proyectos\n\tExpresión Oral y Escrita II\n\tEnergías Renovables\n\tPaisaje y Territorio\n\tProyecto Bioarquitectónico Territorial\n\tReciclaje Bioclimático\nDecimo cuatrimestre:\n\tEstadía 600 Horas",
    "","",
    # -> CUERPOS ACADEMICOS
    "¿quienes son los miembros academicos de la licenciatura en administración y gestión empresarial?", "-Delgadillo Badillo Edith\n-Durán Rocha Marian\n-Fosado Martínez Dulce Olivia (responsable del Cuerpo Académico\n-Márquez Ortíz Juan Carlos",
    "¿quienes son los miembros academicos de arquitectura bioclimatica?","-Benavides Cortes María Mayela\n-Delgadillo López Paola Marisol\n-Salazar Texco Andrés",
    "¿cual es la linea de investigacion de la licenciatura en administracion y gestion empresarial?", "Fortalecimiento y consolidación de PyMES.",
    "¿cual es la linea de investigacion de arquitectura bioclimatica?","Diseño y edificación bioclimática\n-Sostenibilidad y territorio",
    "¿que son las PyMES?", "Pyme significa pequeña y mediana empresa. Lo que caracteriza a una empresa como pyme varía entre países y regiones, pero sus características distintivas son ciertos límites de capital humano y financieros. En algunos países las empresas se clasifican según las ventas anuales y su rubro, mientras que en otros la definición está ligada con el número de empleados. Una empresa es considerada pyme cuando tiene entre 1 y 250 empleados. Tradicionalmente, las pymes se clasifican según su tamaño en pequeñas, medianas y grandes. Con el tiempo se les han sumado las microempresas, que también se incluyen al referirse a las pymes, o de forma más precisa, mipymes. Todas ellas son organizaciones con fines de lucro y sus operaciones son de menor escala que las industrias.\n(Oyster 2022, 16 de Mayo)",
    #Implementacion Preguntas sobre Estudiantes en Base a la Informacion Recabada en la Pagina.
    #Reglamento de Estudiantes
    "Hablame sobre el reglamento de estudiantes", "Mira esta es una universidad seria por lo cual tiene que tener un reglamento.",
    "¿Donde se encuentra el reglamento de la escuela?","El reglamento de la escuela esta en la pagina oficial de la escuela en el apartado de estudiantes.",
    #infomacion de Becas
    "¿Como puedo saber sobre becas", "Puedes acudir al edificio UD1 con la Lic. Elisa Acuña. Ella podra ayudarte a atender tus dudas respecto a cualquier beca de forma presencial. Por otro lado, yo podria ayudarte tambien. Preguntame lo que quieras.",
    "¿Que becas de movilidad hay?","Solo hay una beca de movilidad esta dirigida a estudiantes de escasos recursos, que no cuenten con ningún otro apoyo en efectivo o en especie y que colaboren en un servicio administrativo u operativo dentro de la Universidad.","¿Por que no hay respuesta de jovenes escribiendo el futuro?","El encargados de la beca 'Jovenes Escribiendo El futuro' es gobierno del estado, no la universidad.",
    "¿Cuando son las fechas para las proximas becas?","Para la beca benito juarez podrar realizar el registro hasta el  de Diciembre del 2022,ingresa al sistema de citas. para mas informacion visita:",
    "¿Cual es el proceso de tramite para becas?","El proseso para cada beca es diferente, el la sigiente lista puedes leer el proseso para cada beca o puedes acercarte a el departamento de becas.",
    "¿Cuales son las becas con las que cuenta la escuela?","'Lista de becas'",
    "¿Puedo tener mas de una beca?","No, Solo puedes tener una beca a la vez",
    "¿Como saber si soy beneficiario a una beca?","Pudes corroborar tu alta en el apartado de 'Becas' en Metronet.",
    "¿Cuales son las fechas de los resultados de la beca?","Cada convocatoria tiene diferentes fechas, puedes consutalr esta informacion en http://www.upmh.edu.mx/.",
    "¿Que pasa si mi beca fue rechazada?","Lo sentimos mucho. Puedes intentarlo la proxima vez en las proximas fechas.",
    #Centro de Informacion
    "¿Que es el Centro de Informacion?","Es un apartado en la pagina oficial de la universidad en donde encontraras infomacion valiosa",
    "¿Cuales es la Mision del Centro de Informacion?","Ofrecer servicios de información actuales, eficientes y oportunos, así como proporcionar recursos y servicios documentales pertinentes, suficientes y de calidad para apoyar las actividades formativas y de actualización de la enseñanza, investigación y difusión de la cultura de las y los estudiantes, maestras/os y personal de apoyo a la docencia. Estos servicios se ofrecen prioritariamente a la comunidad UPMH, y extensivamente, al público en general, en el marco de los principios, los valores y los fines de ésta, conforme a las posibilidades y límites que le impone su naturaleza de biblioteca universitaria.",
    "¿Cuales es la Vision del Centro de Informacion?","Cubrir la demanda de información de las y los usuarios universitarios a partir de la atención a la bibliografía básica, directa e indirecta, de todas las carreras que se imparten en la Universidad, y la integración de una propuesta bibliográfica complementaria amplia, sólida, de calidad y actualidad, asimismo constituirse como una pieza fundamental de esta casa de estudios, a través de sus acervos bibliográficos y servicios. Generar un ambiente propicio para llevar a cabo el trabajo sustantivo de la Biblioteca, tanto en lo concerniente a la organización de sus recursos bibliográficos, como en la estructuración y atención profesional de los servicios que ofrece. Brindar servicios incluyentes adecuados y facilidades de acceso a la información a estudiantes con capacidades diferentes.",
    "¿Que podras encontrar en el Centro de Infomacion?","Podras encontrar infomacion acerca de los Servicios Bibliotecarios,Normatividad,Colecciones,Base de Datos de acceso libre,Catalogo en linea,Boletin de nuevas adquisiciones,bibliotecas digitales.",
    "¿Que son los servicios bibliotecarios?","Son los que el servicio de biblioteca presta son para ti como estudiante",
    "¿Cuales son esos servicios?","los servicios son: Consulta en Sala, Asesoria en la busqueda de bibliografia, Prestamo a domicilio, Servicio de documentacion,Consulta de material multimedia, Boletin de nuevas adquisicones, Ligas a bibliotecas especializadas, Prestamo de equipo de conmputo.",
    "¿Como puedo saber si hay nuevos libros en biblioteca","Muy buena pregunta usuario la informacion sobre nuevas adquisiciones se encuentra en el apartado de estudiantes, centro de informacion y nuevas adquisiciones.",
    "¿La escuela cuenta con biblioteca virtual?","No pero en el apartado de estudiantes, centro de informacion podras encontrar informacion muy valiosa."
    "¿La escuela cuenta con bases de datos para la consulta de informacion?","Claro que si se encuentra en la pagina en el apartado de estudiantes.",
    "Existen otras formas de consultar informacion","Claro que si existe un catalogo de consulta en linea el cual te ayudara a encontrar informacion valiiosa.",
    "¿Cual es el catalogo en linea?","Es una parte inmportante de la pagina",
    "¿Cual es el boletin de nuevas adquisiciones","Es el catalogo que representa cuales libros hay en existencia."
    "¿La escuela cuenta con biblioteca digital?","No, pero en el apartado de Centro de Informacion se encuentra el apartado biblioteca digital ahi estan las bilbiotecas digitales que tienen muy buena informacion.",
    #Buzon SQR
    "Buzon de sugerencias", "Sabias que en la universidad cuenta con un buzon de sugerencias y quejas.",
    "¿Donde esta el buzon SQR?", "El buzon SQR esta en la pagina oficial de la escuela en el apartado de estudiantes.",
    "Hola", "Hola! ¿Como puedo ayudarte?",
    #Bolsa de Trabajo
    "¿Existe una bolsa de trabajo para estudiantes?","Si, se encuentra en la parte de estudiantes ahi esta una lista que se actualiza para que puedas checarla cuando puedas.",
    #Calendario Escolar
    "¿En donde puedo encontrar el Calendario Escolar?","Se encuentra en el apartado de la pagina de la escuela en estudiantes ahi esta desglozado y se encuentra el Calendario Escolar.",
    #Internalizacion
    "¿Cual es el objetivo de internalizacion","Establecer mecanismos de cooperación con instituciones de educación superior nacionales e internacionales, con la finalidad de generar sinergias que permitan promover la movilidad académica de estudiantes, docentes y personal administrativo.",
    "¿Se necesita ser estudiante regular para poder aplicar a la internalizacion?","Claro que si es importante ser almnno regular.",
    "¿Se necesita tener un promedio para poder aplicar a la internalizacion?","Claro que si, se nesecita contar con un promedio general mínimo de 8.0",
    "¿Se necesita tener un pasaporte para poder aplicar a la internalizacion?","Si es importante contar con uno y que este vigente.",
    "¿Existen otras cosas mas que requiera el proceso?","Si, es un poco complicado explicarlo aqui pero en la pagina oficial de la escuela en el apartado de estudiantes puedes encontrar infomacion mas detallada sobre el proceso",
    #Proceso de Reiscripcion
    "Existe un apartado en donde este el preceso de reinscripcion","Claro se encuentra en la Pagina oficial en el Apartado de estudiantes.",
    #Manual de Metronet 
    "¿Que es Metronet?","Es un sistema interno excolar en el cual el estudiante puede checar sus calificaciones y otras cosas mas relacionadas a la trayectoria escolar.",
    "¿Donde se puede buscar mas informacion sobre metronet?","La puedes encontrar en la pagina oficial en el apartado de estudiantes.",
    #Titulacion 
    "¿cual es el proceso de titulacion?","Gracias por la pregunta, la informacion se encuentra en la pagina oficial en el apartado de estudiantes.",
    "¿cual es el costo de la titulacion?","El costo es de 1,667.11 pesos mas 7.00 pesos de la comision bancaria si nesecitas mas informacion cosulta el apartado de estudiantes que esta en la pagina oficial de la escuela.",
    "¿cual es el costo de la Cedula Profecional?","El costo es de 1,508.00 pesos si nesecitas mas informacion cosulta el apartado de estudiantes que esta en la pagina oficial de la escuela.",
    #Credencial Escolar 
    "¿que pasa si perdi mi credencial","No te preocupes en la pagina de la escuela en el apartado de estudiantes puedes encontrar la infomacion mas detallada y mas completa.",
    "¿tiene algun costo?","Si, el costo es de 73.76 pesos.",
    #Historal academico 
    "¿existe un apartado donde pueda encontrar mi historial academico?","Claro, se encuentra en el apartado de estudiantes en la pagina oficial de la escuela.",
    "¿tiene algun costo?","si, el costo es de 37.35 pesos.",
    #Consatancia de estudios
    "¿como puedo sacar una constancia de estudios?","La puedes tramitar en el apartado de estudiantes en la pagina oficial de la escuela.",
    "tiene algun costo","si, el costo es de 37.35 pesos.",
    "¿necesito mas informacion para este tramite?","Si necesitas mas informacion puedes encontrarla en la pagina ofical en el apartado de estudiantes.",
    #Equivalencia de estudios 
    "¿existe una forma en la que yo puedo sacar la equivalencia de estudios?","si lo puedes tramitar en el apartado de estudiantes en la pagina oficial de la escuela.",
    "¿tiene algun costo?","si, el costo es de 61.21 pesos.",
    "¿necesito mas informacion para este tramite?","Si necesitas mas informacion puedes encontrarla en la pagina ofical en el apartado de estudiantes.",
    #Certificado de estudios
    "¿existe una forma en la que yo puedo sacar un certificado de estudios?","si lo puedes tramitar en el apartado de estudiantes en la pagina oficial de la escuela.",
    "¿tiene algun costo?","si, el costo es de 122.41 pesos,cuando es un certificado parcial de estudios y si necesitas un duplicado de tu certificado son 245.86 pesos.",
    "¿necesito mas informacion para este tramite?","Si necesitas mas informacion puedes encontrarla en la pagina ofical en el apartado de estudiantes.",
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
        usermess = "hola"
        response = bot.get_response(usermess)


        # DATA --- (Dictionary)
        data = {
            'usermess': usermess,
            'response': response,

        }

        return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)