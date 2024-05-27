
# Otimizando suas queries no Django ORM


Palestra dada no 12º encontro do GruPy em Mossoró.

Veja [aqui](https://www.github.com/yurisalesc/optimizing-your-django-orm-queries-talk/blob/main/presentation.pdf) os slides.
## Autor

- [@yurisalesc](https://www.github.com/yurisalesc)


## Rodando localmente

Executando com docker

```bash
  docker-compose build
```

## Testando as queries

As queries utilizadas estão no arquivo `queries.py`, para testá-las individualmente, segue abaixo.

```
docker-compose run web ./manage.py shell
```

```python
from library.queries import *

get_id_from_all_book_authors()
```

## Projetos relacionados

[Palestra do Thiago Ferreira](https://github.com/thiagoferreiraw/django-orm-optimization-talk)

## Feedback

Em breve, mais exemplos serão adicionados. Qualquer dúvida ou problema, abra uma issue neste repositório.

