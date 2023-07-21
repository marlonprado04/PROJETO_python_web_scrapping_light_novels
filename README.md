# Web Scrapping TBATE

Repositório destinado a realizar Web Scrapping da light novel The Beginning After The End

## Site usado

Na primeira versão do código o site utilizado para scrapping foi o [Reaper Scans](https://reaperscans.net/series/o-comeco-apos-o-fim-novel), mas após algumas alterações no layout e novas descobertas, este site foi substituído pelo [Central Novel](https://centralnovel.com/series/the-beginning-after-the-end/), por conter mais estabilidade e os dados estarem melhor estruturados.

## Sobre o projeto

O projeto é realizado em __Python__, através do VSCode com extensões que permitem trabalhar com arquivos `.ipynb`, mas pode ser compilado no __Google Colaboratory__ ou adaptado para um script Python convencional.

### Bibliotecas e versões

Para que o código funcione é necessário ter instalado e importado as bibliotecas `requests` e `BeautifulSoulp` da `bs4`.

As versões utilizadas foram:

- `Python` => 3.10.2
- `BeautifulSoup` => 4.12.2
- `requests` => 2.31.0

### URL utilizadas para realizar a raspagem de dados

ReaperScans: <https://reaperscans.com.br/obra/o-comeco-apos-o-fim/>

Central Novel: <https://centralnovel.com/series/the-beginning-after-the-end/>

### Ordem de capítulos e livros do TBATE

<https://tbate.fandom.com/wiki/Volumes_and_Chapters>

Agrupamento no site __Central Novel__:

- Volume 1 = 1 ao 21
- Volume 2 = 22 ao 42
- Volume 3 = 43 ao 68
- Volume 4 = 69 ao 97
- Volume 5 = 98 ao 138
- Volume 6 = 139 ao 194
- Volume 7 = 195 ao 249
- Volume 8 = 250 ao 313
- Volume 8.5 (extra) = 1 ao 20
- Volume 9 = 314 ao 381 (+374.5)
- Volume 10 = 382 ao 429
- Volume 11 = 330 ao 439
