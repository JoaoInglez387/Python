class cliente:
    def __init__(self,nome,cnpj_cpf,nome_fantasia, verificacao = 'Não tem'):
        self.nome = nome
        self.cnpj_cpf = cnpj_cpf
        self.nome_fantasia = nome_fantasia
        self.verificacao = verificacao