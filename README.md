# py_test
Criando um módulo em python a partir de um teste<br>

<b>Comando da questão</b><br>
Resolva o desafio a seguir:

arquivo test_google_driver.py<br>
-----
from google_driver import GoogleDriver<br>
<br>
def test_requests():<br>
result = GoogleDriver().search("test")<br>
assert 200 == result.status_code<br>
assert "test" in str(result.content)<br>

Escreva o código necessário para que o teste funcione.<br>
** Já estamos utilizando pytest, portanto será necessário realizar pip install pytest
executar pytest na linha de comando (raíz do projeto) para visualizar os resultados<br>

1º passo: instalar o pytest:<br>
https://docs.pytest.org/en/latest/getting-started.html<br>
2º passo: entrar no terminal e digitar o comando pytest nome_do_arquivo
