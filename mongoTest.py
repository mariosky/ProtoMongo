__author__ = 'mariosky'


import pymongo
from pymongo import MongoClient
client = MongoClient()



POO =  {
    "uri" : "/activity/PB", "name" : "Python Básico", "slug" : "PB", "heading" : "Python Básico", "secondary_text" : "Tutorial",
    "description" : "Tutorial del lenguaje Python, orientado a principiantes.", "image" : "https://s3.amazonaws.com/learning-python/python-logo.png",
    "choice_exit" : False, "rollup_rule"  : "satisfied IF All satisfied", "rollup_objective" : True, "rollup_progress" : True,
    "is_container" : True, "is_visible" : True,
    "children":[
                {   "uri" : '/test/poo', "name" : "Experiencia Programando",
                    "slug" : 'Pretest', "parent" :"/activity/PB",
                    "root"  : "/activity/PB", "heading":"¿Que tanto sabes POO?",
                    "description" : "Antes de empezar, dinos algo sobre tu experiencia en programación orientada a objetos.",
                    "image" : "https://s3.amazonaws.com/learning-python/survey.jpg", "choice_exit" : False,
                    "pre_condition_rule" : """
                if self.objective_status == 'notSatisfied' :
                    self.pre_condition = 'stopForwardTraversal'
                else:
                    self.pre_condition = 'hidden'
                """,
                    "rollup_objective" : True,
                    "rollup_progress" : True,

                    "is_container" : False,
                    "is_visible" : True
                },

                {
                "name" : 'Introduccion', "slug" : 'Intro',
                "uri" : "/activity/introduccion",
                "heading":"Introducción al lenguaje",
                "description" : "Vemos las principales características del lenguaje y hacemos los primeros ejercicios.",
                "image" : "https://s3.amazonaws.com/learning-python/python-logo.png",
                "secondary_text" : "Lección", "choice" : True, "choice_exit" : False, "rollup_rule"  : "satisfied IF All satisfied",
                 "rollup_objective" : True, "rollup_progress" : True,

                "is_container" : True,
                "is_visible" : True,
                "order_in_container" : 1
                }
    ]

}









secuencias = LearningActivity( name = 'Secuencias', slug = 'Intro',
    uri = "/activity/secuencias",
#   lom =
    image = "https://s3.amazonaws.com/learning-python/sequence.jpg",
    heading="Objetos Tipo Secuencia",
    description = "Aprenderás a utilizar las Listas, Tuplas y Cadenas",
    secondary_text = "Lección",

    parent = PPP, root  = PPP,

#    pre_condition_rule = """self.recommendation_value = Text_Verbal.eval(self.user.learningstyleinventory.verbal,self.user.learningstyleinventory.visual)"""  ,
    pre_condition_rule = """
if self.get_ula_attr('Introduccion','objective_status') == 'satisfied':
    self.pre_condition = ''
else:
    self.pre_condition = 'disabled'
""",
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = True,
    choice_exit = False,


    rollup_rule  = "satisfied IF All satisfied",
    rollup_objective = True,
    rollup_progress = True,

    is_container = True,
    is_visible = True,
    order_in_container = 2
    )
secuencias.save()


tema_1 = LearningActivity( name = 'Introduccion', slug = 'Intro',
    uri = '/activity/video/intro',

    heading="Introducción al Lenguaje Python",
    description = "Aprenderás cuales son las caracteristicas del lenguaje.",
    image = "https://s3.amazonaws.com/learning-python/IntroVideo.png",

    parent = intro, root  = PPP,
    pre_condition_rule = "",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 0
    )
tema_1.save()

tema_2 = LearningActivity( name = 'Ejercicios Basados en Pruebas', slug = 'Ejercicios',
    uri = '/activity/video/ejercicios_basados_en_pruebas',

    heading="Ejercicios Basados en Pruebas",
    description = "Explicamos la técnica básica de pruebas unitarias y su uso para especificar ejercicios de programación",
    image = "https://s3.amazonaws.com/learning-python/pruebas.png",


    parent = intro, root  = PPP,
    pre_condition_rule = "",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 1
    )
tema_2.save()

tema_3 = LearningActivity( name = 'Como hacer los ejercicios', slug = 'Ejemplo',
    uri = '/activity/video/ejemplo_ejercicio',

    heading="Haciendo un Ejercicio",
    description = "Aprendemos la manera de programar los ejercicios en Protoboard",
    image = "https://s3.amazonaws.com/learning-python/ejercicioVideo.png",


    parent = intro, root  = PPP,
    pre_condition_rule = "",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 2
    )
