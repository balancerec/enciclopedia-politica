# Enciclopédia do Pensamento Político

> **História · Filosofia · Ideologias · Economia política · Instituições · Movimentos sociais**

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-555)](docs/PLANEJAMENTO.md)
[![Idioma](https://img.shields.io/badge/idioma-pt--BR-blue)](docs/METODOLOGIA.md)

## Missão

Construir uma enciclopédia aberta, documentada e crítica sobre as correntes do pensamento político, do mundo antigo às disputas contemporâneas, com linguagem acessível, rastreabilidade bibliográfica e separação rigorosa entre **teoria normativa**, **programas políticos** e **práticas históricas**.

**Não é propaganda eleitoral nem um teste de alinhamento ideológico.** Descrever uma corrente não significa endossá-la.

## O que o projeto cobre

- Ideologias e famílias ideológicas, com suas subdivisões e relações.
- Filosofia política, teoria democrática, economia política e sistemas institucionais.
- Autores, obras originais, movimentos, governos e contextos históricos.
- Comparações multidimensionais, divergências internas, críticas documentadas e controvérsias de terminologia.
- Recortes brasileiros e latino-americanos sem reduzir conceitos globais à política partidária do presente.

**Nota de escopo:** não existe enumeração consensual ou fechada de “todas as ideologias”. O catálogo é um índice em expansão, não uma afirmação de completude.

## Comece aqui

| Documento | Finalidade |
|---|---|
| [Planejamento e checklist](docs/PLANEJAMENTO.md) | Etapas, critérios de conclusão e atualização |
| [Metodologia editorial](docs/METODOLOGIA.md) | Pesquisa, evidências e neutralidade analítica |
| [Taxonomia](docs/TAXONOMIA.md) | Famílias, categorias e vocabulário controlado |
| [Modelo de verbete](docs/MODELO_VERBETE.md) | Padrão dos quinze eixos de análise |
| [Arquitetura técnica](docs/ARQUITETURA.md) | Dados, aplicações, validação e publicação |
| [Matriz comparativa](docs/MATRIZ_COMPARATIVA.md) | Parâmetros de comparação |
| [Bibliografia](docs/BIBLIOGRAFIA.md) | Referências de partida e protocolo de citação |
| [Governança editorial](docs/GOVERNANCA.md) | Revisão, correções, desacordos e versionamento |
| [Catálogo de correntes](catalogo/README.md) | Índice normalizado com status de cada entrada |
| [Termos candidatos](catalogo/TERMOS_CANDIDATOS.md) | Fila editorial de novas correntes a avaliar |
| [Pesquisa fundamentada](pesquisa/README.md) | Fontes identificadas e fichamentos críticos |
| [Liberalismo — pesquisa inicial](verbetes/ideologias/liberalismo.md) | Primeiro estudo ampliado, ainda em rascunho |
| [Auditoria documental](docs/RELATORIO_DE_AUDITORIA_V1.md) | Resultados verificados e pendências |
| [Volumes](volumes/README.md) | Programa editorial dos 12 volumes |
| [Como contribuir](CONTRIBUTING.md) | Guia para colaboração |

## Coleção planejada — 12 volumes

1. Fundamentos das grandes ideologias políticas
2. Socialismo, comunismo e escolas marxistas
3. Liberalismo, libertarianismo e capitalismo
4. Anarquismo e teorias antiautoritárias
5. Conservadorismo, nacionalismo e tradicionalismo
6. Fascismo, nazismo e movimentos autoritários
7. Democracia, republicanismo e organização do Estado
8. Religião, monarquismo e pensamento político
9. Feminismo, ecologismo e movimentos emancipatórios
10. Economia política e modelos de produção
11. Brasil e América Latina: correntes e movimentos
12. Ideologias contemporâneas, tecnologia e novas correntes

Os **índices** não equivalem a volumes finalizados. O avanço real é marcado em [PLANEJAMENTO.md](docs/PLANEJAMENTO.md).

## Convenções essenciais

- **Tipo de entidade:** distinguir ideologia, vertente, teoria, política econômica, regime, forma de governo, movimento e rótulo analítico.
- **Relações não são identidades:** fascismo, autoritarismo e ditadura, por exemplo, não são sinônimos.
- **Classificações contextuais:** esquerda/direita e autoridade/liberdade são aproximações, não coordenadas científicas universais.
- **Exemplos históricos:** identificar tempo, lugar, fontes e disputas historiográficas.
- **Bibliografia:** fontes primárias para posições originais; historiografia e filosofia política para interpretação crítica.
- **Status editorial:** `planejado`, `rascunho`, `em_revisao`, `publicado` ou `desatualizado`.

## Como a documentação está organizada

```text
.
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── docs/                  # decisões, padrões, metodologia e planejamento
├── catalogo/              # índice dos conceitos e taxonomia
├── volumes/               # 12 volumes e suas propostas editoriais
├── verbetes/              # verbetes individuais versionados
├── data/                  # exemplos e estruturas de dados
└── schemas/               # validação formal (JSON Schema)
```

## Referências acadêmicas iniciais

- Stanford Encyclopedia of Philosophy — [Liberalism](https://plato.stanford.edu/entries/liberalism/), [Socialism](https://plato.stanford.edu/entries/socialism/), [Anarchism](https://plato.stanford.edu/entries/anarchism/), [Conservatism](https://plato.stanford.edu/entries/conservatism/), [Nationalism](https://plato.stanford.edu/entries/nationalism/), [Democracy](https://plato.stanford.edu/entries/democracy/).
- Textos primários e bibliografia comentada: [docs/BIBLIOGRAFIA.md](docs/BIBLIOGRAFIA.md).

## Licenciamento

**Pendente de decisão do mantenedor.** Recomenda-se avaliar **CC BY 4.0** para textos próprios e **MIT** para código futuro, levando em conta que obras, imagens, traduções e trechos de terceiros podem ter direitos específicos. Até a inclusão de licenças explícitas, **não presumir licença aberta**.

## Situação do projeto

Documentação-base em construção. Nenhum volume será rotulado como concluído antes de passar por revisão de fontes, qualidade e consistência. O checklist de entregas é a fonte de verdade editorial.

---
**Repositório:** https://github.com/balancerec/enciclopedia-politica
