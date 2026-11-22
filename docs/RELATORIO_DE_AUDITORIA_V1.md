---
id: doc-relatorio-de-auditoria-v1
classe: documentacao
titulo: "Auditoria da documentação fundacional — 2026-11-22"
status: ativo
aliases: []
tags:
  - enciclopedia/documentacao
atualizado_em: 2026-11-22
---
# Auditoria da documentação fundacional — 2026-11-22

## Escopo verificado
- Repositório GitHub público balancerec/enciclopedia-politica, branch main.
- 12 sumários de volumes e índices com ligações internas.
- 168 IDs únicos no catálogo e 188 menções entre volumes.
- 20 conceitos aparecem em mais de um índice e usam mesmo ID canônico.
- 12 verbetes introdutórios separados, identificados como rascunho.
- 15 dimensões no modelo de verbete.
- Schemas para catálogo e verbete, script de verificação e workflow GitHub Actions.

## Verificação técnica
- O GitHub Actions concluiu com **sucesso** a checagem estrutural do commit `f4a5319d9548eda02a170536f5e9640c3c4351fb`.
- Registro: https://github.com/balancerec/enciclopedia-politica/actions/runs/45026470494
- Um CI bem-sucedido atesta apenas as regras estruturais executadas, **não** a correção histórica das descrições.

## Escopo dos dados
- O catálogo é intencionalmente inicial, não exaustivo.
- Uma fila adicional de 153 termos está em catalogo/TERMOS_CANDIDATOS.md, sujeita a validação editorial.
- Para corrigir remissivas, as famílias adicionais dos 20 conceitos transversais foram reconciliadas com os índices de volumes.

## Pendências importantes
1. Escolher licenças para texto, código e imagens.
2. Pesquisar fontes primárias e bibliografia especializada por verbete.
3. Revisar historicamente os 12 rascunhos e expandir as 168 entradas.
4. Decidir stack e implementar website, busca e comparador.
5. Implantar testes formais de JSON Schema, links externos e acessibilidade.

## Estado da entrega
**Fundação documental publicada. Enciclopédia acadêmica e plataforma web ainda em desenvolvimento.**

[Início do vault Obsidian](../INICIO.md)
