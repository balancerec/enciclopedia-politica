---
id: doc-modelo-verbete
classe: documentacao
titulo: "Ficha canônica de verbete — 15 dimensões"
status: ativo
aliases: []
tags:
  - enciclopedia/documentacao
atualizado_em: 2026-11-22
---
# Ficha canônica de verbete — 15 dimensões

Todo verbete usa frontmatter/JSON validável e 15 seções editoriais. A publicação é condicionada à revisão, não ao simples preenchimento de campos.

## Metadados obrigatórios
- id (slug único), nome, tipo, família, volume, status.
- resumo neutro (até 500 caracteres), aliases, tags, idiomas e relações.
- autores/revisores, datas (criação/atualização), fontes referenciadas.
- versão do modelo, observações terminológicas e grau de controvérsia.

## Estrutura do corpo
1. **Identidade:** definição precisa e delimitação.
2. **Origem:** contexto histórico, intervalos e local.
3. **Pensadores:** autores relevantes e papel de cada um.
4. **Obras:** referência bibliográfica completa quando pesquisada.
5. **Filosofia:** fundamentos morais, antropológicos e epistemológicos.
6. **Estado:** funções, legitimidade, tamanho, centralização.
7. **Economia:** propriedade, mercado, coordenação, distribuição.
8. **Propriedade:** distinção entre bens pessoais e meios de produção quando relevante.
9. **Democracia:** participação, pluralismo, oposição, sufrágio.
10. **Liberdades:** expressão, consciência, reunião, associação e suas tensões.
11. **Igualdade:** jurídica, política, econômica, oportunidades e resultados.
12. **Religião:** religião pública, laicidade, confessionalismo, tolerância.
13. **Experiências:** casos históricos atribuídos, com datas, diversidade interna e cautelas.
14. **Críticas e respostas:** controvérsias historiográficas e argumentos substantivos dos interlocutores.
15. **Subcorrentes:** mapa de heranças, diferenças e conexões.

## Referências por afirmação
Uma bibliografia final genérica **não** é suficiente para afirmações controversas. Para cada alegação específica, anexar nota com identificação de fonte e, quando pertinente, capítulo/página. Usar citações literais curtas e atribuição contextual.

## Grau de confiança de cada afirmação factual
- alto: convergência robusta de fontes independentes ou documentação primária clara;
- médio: literatura relevante com controvérsia contextual;
- baixo: interpretação disputada, lacuna documental ou fonte única.
Não medir "verdade ideológica" por nota numérica.

## Estados editoriais
- planejado: apenas registro de intenção;
- rascunho: texto ainda sem revisão completa;
- em_revisao: fontes e texto submetidos ao processo;
- publicado: aprovações e evidências suficientes;
- desatualizado: revisão necessária por evidência posterior.

## Arquivo modelo
Consultar [verbetes/_TEMPLATE.md](../verbetes/_TEMPLATE.md) e [schemas/verbete.schema.json](../schemas/verbete.schema.json). Os exemplos fornecidos são demonstrativos e **não equivalem a verbetes publicados**.

## Auditoria antes da publicação
Verificar classificação, precisão histórica, autores, distinção entre experiência e teoria, bibliografia, contra-argumentos, ortografia, formatação e acessibilidade.

[Início do vault Obsidian](../INICIO.md)