tema_3.save()


EjerciciosIntro = LearningActivity( name = 'Ejercicios', slug = 'Ejercicios',
    uri = "/activity/EjerciciosIntro",
    parent = intro,
    root   = PPP,

    heading="Ejercicios Básicos",
    description = "Algunos ejercicios para calentar morores",
    secondary_text = "Ejercicios",
    image = "https://s3.amazonaws.com/learning-python/cafe.png",



    flow = True,
    forward_only = False,
    choice = True,
    choice_exit = False,

    rollup_rule  = "satisfied IF All satisfied",
    rollup_objective = True,
    rollup_progress = True,

    is_container = True,
    is_visible = True,
    order_in_container = 3
    )
EjerciciosIntro.save()

program_1 = LearningActivity( name = 'Imprime Hola', slug = 'E1',
    uri = "/program/PPP/1",

    heading="Imprime Hola",
    description = "La versión básica del clásico Hola Mundo",
    image = "https://s3.amazonaws.com/learning-python/images.png",



    parent = EjerciciosIntro, root  = PPP,
    pre_condition_rule = "",
    post_condition_rule = "",

    choice_exit = False,
    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 3
    )
program_1.save()


program_2 = LearningActivity( name = '¿Es par?', slug = 'E2',
    uri = "/program/PPP/2",
    parent = EjerciciosIntro, root  = PPP,
    pre_condition_rule = """
if self.get_ula_attr('Imprime Hola','objective_status') == 'satisfied':
    self.pre_condition = ''
else:
    self.pre_condition = 'disabled'
""",
    description = "Haz una función que te diga si es un número par. Necesario completar: Imprime Hola ",
    post_condition_rule = "",
    choice_exit = False,
    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 5
    )
program_2.save()

program_3 = LearningActivity( name = 'Suma dos números', slug = 'E3',
    uri = "/program/PPP/3",

    heading="Uno + Uno",
    description = "Escribe una función que sume dos números",
    image = "https://s3.amazonaws.com/learning-python/suma.png",


    parent = EjerciciosIntro, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    choice_exit = False,

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 7
    )
program_3.save()


program_4 = LearningActivity( name = 'distancia()', slug = 'E4',
    uri = "/program/PPP/4",
    parent = EjerciciosIntro, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 9
    )
program_4.save()


program_5 = LearningActivity( name = 'mayor()', slug = 'E5',
    uri = "/program/PPP/5",
    parent = EjerciciosIntro, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 11
    )
program_5.save()

secuencias_1 = LearningActivity( name = 'Video', slug = 'Intro',
    uri = '/activity/video/secuencias',
    parent = secuencias, root  = PPP,
    pre_condition_rule = "",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,
    order_in_container = 0
    )
secuencias_1.save()

EjerciciosSec = LearningActivity( name = 'Ejercicios', slug = 'Ejercicios',
    uri = "/activity/EjerciciosSec",
    parent = secuencias,
    root   = PPP,

    flow = True,
    forward_only = False,
    choice = True,
    choice_exit = False,

    rollup_rule  = "satisfied IF All satisfied",
    rollup_objective = True,
    rollup_progress = True,

    is_container = True,
    is_visible = True,
    order_in_container = 3
    )
EjerciciosSec.save()


program_6 = LearningActivity( name = 'Dame una lista', slug = 'E6',
    uri = "/program/PPP/6",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 8
    )
program_6.save()


program_7 = LearningActivity( name = 'Dame una tupla', slug = 'E7',
    uri = "/program/PPP/7",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 10
    )
program_7.save()

program_8 = LearningActivity( name = 'Solo una tajada', slug = 'E8',
    uri = "/program/PPP/8",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 12
    )

program_8.save()

program_9 = LearningActivity( name = 'Solo una tajadita', slug = 'E9',
    uri = "/program/PPP/9",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 14
    )
program_9.save()

program_10 = LearningActivity( name = '¡Pura Acción!', slug = 'E10',
    uri = "/program/PPP/10",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 16
    )
program_10.save()

program_11 = LearningActivity( name = 'Mutantes', slug = 'E10',
    uri = "/program/PPP/11",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 18
    )
program_11.save()

program_12 = LearningActivity( name = 'Ordena la Lista', slug = 'E10',
    uri = "/program/PPP/12",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 20
    )
program_12.save()


program_13 = LearningActivity( name ='Producto punto' , slug = 'E10',
    uri = "/program/PPP/13",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 22
    )
program_13.save()
