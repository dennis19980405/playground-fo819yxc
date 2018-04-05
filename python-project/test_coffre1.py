import builtins

anc_print = builtins.print


def send_msg(channel, msg):
    anc_print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    anc_print("TECHIO> success true")


def fail():
    anc_print("TECHIO> success false")


def nouv_print(chaine):
    if isinstance(chaine, int) and chaine >= 100 and chaine <= 999:
        success()
        send_msg("Bien joué!", "Avancez à l'étape suivante")
    else:
        fail()
        send_msg("Ce n'est pas exactement cela.",
                 "Remarquez les nombres entre parenthèses, ce sont les limites des possibilités de la combinaison.")
    anc_print(chaine)


builtins.print = nouv_print
import coffre1
