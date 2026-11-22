---
id: guia-obsidian
titulo: Guia do Obsidian
classe: documentacao
status: ativo
tags:
  - sistema/obsidian
  - guia
---
# Guia Obsidian — Enciclopédia Política

## 1. Instalação e abertura do vault
No Windows, abra PowerShell e execute:

```powershell
git clone https://github.com/balancerec/enciclopedia-politica.git
```

No aplicativo Obsidian, escolha **Abrir pasta como vault** e selecione a pasta inteira `enciclopedia-politica`. Abra [INICIO](../INICIO.md), não um subdiretório do projeto.

## 2. O que está configurado
- `.obsidian/app.json`: links Markdown relativos e atualização automática ao renomear.
- `.obsidian/core-plugins.json`: Graph, Backlinks, Canvas, Bases, Templates e outros plugins nativos.
- `.obsidian/templates.json`: modelos em `_sistema/templates/`.
- `.obsidian/daily-notes.json`: diário de pesquisa em `_sistema/diario/`.
- `.gitignore`: arquivos locais de workspace não devem ser versionados.
- Não há necessidade de plugin comunitário, Dataview ou serviço pago.

Se sua versão do Obsidian não reconhecer `.base`, atualize o aplicativo: os arquivos Markdown continuam legíveis.

## 3. Organização
- `INICIO.md`: mapa principal.
- `mapas/`: Mapas de Conteúdo (MOCs) dos 12 volumes.
- `verbetes/ideologias/`: fichas já existentes (rascunhos).
- `verbetes/conceitos/`: notas individuais ainda planejadas.
- `pesquisa/`: fontes, fichamentos, autores e obras.
- `painel/`: painéis de acompanhamento.
- `bases/`: tabelas dinâmicas nativas.
- `canvas/`: mapa visual de volumes.
- `_sistema/templates/`: modelos de novas notas.
- `catalogo/catalogo.json`: lista canônica de IDs, classificações e estados.
- `docs/PLANEJAMENTO.md`: lista oficial de etapas concluídas.

## 4. Metadados
Use propriedades YAML no início de cada arquivo. Exemplo:

```yaml
---
id: liberalismo
classe: verbete
tipo: ideologia
status: rascunho
volume_principal: 1
familias:
  - F01
  - F03
aliases:
  - Liberalismo
tags:
  - enciclopedia/verbete
  - estado/rascunho
---
```

Regras: `id` estável, `tipo` de acordo com taxonomia, `status` fiel ao estado editorial. Tags hierárquicas não substituem a classificação acadêmica. Os status possíveis de verbetes são `planejado`, `rascunho`, `em_revisao`, `publicado` e `desatualizado`.

## 5. Links e grafo
Prefira links Markdown relativos, por exemplo `[Socialismo](../verbetes/ideologias/socialismo.md)`. Obsidian identifica esses links e também reconhece `[[wikilinks]]`, mas o Markdown relativo mantém navegabilidade no GitHub. Não use apenas `README` em links, pois há vários nomes idênticos; prefira MOCs `mapas/VOLUME-XX.md` ou caminhos completos.

Para ver conexões, abra **Graph View**. O mapa `canvas/ENCICLOPEDIA.canvas` é uma visualização visual editável, diferente do grafo automático.

## 6. Bases e templates
Acesse [Verbetes](../bases/VERBETES.base), [Volumes](../bases/VOLUMES.base) e [Pesquisa](../bases/PESQUISA.base). Para criar nova nota use o comando **Templates: Insert template**, depois escolha Verbete, Fonte, Fichamento, Pensador, Obra, Revisão editorial ou Registro diário.

## 7. Fluxo de trabalho
1. Encontre o conceito no [Índice](../mapas/INDICE-CONCEITOS.md).
2. Documente fontes com autor, edição, localizador e URL.
3. Redija com as 15 dimensões e registre críticas com atribuição.
4. Preserve `status: rascunho` até revisão independente.
5. Mantenha `catalogo/catalogo.json` e o `status` da nota sincronizados.
6. Atualize [PLANEJAMENTO](PLANEJAMENTO.md) e [CHANGELOG](../CHANGELOG.md) com o mesmo avanço.
7. Execute os validadores antes de enviar ao Git.

```powershell
git pull --ff-only
python scripts/validar_catalogo.py
python scripts/validar_pesquisa.py
python scripts/validar_obsidian.py
git add .
git commit -m "docs: atualiza enciclopedia"
git push
```

Não usar `git push --force`, nem versionar tokens, workspace pessoais ou livros protegidos. Para colaborar, preferir branches e pull requests.

## 8. Fontes oficiais do Obsidian
- [Vault](https://obsidian.md/help/vault)
- [Links internos](https://obsidian.md/help/links)
- [Propriedades](https://obsidian.md/help/properties)
- [Templates](https://obsidian.md/help/plugins/templates)
- [Bases](https://obsidian.md/help/bases)
- [Graph View](https://obsidian.md/help/Plugins/Graph+view)
- [Canvas](https://obsidian.md/help/Plugins/Canvas)

## 9. Limites da implementação
Os painéis consultam metadados das notas, não verificam sua história. O cadastro JSON continua sendo a fonte canônica de IDs; o Markdown é sua representação no Obsidian. A migração preserva os arquivos originais e o histórico Git; o deploy web e a revisão acadêmica continuam pendentes.
