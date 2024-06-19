# Blockbuster Project

**Authors:** Renato Laffranchi Falcão (@renatex333) & Matheus Ribeiro Barros (@MineManiac)

## Project Development

To test the API on your machine, execute the following command in the terminal:

    uvicorn sql_app.main:app --reload

Where:

- `sql_app.main`: refers to the `main.py` file located within the `sql_app` subdirectory;
- `app`: denotes the object instantiated in the `main.py` file with the line `app = FastAPI()`;
- `--reload`: enables the server to automatically reload upon detecting code changes (development mode only).

To access the API functionalities via a web browser and perform requests through a visual interface, navigate to:

- localhost:8000/docs

## Initial API Prototype

A demonstration of the API, developed using Python and the FastAPI framework without database integration, can be viewed here: [API Prototype Demo](https://youtu.be/x6H8JLdpoqA).

<img src="https://user-images.githubusercontent.com/15271557/231797556-a0293439-939a-4a3d-b3b5-3d2abbbe7420.png" width="800">

## Complete Version of the API

The RESTful API has been designed to interface with a MySQL database server, supporting full CRUD operations and providing appropriate responses to user actions. Below is the database schema used for modeling:

<img src="blockbuster_model.png" width="800">

A demonstration of the complete RESTful API, developed using Python with FastAPI and integrated with a MySQL database, is available here: [Complete API Demo](https://youtu.be/xASq6oCNMjE).

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [HTTP Status Codes](https://www.restapitutorial.com/httpstatuscodes.html)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/orm/)
