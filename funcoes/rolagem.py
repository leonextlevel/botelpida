from random import randint


# Imprimir Resultado
# Recebe uma lista de com os valores de rolagens e opcionalmente uma com rolagens extras.
# Retrona uma string formatada com os resultados dessas rolagens.
def imprime_resultado(rolagens, dados, extras=[]):
    sucessos = sum(map(lambda x: x > 5, rolagens + extras))
    falhas = sum(map(lambda x: x <= 5, rolagens + extras))
    saida = ''
    if extras:
        return f'''**ROLANDO {dados}D10**
**Resultados:** {rolagens}
**Extras:** {extras}

:white_check_mark:  Sucessos: {sucessos}    :no_entry:  Falhas: {falhas}'''

    return f'''**ROLANDO {dados}D10**
Resultados: {rolagens}

:white_check_mark:  Sucessos: {sucessos}    :no_entry:  Falhas: {falhas}'''


# Criar Rolagem
# Recebe um número inteiro positivo <= 100
# Retrona uma string com uma mensagem informando o sucesso da rolagem
def criar_roll(message):
    dados = int(message.content.lower().split()[1])
    if dados > 0 and dados <= 15:
        rolagens = []
        extras = []
        ver_ultima_rolagem = True
        for k in range(dados):
            if rolagens:
                while rolagens[-1] == 10 and ver_ultima_rolagem:
                    extras.append(randint(1, 10))
                    ver_ultima_rolagem = False
            if extras:
                while extras[-1] == 10:
                    extras.append(randint(1, 10))
            rolagens.append(randint(1, 10))
            ver_ultima_rolagem = True
        if rolagens:
            while rolagens[-1] == 10 and ver_ultima_rolagem:
                extras.append(randint(1, 10))
                ver_ultima_rolagem = False
        if extras:
            while extras[-1] == 10:
                extras.append(randint(1, 10))
        if extras:
            return imprime_resultado(rolagens, extras=extras, dados=dados)
        return imprime_resultado(rolagens, dados=dados)
    return (
        ":robot: BOT\n\n"
        ":speech_balloon: Valor fora dos meus limites! Tente com valores de 1 a 15 :wink:"
    )
