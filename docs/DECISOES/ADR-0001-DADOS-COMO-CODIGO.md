---
id: doc-decisoes-adr-0001-dados-como-codigo
classe: decisao
titulo: "ADR-0001 — Conteúdo e metadados versionados em Git"
status: aceito
aliases: []
tags:
  - enciclopedia/documentacao
atualizado_em: 2026-11-22
---
# ADR-0001 — Conteúdo e metadados versionados em Git

- Estado: aceito para a fundação documental.
- Data: 2026-11-22.

## Contexto
Um acervo político precisa de rastreabilidade, correções, remissivas e revisão de cada alteração.

## Decisão
Manter textos Markdown e dados JSON estruturados em repositório Git, com schemas e verificações. Mudanças passam por revisão; cada verbete retém histórico de edição.

## Consequências
**Benefícios:** transparência, versionamento, possibilidade de diff e publicação estática.
**Custos:** edição mais técnica e necessidade de ferramentas de validação.
**Não implica:** escolha definitiva do framework web ou banco operacional.

[Início do vault Obsidian](../../INICIO.md)
