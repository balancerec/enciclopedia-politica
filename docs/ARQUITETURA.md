---
id: doc-arquitetura
classe: documentacao
titulo: "Arquitetura documental e técnica — proposta V1.0"
status: ativo
aliases: []
tags:
  - enciclopedia/documentacao
atualizado_em: 2026-11-22
---
# Arquitetura documental e técnica — proposta V1.0

## Estado real
Este repositório possui documentação e estruturas de dados iniciais. **Não existe ainda plataforma web implementada**, API operacional ou banco em produção. Esta arquitetura é uma proposta, sujeita a ADR antes da implantação.

## Princípios
1. Conteúdo como código versionado: textos, referências e dados em Git.
2. Texto editorial separado de metadados estruturados.
3. Validação automática para impedir entradas quebradas ou duplicadas.
4. Página estática legível por humanos e mecanismos de busca.
5. Multidimensionalidade: um conceito pode se relacionar a mais de uma família.
6. Bibliografia e versão rastreáveis por item.
7. Acessibilidade e internacionalização sem comprometer português do Brasil.

## Camadas propostas
~~~text
Fontes primárias/secundárias (externas)
                |
         Pesquisa e revisão
                |
    Markdown + JSON / JSON Schema
                |
        Validação e build
                |
      Busca / índice / remissivas
                |
   Website estático (GitHub Pages)
                |
     Usuários, leitores e revisão
~~~

## Stack (candidata, ainda não aprovada)
- **Astro + Starlight:** publicação documental rápida e estática.
- **TypeScript:** tipagem de dados, índice e verificações de build.
- **Markdown/MDX:** autoria editorial com frontmatter.
- **JSON Schema 2020-12:** contratos e verificações independentes do framework.
- **Busca estática:** Pagefind ou alternativa equivalente após avaliação.
- **CI/CD:** GitHub Actions com permissões mínimas.
- **Hospedagem:** GitHub Pages, respeitando prefixo /enciclopedia-politica/.

### Alternativa
Next.js com exportação estática quando houver demanda que justifique recursos adicionais. A opção final deve ser registrada em ADR, com custos e implicações de hospedagem.

## Estrutura do repositório
~~~text
README.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
CHANGELOG.md
SECURITY.md
docs/
  METODOLOGIA.md
  TAXONOMIA.md
  MODELO_VERBETE.md
  MATRIZ_COMPARATIVA.md
  BIBLIOGRAFIA.md
  GOVERNANCA.md
  ARQUITETURA.md
  UX_E_ACESSIBILIDADE.md
  PLANEJAMENTO.md
  DECISOES/
catalogo/
  README.md
  catalogo.json
volumes/
  README.md
  01-fundamentos/README.md
  ...
  12-contemporaneas/README.md
verbetes/
  README.md
  _TEMPLATE.md
  ideologias/
data/
  verbete-exemplo.json
schemas/
  catalogo.schema.json
  verbete.schema.json
scripts/
  validar_catalogo.py
~~~

## Modelo de entidade
- ID e slug estáveis (evitar mudar, usar alias/redirecionamento se necessário).
- Nome canônico, aliases, tipo, família(s), volume principal.
- Relações semânticas direcionadas e fontes.
- 15 dimensões de análise por verbete.
- Estados editoriais e datas.
- Histórico de fonte/versão no Git.

## Caminho dos dados
1. Cadastrar entidade no catálogo.
2. Criar arquivo do verbete seguindo template.
3. Validar estrutura e fontes.
4. Revisar texto e relações cruzadas.
5. Publicar quando critérios editoriais estiverem cumpridos.
6. Construir índices e páginas derivadas no build.

## Segurança e privacidade
- Nenhuma autenticação é necessária para leitura pública.
- Não guardar dados pessoais de leitores no repositório.
- Fontes externas sem scripts arbitrários incorporados.
- Escapar Markdown/HTML, validar URL e restringir permissões CI.
- Preferir páginas estáticas, evitando superfícies de ataque desnecessárias.

## Evolução futura
Fase 1, publicação textual; fase 2, comparador e mapas de influências; fase 3, cronologia e visualizações geográficas; fase 4, multilíngue e API pública versionada. **Nada disso está implantado nesta etapa.**

## Decisões pendentes
- Framework, buscador, política de cache, metadados de SEO, hospedagem final.
- Regime de licenças e regras de colaboração com direitos de reprodução.
- Versão final do modelo de dados e migrações futuras.


## Implementação Obsidian (2026-11-22)

**Camada de pesquisa efetivamente implementada:** vault local com arquivos Markdown, propriedades YAML, MOCs, consultas nativas Bases, Canvas e modelos, conforme [guia Obsidian](OBSIDIAN.md).

- `catalogo/catalogo.json` continua sendo a referência de IDs e tipologia.
- Os 168 IDs estão materializados em notas em `verbetes/ideologias/` e `verbetes/conceitos/`.
- `mapas/` agrega conceitos por volume e cria links internos de navegação.
- `pesquisa/fontes/notas/`, `pesquisa/autores/` e `pesquisa/obras/` conectam pesquisa documental a verbetes.
- Obsidian é editor/navegador local. **Não substitui** a proposta futura do site Astro/Next.js.
- `scripts/validar_obsidian.py` verifica coerência estrutural. Migração automática futura deve evitar IDs duplicados.

**Decisão atual:** arquivos Markdown relativos como interoperabilidade padrão Obsidian/GitHub. Wikilinks e embeds específicos são usados apenas nos painéis onde o recurso é realmente necessário.

[Início do vault Obsidian](../INICIO.md)
