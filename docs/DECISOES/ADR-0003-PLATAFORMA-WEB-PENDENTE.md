---
id: doc-decisoes-adr-0003-plataforma-web-pendente
classe: decisao
titulo: "ADR-0003 — Plataforma estática de publicação"
status: proposto
aliases: []
tags:
  - enciclopedia/documentacao
atualizado_em: 2026-11-22
---
# ADR-0003 — Plataforma estática de publicação

- Estado: **proposto, não aprovado**.
- Data: 2026-11-22.

## Problema
Disponibilizar enciclopédia em português com busca, navegação por família, comparação e acessibilidade, sem infraestrutura complexa.

## Opção candidata
Astro + Starlight + TypeScript + Pagefind + GitHub Pages.

## Alternativa
Next.js com exportação estática, caso o produto precise de interfaces interativas que justifiquem maior configuração.

## Critérios de escolha
Compatibilidade com GitHub Pages, manutenção, performance mobile, busca, suporte a Markdown, schemas, acessibilidade, escalabilidade e facilidade de contribuir.

## Estado
Nenhum frontend, dependência, deploy ou workflow foi implementado por esta ADR.

[Início do vault Obsidian](../../INICIO.md)
