# Web Scrapping Classroom Of The Elite

## Links e utilitários

Link principal:

<https://animecenterbr.com/youkoso-jitsuryoku-light-novel-pt-br/>

Links de exemplo:

<https://animecenterbr.com/youkoso-jitsuryoku-prologo-vol-1/>
<https://animecenterbr.com/youkoso-jitsuryoku-capitulo-1-vol-1/>
<https://animecenterbr.com/youkoso-jitsuryoku-vol-1-ss-horikita-uma-certa-manha-na-piscina/>

Sobre a estrutura do HTML:

- __Título do capítulo__
  - Os capítulos possuem uma tag `h2` que é o `título do volume`
  - Também pode ser uma tag `strong` dentro de uma tag `p` no início do capítulo
- __Texto corrido__
  - `p` são tags do texto corrido e podem ou não ter dentro de si algumas outras tags:
    - `span` (caso tenha) é o parágrafo corrido normal
    - `em` é o parágrafo em itálico
    - `strong` é um parágrafo em negrito, para iniciar uma nova sessão de texto
- __Imagens__
  - Imagens estão em tags `img` soltas logo após tags `p` ou `div` (propaganda)

## Ideia para desenvolvimento

Opção de passos 1:

1. Código acessa a página raiz contendo todos os links dos capítulos
2. Código varre e agrupa todos os links de acordo com a seção do volume específico
3. Código acessa cada link individualmente, renderiza o HTML e faz o scrapping do texto e imagem formatado
4. Código cria arquivo .ODT e salva as imagens e textos formatados no arquivo criado (com o nome do capítulo)
5. Código retorna para etapa 1

Opção de passos 2:

1. Usuário vai copiar a URL específica que deseja fazer download (pois são muitas variações possíveis, impossível de colocar no código)
2. Código renderiza o HTML e faz o scrapping do texto e imagem formatado
3. Código cria arquivo .ODT e salva as imagens e textos formatados no arquivo criado (com o nome do capítulo)
4. Usuário retorna para etapa 1

## Etapas para desenvolvimento

Opção de passos 1:

   - [x] Código acessa a página raiz contendo todos os links dos capítulos
   - [ ] Código varre todos os links e agrupa de acordo com a seção do volume específico
   - [ ] Código acessa cada link individualmente, renderiza o HTML e faz o scrapping do texto e imagem formatado
   - [ ] Código cria arquivo .ODT e salva as imagens e textos formatados no arquivo criado (com o nome do capítulo)
   - [ ] Código retorna para etapa 1
