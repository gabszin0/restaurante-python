## Esse código é um script em Python que gerencia um sistema de restaurantes:

### Lista de Restaurantes

O script começa criando uma lista de dicionários chamada `restaurantis`, onde cada dicionário representa um restaurante com nome, categoria e estado ativo/inativo.

### Funções

O código define várias funções para executar operações:

- **`exibir_nome()`**: Exibe um banner estilizado no console.
- **`opcoes()`**: Exibe o menu de opções.
- **`exibir_subtitulo(texto)`**: Limpa o console e exibe um texto como subtítulo.
- **`finalizar_app()`**: Exibe uma mensagem de finalização.
- **`opcao_inva()`**: Exibe uma mensagem de opção inválida e retorna ao menu.
- **`voltar_menu()`**: Espera uma tecla para voltar ao menu.
- **`cadastro_resta()`**: Permite cadastrar um novo restaurante, solicitando nome e categoria.
- **`listar_resta()`**: Lista todos os restaurantes cadastrados.
- **`alternar_estado()`**: Ativa ou desativa um restaurante com base no nome informado.

### Escolher Opção

A função `escolher_opcao()` permite ao usuário selecionar uma opção no menu. Ela utiliza a estrutura `match` para determinar qual função chamar com base na opção escolhida.

### Função Principal

A função `main()` organiza a execução do programa. Limpa o console, exibe o banner, mostra o menu de opções e espera uma escolha.

Ao executar o script, ele entra na função `main()` e permanece no loop até que o usuário escolha sair. Basicamente, o código gerencia a listagem e o estado de ativação dos restaurantes cadastrados.
