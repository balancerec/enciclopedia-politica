# Validação documental automatizada

A pasta **schemas/** contém contratos JSON Schema 2020-12. O script **scripts/validar_catalogo.py** executa uma checagem estrutural inicial sem dependências externas. A automação em **.github/workflows/validacao-documental.yml** executa esse script em push e pull request.

~~~bash
python scripts/validar_catalogo.py
~~~

Cobertura inicial: parse JSON; IDs únicos; slugs; status; tipos; volume/família; 15 seções no exemplo; URLs de fontes e relações. O script não implementa integralmente a especificação JSON Schema e não verifica alegações históricas ou links externos. Ampliar cobertura é tarefa futura.
