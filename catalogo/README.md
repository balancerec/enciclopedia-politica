# Catálogo de conceitos

## Finalidade
Manter um índice normalizado de correntes, doutrinas, movimentos e conceitos correlatos. O arquivo [catalogo.json](catalogo.json) é o índice estruturado inicial, não a obra redigida.

## Tipos
Ver [TAXONOMIA](../docs/TAXONOMIA.md): ideologia, vertente, teoria_politica, teoria_economica, sistema_economico, regime, forma_governo, movimento, politica_publica, doutrina_politico_religiosa e rotulo_analitico.

## Regra de entrada
Todo registro contém identificador, nome, tipo, família principal, volume principal e estado. A presença no catálogo não significa endosso, completude ou verificação historiográfica.

## Operações
1. Verificar se já existe um ID/alias.
2. Escolher tipo com justificativa.
3. Atribuir família e volume principal.
4. Marcar "planejado" até haver texto e referências.
5. Criar verbete e metadados quando houver pesquisa.
6. Revisar links de relações antes de publicar.

## Convenções
Slugs sem acento e em kebab-case. Homônimos exigem qualificador. Conceitos transversais podem pertencer a múltiplas famílias, com uma única URL canônica.

## Riscos conhecidos
As nomenclaturas mudam entre idiomas, épocas e autores. Rótulos controversos requerem notas e fontes; classificações que rotulam movimentos contemporâneos não podem ser afirmadas sem evidência suficiente.


## Integração com Obsidian

Cada entidade de `catalogo.json` possui o campo `nota` apontando a um arquivo Markdown do vault. Existem 12 fichas em `verbetes/ideologias/` e 156 notas planejadas em `verbetes/conceitos/`. O catálogo **não** é automaticamente atualizado quando uma propriedade YAML muda: sincronize os dois arquivos e rode o [validador](../scripts/validar_obsidian.py).

[Índice navegável](../mapas/INDICE-CONCEITOS.md).
