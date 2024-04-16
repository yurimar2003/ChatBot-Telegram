from email import message
import os
import sys
import logging
from turtle import update
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()

TOKEN = ("5765922288:AAHrMCaAhzqthTx2jcdNUfEy4YjCaIqIq0w")




def start(update, context):
    bot = context.bot
    userName = update.effective_user["first_name"]
    update.message.reply_text(f'¡Hola un gusto! {userName}. Soy un bot creado para interactuar contigo y enseñarte sobre el estupendo mundo de la inteligencia artificial. Comencemos, ya sabes ¿que es la inteligencia artificial?. Porfavor respondeme con un simple "Si" o "No".'
    )
    update.message.reply_text(f'Ten presente que, si deseas despedirte introduce o dale clic al comando /adios para dejar esta conversacion'
    )

def adios(update, context):
    bot = context.bot
    userName = update.effective_user["first_name"]
    update.message.reply_text(f'Me despido {userName}. Fue un gusto enseñarte sobre este nuevo mundo de la tecnologia. Aqui te dejo un link de noticias actuales de la AI https://www.xataka.com/tag/inteligencia-artificial'
    )
    update.message.reply_text(f'Hasta luego Jeje... ¡Espero verte pronto!'
    )


def one(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f'el usuario {userName} ha solicitado informacion sobre category one')
    bot.sendMessage(
        chat_id=chatId,
        parse_mode="HTML",
        text=f"El aprendizaje automático es uno de los tipos de inteligencia artificial al que más acostumbrados estamos, sobre todo a nivel de series o películas. Se basa en la capacidad que un software o dispositivo tiene de aprender por su cuenta. El aprendizaje automático sigue tres pasos fundamentales, como cualquier otro método: aprendizaje, entrenamiento y resultados."
        )
    bot.sendMessage(
        chat_id=chatId,
        parse_mode="HTML",
        text=f"Interesante... Puedes introducir o dale clic a el comando /video1 para ver un video relacionado al aprendizaje automático o tambien puedes introducir una nueva categoria que desees conocer (no olvides que debes introducir el comando). ¡Anímate es bueno aprender cosas nuevas!"
        )
    bot.sendMessage(
        chat_id=chatId,
        text=f'Si deseas despedirte introduce o dale clic al comando /adios para dejar esta conversacion'
        )


def two(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f'el usuario {userName} ha solicitado informacion sobre category one')
    bot.sendMessage(
        chat_id=chatId,
        parse_mode="HTML",
        text=f"El aprendizaje profundo es un tipo de aprendizaje que va más allá del automático, ya que engloba y procesa más datos e información al mismo tiempo. Utiliza otro de los tipos de inteligencia artificial, las redes neuronales, para desenvolverse entre un mayor volumen de información. Está estrechamente ligado con otros de los términos del momento, el Big Data."
        )
    bot.sendMessage(
        chat_id=chatId,
        parse_mode="HTML",
        text=f"Interesante... Puedes introducir o dale clic a el comando /video2 para ver un video relacionado al aprendizaje automático o tambien puedes introducir una nueva categoria que desees conocer (no olvides que debes introducir el comando). ¡Anímate es bueno aprender cosas nuevas!"
        )
    bot.sendMessage(
        chat_id=chatId,
        text=f'Si deseas despedirte introduce o dale clic al comando /adios para dejar esta conversacion'
        )


def three(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f'el usuario {userName} ha solicitado informacion sobre category one')
    bot.sendMessage(
        chat_id=chatId,
        parse_mode="HTML",
        text=f"Las redes neuronales, como su propio nombre indica, es un tipo de IA que intenta imitar el comportamiento de las neuronas. A partir de una red de neuronas artificiales, se crea un sistema por el que reciben y procesan datos. Las Redes Neuronales Artificiales (RNA) están formadas por millones de neuronas artificiales trabajando de manera coordinada, con capacidad de operar con acciones de aprendizaje."
        )
    bot.sendMessage(
        chat_id=chatId,
        parse_mode="HTML",
        text=f"Interesante... Puedes introducir o dale clic a el comando /video3 para ver un video relacionado al aprendizaje automático o tambien puedes introducir una nueva categoria que desees conocer (no olvides que debes introducir el comando). ¡Anímate es bueno aprender cosas nuevas!"
        )
    bot.sendMessage(
        chat_id=chatId,
        text=f'Si deseas despedirte introduce o dale clic al comando /adios para dejar esta conversacion'
        )


