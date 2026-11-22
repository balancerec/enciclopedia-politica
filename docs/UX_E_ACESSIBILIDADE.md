# Experiência de leitura, navegação e acessibilidade

## Objetivos de UX
A enciclopédia deve funcionar em telefone, tablet e desktop, com foco na leitura profunda e na busca por conceitos.

## Páginas principais propostas
1. Início: busca, 12 volumes e conceitos de entrada.
2. Catálogo: filtro por tipo, família, período, status e assunto.
3. Verbete: resumo, sumário das 15 seções, fontes e conceitos relacionados.
4. Comparador: seleção de até quatro correntes e dimensões explícitas.
5. Linha do tempo: autores, obras, eventos e contextos.
6. Grafo: influência histórica e desambiguação com notas de fonte.
7. Bibliografia: busca por autor, obra, período e tipo.
8. Sobre/metodologia: transparência e correção de erros.

## Padrão visual proposto
- Identidade editorial sóbria; hierarquia tipográfica nítida; espaço generoso.
- Modo claro e escuro opcional com contraste aferido.
- Cor não deve ser o único meio de expressar posição, parentesco ou status.
- Ícones acompanhados de texto; evitar símbolos de movimentos usados fora de contexto.
- Não atribuir valor moral fixo a cores de espectro político.
- Visualizações com legenda, ressalvas e versão em tabela acessível.

## Acessibilidade
Meta: WCAG 2.2 nível AA, sem alegar conformidade antes de testar.
- Teclado para toda interação e foco visível.
- Sem conteúdo bloqueado apenas por hover.
- Contraste adequado de texto e componentes.
- Leitores de tela: landmarks, headings sem salto, estados acessíveis.
- Tabelas com cabeçalhos e legendas.
- Gráficos com resumo textual e dados tabulares.
- Respeito a prefers-reduced-motion.
- Links com rótulos descritivos.
- Textos ajustáveis, layout sem rolagem horizontal forçada no mobile.

## Busca e navegação
- Alias e termos equivalentes dirigem ao conceito canônico.
- Auto-complete deve distinguir ideologia, regime, teoria e movimento.
- Avisos de classificação contestada nos verbetes.
- Links diretos para seção e referência específica.
- Breadcrumbs com família e volume principal.
- Sem bloquear leitura por login.

## Comparador — regras
Apresentar tipo e contexto de cada coluna. Não montar "placar" de virtudes com pesos arbitrários. Mostrar "variável" ou "não informado" quando necessário e referência associada às células.

## Testes de aceitação planejados
- Navegação exclusivamente por teclado.
- Leitura em dispositivo de largura estreita e alto zoom.
- Busca por nome com e sem acentos.
- Leitor de tela entende tabela de comparação.
- Usuário identifica claramente estado "rascunho".
- Links externos possuem destino e contexto legíveis.
