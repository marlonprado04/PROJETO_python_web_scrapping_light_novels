# Web Scrapping TBATE

Repositório destinado a realizar Web Scrapping da light novel The Beginning After The End.

## Sobre o projeto

O projeto é realizado em __Python__, através do VSCode com extensões que permitem trabalhar com arquivos `.ipynb`, mas pode ser compilado no __Google Colaboratory__ ou o próprio __Jupiter Notebook__.

Também há uma versão alternativa feita em `.py` que pode ser executado em qualquer máquina com __Python__ instalado.

## Site usado

Na primeira versão do código o site utilizado para scrapping foi o [Reaper Scans](https://reaperscans.net/series/o-comeco-apos-o-fim-novel), mas após algumas alterações no layout do site resolvi substituí-lo pelo [Central Novel](https://centralnovel.com/series/the-beginning-after-the-end/) já que este contém mais estabilidade e os dados estão melhor estruturados.

## Bibliotecas e versões

Para que o código funcione é necessário ter instalado e importado as bibliotecas `requests` e `BeautifulSoulp` da `bs4`.

As versões utilizadas foram:

- `Python` => 3.10.2
- `BeautifulSoup` => 4.12.2
- `requests` => 2.31.0

## URL utilizadas

Abaixo as 2 URLs utilizadas na raspagem de dados deste projeto:

ReaperScans: <https://reaperscans.com.br/obra/o-comeco-apos-o-fim/>

Central Novel: <https://centralnovel.com/series/the-beginning-after-the-end/>

## Ordem de capítulos e livros do TBATE

[Neste site](https://tbate.fandom.com/wiki/Volumes_and_Chapters) encontramos a listagem de capítulos e volumes da obra para tomarmos como base.

O agrupamento no site __Central Novel__ respeita a ordem original da obra, conforme relação abaixo:

- Volume 1 = 1 ao 21
  - 14.5
- Volume 2 = 22 ao 42
- Volume 3 = 43 ao 68
- Volume 4 = 69 ao 97
- Volume 5 = 98 ao 138
- Volume 6 = 139 ao 194
- Volume 7 = 195 ao 249
  - 221.5, 223.5, 230.5, 233.5
- Volume 8 = 250 ao 313
- Volume 8.5 (extra) = 1 ao 20
- Volume 9 = 314 ao 381
  - 374.5
- Volume 10 = 382 ao 429
- Volume 11 = 330 ao 439

## Próximas etapas

- [x] Adicionar quebra de linha nos parágrafos
- [x] Adaptar nome dos arquivos para ordenação "009, 099, 999"
- [x] Criar arquivo alternativo no formato .py para poder editar e executar com mais facilidade
- [x] Refatorar código para receber caminho de download informado pelo usuário
- [ ] - [ ] Refatorar código para baixar capítulos intermediários (ex: 14-5, 221-5)