def four(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f'el usuario {userName} ha solicitado informacion sobre category one')
    bot.sendMessage(
        chat_id=chatId,
        parse_mode="HTML",
        text=f"El sistema experto funciona a partir de una lógica racional que intenta imitar a un humano con dominio de una materia concreta.Este tipo de IA la podemos encontrar, por ejemplo, en los chats automáticos que muchos servicios de atención al cliente ya tienen implantados. Se usan en muchos ámbitos destinados al cliente."
        )
    bot.sendMessage(
        chat_id=chatId,
        parse_mode="HTML",
        text=f"Interesante... Puedes introducir o dale clic a el comando /video4 para ver un video relacionado al aprendizaje automático o tambien puedes introducir una nueva categoria que desees conocer (no olvides que debes introducir el comando). ¡Anímate es bueno aprender cosas nuevas!"
        )
    bot.sendMessage(
        chat_id=chatId,
        text=f'Si deseas despedirte introduce o dale clic al comando /adios para dejar esta conversacion'
        )



def echo(update, context):
    bot = context.bot
    updateMsg = getattr(update, 'message', None)
    messageId = updateMsg.message_id
    chatId = update.message.chat_id
    userName = update.effective_user['first_name']
    text = update.message.text
    logger.info(f'el usuario a enviado un nuevo mensaje para entrar al si/no, categorias')

    if 'Si' in text:
        bot.sendMessage(
            chat_id=chatId,
            text=f'Perfecto {userName}, recordemos que...La inteligencia artificial (IA) hace posible que las máquinas aprendan de la experiencia, se ajusten a nuevas aportaciones y realicen tareas como seres humanos. La mayoría de los ejemplos de inteligencia artificial sobre los que oye hablar hoy día – desde computadoras que juegan ajedrez hasta automóviles de conducción autónoma – recurren mayormente al aprendizaje profundo y al procesamiento del lenguaje natural. Empleando estas tecnologías, las computadoras pueden ser entrenadas para realizar tareas específicas procesando grandes cantidades de datos y reconociendo patrones en los datos.'
        )
        bot.sendMessage(
            chat_id=chatId,
            text=f'¡Estupendo! ¿no crees?...Utiliza el comando /mas para seguir conociendo sobre este tema'
        )
        bot.sendMessage(
            chat_id=chatId,
            text=f'Si deseas despedirte introduce o dale clic al comando /adios para dejar esta conversacion'
        )
    elif 'No' in text:
        bot.sendMessage(
            chat_id=chatId,
            text=f'No te preocupes {userName}, Aqui te lo explicamos de la manera mas sencilla...En términos simples, inteligencia artificial (IA) se refiere a sistemas o máquinas que imitan la inteligencia humana para realizar tareas y pueden mejorar iterativamente a partir de la información que recopilan.',      
        )
        bot.sendMessage(
            chat_id=chatId,
            text=f'¡Estupendo! ¿no crees?...Utiliza el comando /mas para seguir conociendo sobre este tema'
        )
        bot.sendMessage(
            chat_id=chatId,
            text=f'Si deseas despedirte introduce o dale clic al comando /adios para dejar esta conversacion'
        )   
    else:
        bot.sendMessage(
        chat_id=chatId,
        text=f'El mensaje que introduciste no es válido, por favor intenta nuevamente'
        )

