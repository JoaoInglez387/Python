from veiculo import Veiculo

ka_1 = Veiculo('Branco', 'Ka', 2020, 'Ford')
print('Modelo:', ka_1.modelo, ka_1.velocidade)
print()

ka_1.alterar_velocidade(60)
print('Modelo:', ka_1.modelo, ka_1.velocidade)

ka_1.buzinar(1)
ka_1.buzinar(2)
ka_1.buzinar(5)