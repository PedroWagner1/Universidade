# Projeto ONG: Animal Heroes

<h1>Este é um projeto que eu desenvolvi como atividade da universidade.</h1>

<h2>O projeto apresenta a aplicação prática de:</h2>

<ul>
<li>HTML Semântico</li>
<li>CSS e Estilização</li>
<li> Responsividade através de unidades de medidas como vw, vh e %, além de uso de flexbox e grid's para organização do conteúdo</li>
<li> Utilização de JS com manipulação do DOM para redirecionamento de página e exibição de aside em button </li>
<li> Elementos de Formulário com filtro (pattern) e estilização adequada </li>
</ul>

Fiquei em torno de aprox. 1 semana codificando o site, estudando profundamente a linguagem de estilo para organizar corretamente
os elementos na pagina de forma que fique responsivo e dinâmico. Além da ferramenta de redimensionamento disponível na maioria dos clientes
de Browser atualmente, rodei o projeto em um apache2 no meu Kubuntu para testar na prática como o site ficaria em uma tela de celular, certificando de fato a ótima responsividade que consegui aplicar, principalmente pela ajuda da unidade vw, ótima para fazer os elementos
não excederem o tamanho da tela, além da utilização de flex-grow, flex,shrink e flex-basis (propriedade flex: ) para tornar mais dinâmico ainda. 


<h3>Fontes Utilizadas durante o Desenvolvimento:</h3>

<ul>
    
    <li>https://www.origamid.com/projetos/css-grid-layout-guia-completo/</li>
    <li>https://cssgradient.io (para pegar modelos de linear-gradient com escolha de cor gráfica)</li>
    <li> https://developer.mozilla.org/pt-BR/docs/Web/CSS/Reference#selectors (Checagem geral de propriedades CSS) </li>
    <li>https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Core/CSS_layout/Flexbox</li>
    <li> Além do curso de HTML5 e CSS3 gratuito extra presente no curso que faço atualmente de Python3 de Otávio Miranda (Udemy) </li>
    <li> Entre outras fontes como vídeos do youtube, etc </li>
</ul>

<h3>Estrutura Geral: Explicação Concisa </h3>

Bom, primeiro eu comecei desenvolvendo a semãntica, depois fiz o CSS e por fim os script's, o projeto inteiro está com
uma estrutura de pastas que segue as boás práticas para melhor organização e visualização. A respeito da criação do layout
do cabeçalho, desenvolvi toda a estilização dele dentro do elemento header do html. Ele possui position:fixed que força o layout a 
ficar persistente na visualização da página idependente de rolagem. Abaixo do header desenvolvi a seção main na qual atribui a propriedade
display:flex . O motivo pelo qual eu defini flex para o main é que minha idéia era estruturar a página principal verticalmente, tentando
torná-la o mais minimalista e elegante possível. Separei os conteúdos por section, definindo height de 100vh e restringindo seus elementos
filhos a aninharem seus conteúdos dentro desta altura, permitindo dessa forma um layout minimalista e muito elegante. No final do projeto
ainda antes do main uma div que é exibida na execução do button do cabeçalho, que abre um aside laterale exibe as páginas de acesso.
O script que executa essa ação está em Scripts/btn_redirecionar.js

Formatei cada section de maneira semelhante, para que as 2 primeiras fiquem ocupando os 100vh da tela, usando elementos de vw no font-size
dos elementos p e h, precisei definir essa unidade pois, na tela do meu celular (que deve ter uns 380 -420 de largura) o font-size ficava
estourando o section, fazendo o texto ficar escondido indo para baixo do background inferior do próximo section. Colocando vw consegui
fazer com que o tamanho da fonte redimensionasse conforme a tela diminui, o que me posibilitou arrumar este problema.

A respeito da página projetos.html, é definitivamente mais simples. Utilizei a mesma formatação do cabeçalho do index.html e defini uma grid
com grid-template-columns: repeat(auto-fit) essa solução eu demorei para conseguir resolver pois, eu estava tendo muita dificuldade para
fazer as imagens quebrarem a  linha de forma responsiva e adequada, inicialmente as imagens simplismente ficavam em uma única linha
pois eu havia declarado grid-template-columns: 1fr 1fr 1fr o que forçava o grid a SEMPRE manter 3 elementos em uma única linha


A página cadastro.html é a mais completa e a mais extensa em termos de separação de conteúdo, eu tive uma certa dificuldade para agrupar corretamente os conteúdos pois, meu raciocínio era o seguinte:

Quero colocar Nome e Sobrenome na mesma linha, porém ao mesmo tempo quero colocar CPF em uma única linha sozinho, quero colocar endereço
e estado na mesma linha mas outro elemento em uma única sozinho, etc. No geral esse problema me ajudou a entender melhor a estrutura de agrupamento que um grid ou um flexbox faz com seus elementos filhos, principalmente usando o gap para monitorar o que exatamente está sendo separado dentro da estrutura. Eu usei um



     Mapeamento: 

GRID: (1 coluna p/linha)

    Div: Flex row : Nome, Sobrenome (mesma linha)

    (campo CPF) -> 1 linha

    Div: Endereço,Numero (MESMA LINHA)

    Div: CEP, Estado (select) (MESMA Linha)

   Div: (Email) (Número) -> 1 linha (flexbox)


(comentário que fiz durante a criação para tentar fazer um mapa mental da separação)

Codei Scripts/btn_redirecionar_obrigado.js com basicamente o mesmo código do btn_redireciona porém desta vez redirecionando para obrigado.html, tive problemas inicialmente com o caminho relativo mas depois consegui referenciar corretamente.


<h3>Conclusão</h3>

Bem, eu fiquei aprox 1 semana codificando toda a página e o código é bem mais extenso que a minha explicação, no geral eu fiquei orgulhoso com o resultado e considerando que meu forte é mais back-end, eu acho que ficou muito bom. EU já havia conhecimentos de HTML e CSS3 (Mas não de JS) antes e isso me facilitou um pouco. Eu nunca havia programado efetivamente em JS e modeste a parte eu gostei bastante, achei divertido. Portanto creio eu ue possivelmente vou me aprofundar mais na linguagem, principalmente por causa do canva que eu vi alguns projetos incríveis. Enfim, essee projeto me inspirou a estudar mais a respeito de Javascript e de páginas web, e eu achei o resultado muito bom. Espero que gostem : )