def video1 (update, context):
    bot = context.bot
    userName = update.effective_user["first_name"]
    update.message.reply_text(f'Que bueno que te decidiste a verlo {userName}, aqui te lo dejamos...Presta mucha atención, te ayudará a entender mas a fondo el concepto https://www.youtube.com/watch?v=NdNyYcAJQr8'
    )
    update.message.reply_text(f'Si deseas despedirte introduce o dale clic al comando /adios para dejar esta conversacion'
    )

def video2 (update, context):
    bot = context.bot
    userName = update.effective_user["first_name"]
    update.message.reply_text(f'Que bueno que te decidiste a verlo {userName}, aqui te lo dejamos...Presta mucha atención, te ayudará a entender mas a fondo el concepto https://www.youtube.com/watch?v=3h55dfFv83Y&t=20s'
    )
    update.message.reply_text(f'Si deseas despedirte introduce o dale clic al comando /adios para dejar esta conversacion'
    )

def video3 (update, context):
    bot = context.bot
    userName = update.effective_user["first_name"]
    update.message.reply_text(f'Que bueno que te decidiste a verlo {userName}, aqui te lo dejamos...Presta mucha atención, te ayudará a entender mas a fondo el concepto https://www.youtube.com/watch?v=CU24iC3grq8'
    )
    update.message.reply_text(f'Si deseas despedirte introduce o dale clic al comando /adios para dejar esta conversacion'
    )

def video4 (update, context):
    bot = context.bot
    userName = update.effective_user["first_name"]
    update.message.reply_text(f'Que bueno que te decidiste a verlo {userName}, aqui te lo dejamos...Presta mucha atención, te ayudará a entender mas a fondo el concepto https://www.youtube.com/watch?v=DGBDaL9okkA'
    )
    update.message.reply_text(f'Si deseas despedirte introduce o dale clic al comando /adios para dejar esta conversacion'
    )

def getBotInfo(update, context):
    bot = context.bot
    chatId = update.message.chat_id
    userName = update.effective_user["first_name"]
    logger.info(f'el usuario {userName} ha solicitado informacion sobre el bot, entro al comando /mas')
    bot.sendMessage(
        chat_id=chatId,
        parse_mode="HTML",
        text=f"La inteligencia artificial es un mundo en constante evolución que cada año nos sorprende con impactantes novedades. <b>Actualmente, los tipos de inteligencia artificial se suelen aglutinar en 4 categorías.</b>    1)Aprendizaje automático   2)Aprendizaje profundo    3)Redes neuronales  4)Sistema experto"
        )
    bot.sendMessage(
        chat_id=chatId,
        parse_mode="HTML",
        text=f"Introduzca o dale clic a el comando '/1' para seleccionar aprendizaje automático   '/2' para seleccionar aprendizaje profundo   '/3' para seleccionar redes neuronales  '/4' para seleccionar sistema"
        )
    bot.sendMessage(
        chat_id=chatId,
        text=f'Si deseas despedirte introduce o dale clic al comando /adios para dejar esta conversacion'
        )






if __name__ == "__main__":
    #Obtenemos la info del bot
    myBot = telegram.Bot(token = TOKEN)

#updater es el que conecta y recibe los mensajes
updater = Updater(myBot.token,use_context=True)

#creamos el dispatcher
dp = updater.dispatcher

#creamos un manejador, seria un comando
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("adios", adios))
dp.add_handler(CommandHandler("video1", video1))
dp.add_handler(CommandHandler("video2", video2))
dp.add_handler(CommandHandler("video3", video3))
dp.add_handler(CommandHandler("video4", video4))
dp.add_handler(CommandHandler("mas", getBotInfo))
dp.add_handler(CommandHandler("1", one))
dp.add_handler(CommandHandler("2", two))
dp.add_handler(CommandHandler("3", three))
dp.add_handler(CommandHandler("4", four))
dp.add_handler(MessageHandler(Filters.text, echo))




updater.start_polling()
print("CORRIENDO BOT")
updater.idle() #terminar bot con control+c