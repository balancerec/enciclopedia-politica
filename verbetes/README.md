# Verbetes

Cada verbete possui ID estável, tipo de entidade, família, bibliografia e 15 dimensões descritivas. O template [ _TEMPLATE.md ](_TEMPLATE.md) é a estrutura editorial. A representação JSON de exemplo está em [data/verbete-exemplo.json](../data/verbete-exemplo.json).

## Fluxo
Planejado → rascunho → em revisão → publicado → desatualizado (quando necessitar atualização).

## Não confundir
Fichas preparatórias ou demonstrativas não são pesquisa acadêmica revisada, independentemente do tamanho do texto.

## Nomenclatura
Use id canônico igual ao slug no catálogo. Um conceito com mais de um nome deve guardar aliases e remissivas.

## Fichas introdutórias do Volume I (rascunhos)
- [Liberalismo](ideologias/liberalismo.md)
- [Socialismo](ideologias/socialismo.md)
- [Comunismo](ideologias/comunismo.md)
- [Anarquismo](ideologias/anarquismo.md)
- [Conservadorismo](ideologias/conservadorismo.md)
- [Social-democracia](ideologias/social-democracia.md)
- [Libertarianismo](ideologias/libertarianismo.md)
- [Nacionalismo](ideologias/nacionalismo.md)
- [Fascismo](ideologias/fascismo.md)
- [Democracia](ideologias/democracia.md)
- [Feminismo político](ideologias/feminismo-politico.md)
- [Ecologismo político](ideologias/ecologismo-politico.md)

**Nenhuma ficha desta lista foi aprovada como publicação acadêmica.**


## Integração Obsidian

- `ideologias/`: 12 verbetes introdutórios já desenvolvidos, ainda em rascunho.
- `conceitos/`: 156 **notas planejadas** para que todos os conceitos estejam presentes no grafo.
- [Índice canônico de conceitos](../mapas/INDICE-CONCEITOS.md) e [Bases de verbetes](../bases/VERBETES.base).

Não editar `id` sem migração. Alterações de `status` ou `familias` devem ser refletidas no catálogo JSON e verificadas em CI. Uma nota navegável não é sinônimo de pesquisa concluída.
