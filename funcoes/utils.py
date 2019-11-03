def ajuda(user):
    return (
        ":robot: BOT\n\n"
        f":speech_balloon: Olá, **{user}**!\n"
        "Não se desespere, logo alguém vai te ajudar!\n"
        "Por hora, por quê não experimenta umas das minhas funcionalidades básicas?\n"
        "Para isso utilize o comando **/comandos** e veja uma lista deles :grin:"
    )


def comandos():
    return (
        ":robot: BOT\n\n"
        "**Os comandos disponíveis são:**\n"

        "**/help** - *mensagem de ajuda para quem está mais perdido.*\n\n"

        "**/roll <numero de dados>** - *rola uma quantidade de d10 igual ao número informado, "
        "retornando também a quantidade de sucessos e falhas adquiridas.*\n\n"

        "*(comando <argumentos> - função)*\n\n"
    )
