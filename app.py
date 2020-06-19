from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from covid import Covid
covid = Covid()
app = Flask(__name__)

steam_bot = ChatBot("Forsage",
                    storage_adapter="chatterbot.storage.SQLStorageAdapter",
                    logic_adapters = [
                        "chatterbot.logic.MathematicalEvaluation",
                        #"chatterbot.logic.TimeLogicAdapter",
                        "chatterbot.logic.BestMatch"
                        ]
                    )
with open('tr-data.txt') as tr:
    tr = tr.read().strip().split('\n')
    traine = ListTrainer(steam_bot)
    traine.train(tr)
    traine.train(["Covid ", "Nigeria:"+str(covid.get_status_by_country_name("Nigeria"))[15:]])
#trainer.train(['who are you?', 'I\'m  a BOT'])

trainer = ChatterBotCorpusTrainer(steam_bot)
trainer.train("chatterbot.corpus.english")#,
              #"chatterbot.corpus.english.conversations")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(steam_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
