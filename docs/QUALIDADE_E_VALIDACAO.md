# Qualidade e validação — critérios de aceite

## Qualidade editorial
- Definição evita redução grosseira e inclui contexto.
- Tipos corretos de entidade; aliases e relações não contraditórios.
- Não confundir teoria, política proposta e consequências históricas.
- Autores e obras efetivamente relacionados à tradição.
- Datas, atribuições e traduções verificadas.
- Críticas e respostas apresentadas com fontes.
- Linguagem clara e sem doutrinação.

## Qualidade das fontes
- Conferir edição, autoria, datas e correspondência com a afirmação.
- Avaliar independência, competência e relevância da fonte.
- Registrar dissenso entre estudiosos quando substantivo.
- Evitar texto sem fontes em seções factuais publicadas.
- Links mortos não podem apagar a referência bibliográfica.

## Qualidade técnica
- Catálogo validável conforme JSON Schema.
- Sem IDs duplicados, slugs inválidos ou estados não reconhecidos.
- Volumes entre 1 e 12 e famílias F01–F12.
- Tipos de relação pertencem ao vocabulário controlado.
- Fontes de exemplo possuem URLs válidas.
- Ideal futuro: links cruzados resolvidos, lint de Markdown, checagem de URLs e CI.

## Governança de estados
- Rascunho ≠ publicado.
- Schemas aprovados ≠ dados historicamente revisados.
- CI verde ≠ validação acadêmica de conteúdo.
- Checklist [x] ≠ ausência de novas melhorias.
- Publicação só quando evidência e revisão humana documentadas.

## Plano de testes
| Teste | Método | Status inicial |
|---|---|---|
| JSON parse de catálogo e exemplos | Automatizado | A implantar como rotina CI |
| Chaves, slugs, tipos, duplicatas | Script inicial | A conferir por execução |
| Integridade de referências cruzadas | Automatizado | Planejado |
| Revisão historiográfica | Revisores | Pendente |
| Verificação de fontes e obras | Revisores | Pendente |
| Acessibilidade WCAG 2.2 AA | Ferramenta e revisão humana | Planejado |
| Desempenho do site | Lighthouse e métricas | Planejado |
| Segurança de dependências | CI | Planejado |

## Critério mínimo de lançamento do website
100% das rotas públicas sem erro, no mínimo o volume inicial revisado, busca funcional, referências legíveis, política de direitos definida, responsividade e avaliação de acessibilidade. Metas quantitativas adicionais a estabelecer com medições reais.
