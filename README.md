comandos

git:
git init

git add README.md

git commit -m "first commit"

git branch -M main

git remote add origin https://github.com/PJKTDELFOS/E_COMMERCE.git

git push -u origin main

git checkout  serve para trocar de  branch

django:
check:para checar problemas
startapp: começar os apps
createsuperuser: para criar o super usuario

instalar o pip install django-debug-toobar


para resolver o seguinte issue do check
'?: (urls.W005) URL namespace 'admin' isn't unique. You may not be 
able to reverse all URLs in this namespace
Resposta: apenas retire o path que esta repetido(resolução dia 05/11/2024)

'

questao da formatação, quando voce fizer um metodo que subescreve como uma coisa exibida,
voce lança no list display do admin, o nome do metodo que subescreve

para  justificar o texto, pode aplicar uma propriedade css direto no elemento como style="text-align: justify;"
atentar aos espaços entre os elementos inline,

posso fazer a adição de mais opções, inclusive a original, so adicionando mais options
fazer a a url apontar para o name space, , url de slug, deixa por ultimo que e melhor
sintaxe de url  = nome do app:nome da view exemplo : produto:lista
lembrar de att a pagina 

se usar ns views view tem que escrever na mao os metodos get e post



1. View (Classe Genérica Básica)
Definição: É a classe base genérica para criar qualquer tipo de view.
Objetivo: Fornece a estrutura para criar qualquer comportamento customizado em uma view.
Flexibilidade: Não impõe nenhum comportamento específico, então você deve definir manualmente como os dados são
rocessados e exibidos.
Métodos Customizáveis: Permite sobrescrever métodos HTTP, como get, post, put, delete, etc., 
para definir o comportamento desejado.
Uso Comum: Ideal para exibições que não precisam apenas listar objetos, como formulários de contato, exibições de 
detalhe customizadas ou qualquer view que exija lógica personalizada.


2. ListView (Classe Genérica para Listas)
Definição: Subclasse de View projetada especificamente para exibir listas de objetos.
Objetivo: Simplifica a exibição de uma lista de objetos de um modelo no Django.
Comportamento Automático: Configura automaticamente a busca dos objetos no banco de dados e passa uma lista para 
o template.
Configuração Rápida: É necessário apenas definir o model ou queryset que será listado, reduzindo a quantidade de código.
Atributos e Métodos Padrão: Possui atributos como model, context_object_name e paginate_by, e métodos como get_queryset 
para facilitar a personalização.
Uso Comum: Ideal para views que apenas listam objetos, como listagens de produtos, posts de um blog, ou listas de 
usuários.

quando precisar adicionar um contador, como por exemplo de produtos adicionados no carrinho
começo ele dentro da classe, e o chame pela sintaxe classe.variavel, eo incremente, jogue o valor em uma variavel
e a chame aonde precisar, como um informativo de  quantidade de produtos no carrinho
#contador = 0
#addcarrinho.contador+=1
#mensagem = f'compra adicionada {addcarrinho.contador}'