# pip install plyer
# version python 3.11.4

from plyer import notification
from time import sleep



class Pomodoro():
    def __init__(self, tempo, descricao, tempo2) -> None:
        self.tempo = int(tempo)
        self.descricao = str(descricao)
        self.tempo2 = str(tempo2)

    # defindo a mensagem de alerta para inicializacao do Pomodoro
    def notificacao_pomodoro(self):
        notification.notify(
            title = 'Iniciando o Pomodoro',
            message = self.descricao,

            # display time
            timeout=5
        )

        # waiting time
        sleep(1)

    def executando_pomodoro(self):
        sleep(self.tempo)


    def fim_pomodoro(self):
        notification.notify(
            title = 'Tempo Progamado Finalizado',
            message = f'seu objetivo: "{self.descricao}", com: {self.tempo} {self.tempo2} foi concluido!!',

            # displey time
            timeout=5
        )
        sleep(1)


if __name__=="__main__":
    print("============ INICIANDO O POMODORO ============")
    sleep(5)
    descricao = str(input("\nQual o seu objetivo para iniciar o POMODORO: "))
    sleep(2)
    tempo = int(input("\nQuanto tempo deseja fazer programar o POMODORO? (número) : "))
    sleep(2)

    print("\nEsse tempo estabelecido é minutos ou segundos? ")
    sleep(1)
    verifica = int(input("\nDigite 1 para [SEGUNDOS] ou 2 para [MINUTOS]: "))

    # verifica se é minutos ou segundos
    if verifica == 2:
        tempo = tempo * 60
        tipo_tempo = 'Minutos'
    else:
        tempo
        tipo_tempo = 'Segundos'


    # iniciando a classe
    pomodoro = Pomodoro(tempo, descricao, tipo_tempo)
    notificacao = pomodoro.notificacao_pomodoro()
    tempo =  pomodoro.executando_pomodoro()
    fim_pomodoro = pomodoro.fim_pomodoro()

