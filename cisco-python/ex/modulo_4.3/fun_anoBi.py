def anoBi(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Dados de teste e resultados esperados
testes = [1600, 2000, 2020, 2021, 1900, 1800]
resultados_esperados = [True, True, True, False, False, False]

# Loop de teste
for i in range(len(testes)):
    ano = testes[i]
    comparacao = resultados_esperados[i]
    resultado = anoBi(ano)
    assert resultado == comparacao, f"Erro: ano {ano}, esperado {comparacao}, mas obteve {resultado}"
    print(f"O ano {ano} é bissexto? {resultado}. Teste verdadeiro.")
