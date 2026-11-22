---
id: doc-validacao-dados
classe: documentacao
titulo: "Validação documental automatizada"
status: ativo
aliases: []
tags:
  - enciclopedia/documentacao
atualizado_em: 2026-11-22
---
# Validação documental automatizada

A pasta **schemas/** contém contratos JSON Schema 2020-12. O script **scripts/validar_catalogo.py** executa uma checagem estrutural inicial sem dependências externas. A automação em **.github/workflows/validacao-documental.yml** executa esse script em push e pull request.

~~~bash
python scripts/validar_catalogo.py
~~~

Cobertura inicial: parse JSON; IDs únicos; slugs; status; tipos; volume/família; 15 seções no exemplo; URLs de fontes e relações. O script não implementa integralmente a especificação JSON Schema e não verifica alegações históricas ou links externos. Ampliar cobertura é tarefa futura.


## Auditoria do vault Obsidian

```bash
python scripts/validar_obsidian.py
```

O validador confere IDs e notas do catálogo, 12 mapas de volume, metadados canônicos, referências relativas, embeds, Canvas e a presença de Bases. Também roda no workflow `.github/workflows/validacao-documental.yml`.

**O que não mede:** precisão histórica, integridade acadêmica de fontes, qualidade visual do aplicativo ou renderização de Base por versão incompatível do Obsidian. Esses pontos exigem revisão específica.

[Início do vault Obsidian](../INICIO.md)
