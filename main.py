import telebot
import textos as tx

with open("chave.txt", "r") as file:
    CHAVE =  file.readline()

bot = telebot.TeleBot(CHAVE)


def MessageOut():
    return "Foi um prazer te atender, até mais"

@bot.message_handler(commands=["1"])
def opcao1(mensagem):
    texto = tx.pedidoPizza
    bot.reply_to(mensagem, texto)


def verificarSabor(mensagem):
    with open("sabores.txt", "r") as opcoes:
        sabores = opcoes.readlines()
        for sabor in sabores:
            if sabor == mensagem:
                return True
            else:
                return "Não temos esse sabor disponivel"



@bot.message_handler(commands=["op1"])
def pizzaUmSabor(mensagem):
    bot.send_message(mensagem.chat.id, "Qual o sabor da pizza?")
    with open("menu.txt", "r") as file:
        sabores = file.readlines()
        for sabor in sabores:
            bot.send_message(mensagem.chat.id, sabor)
   

@bot.message_handler(commands=["2"])
def opcao2(mensagem):
    email = tx.email
    bot.reply_to(mensagem, tx.textoEmail.format(email))
    texto=  tx.continuarAtendimento
    bot.send_message(mensagem.chat.id,texto)
    
@bot.message_handler(commands=["Nao"])
def optionOut(mensagem):
    bot.send_message(mensagem.chat.id , MessageOut())
    

    
@bot.message_handler(commands=["3"])
def opcao3(mensagem):
    texto = tx.atendimentoHumano
    bot.send_message(mensagem.chat.id , texto)
    bot.send_message(forward_from_chat = 1528956255)
#   mensagem.chat.id ==1528956255

@bot.message_handler(commands=["4"])
def opcao4(mensagem):
    bot.send_message(mensagem.chat.id , MessageOut())
    


def verificarMensagem(mensagem):
    return True

@bot.message_handler(func=verificarMensagem)
def inicioDeConversa(mensagem):
    # print(mensagem)
    
    texto = tx.bemVindo
    bot.reply_to(mensagem, texto)



bot.polling()


