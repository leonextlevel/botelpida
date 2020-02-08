from random import randint


class Roll:
    num_lados = 10
    explosao = True

    def __init__(self, num_dados):
        self.num_dados = num_dados
        self.resultados = []
        self.resultados_extra = []

    def valida_num_dados(self):
        '''
            Valida se a quantidade de dados rolados está dentro do limite e
            se é um valor válido.
        '''
        if isinstance(self.num_dados, int):
            if self.num_dados > 0 and self.num_dados <= 15:
                return True
        return False

    def checar_dado(self, valor_dado):
        '''
            Caso explosão esteja ativa, verifica se o valor do dado é
            igual ao valor máximo possível, se for, rola um dado extra
            e aplica o mesmo tratamento para esse dado extra.
        '''
        if self.explosao:
            if valor_dado == self.num_lados:
                rolagem_extra = randint(1, self.num_lados)
                self.resultados_extra.append(rolagem_extra)
                self.checar_dado(rolagem_extra)
        return

    def rolagem(self):
        '''
            "Rola" uma quantidade de dados igual ao atributo num_dados,
            armazena cada resultado no atributo resultados
        '''
        if self.valida_num_dados():
            for dado in range(self.num_dados):
                valor_dado = randint(1, self.num_lados)
                self.resultados.append(valor_dado)
                self.checar_dado(valor_dado)

    def get_resultados(self):
        '''
            Retorna mensagem com resultados das rolagens
        '''
        self.rolagem()
        todos_resultados = self.resultados + self.resultados_extra
        sucessos = sum(map(lambda x: x > 5, todos_resultados))
        falhas = sum(map(lambda x: x <= 5, todos_resultados))
        if self.resultados_extra:
            return (
                f"ROLANDO {self.num_dados}D{self.num_lados}\n"
                f"RESULTADOS {self.resultados}\n"
                f"EXTRAS {self.resultados_extra}\n"
                f"SUCESSOS {sucessos}\n"
                f"FALHAS {falhas}\n"
            )
        return (
            f"ROLANDO {self.num_dados}D{self.num_lados}\n"
            f"RESULTADOS {self.resultados}\n"
            f"SUCESSOS {sucessos}\n"
            f"FALHAS {falhas}\n"
        )


if __name__ == "__main__":
    rolagem_teste = Roll(10)
    print(rolagem_teste.get_resultados())
