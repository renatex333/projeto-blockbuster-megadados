# Blockbuster - MEGADADOS Projeto 1

## Desenvolvimento do projeto

Para testar a API na máquina, rodar o seguinte comando no terminal:

    uvicorn sql_app.main:app --reload

No qual:

- `sql_app.main`: nome do arquivo `main.py` que está no subdiretório `sql_app`;
- `app`: objeto criado dentro do arquivo `main.py` na linha `app = FastAPI()`;
- `--reload`: faz o servidor recarregar quando há mudanças (apenas para desenvolvimento).

Para acessar no WebBrowser as funcionalidades da API:

- localhost:8000/docs

## Uso [Link](https://youtu.be/x6H8JLdpoqA)

<img src="https://user-images.githubusercontent.com/15271557/231797556-a0293439-939a-4a3d-b3b5-3d2abbbe7420.png" width="800">

<!-- [`<img src="https://user-images.githubusercontent.com/15271557/231797556-a0293439-939a-4a3d-b3b5-3d2abbbe7420.png" width="800">`](https://youtu.be/x6H8JLdpoqA) -->

## Referências

[FastAPI Docs](https://fastapi.tiangolo.com/)

[Uvicorn](https://www.uvicorn.org/)

[Status Code](https://www.restapitutorial.com/httpstatuscodes.html)

[Notion - Bloco de Notas](https://juniper-condor-453.notion.site/Projeto-BlockBuster-2e755cab08d94bcb8cdefe871d6d212d)
