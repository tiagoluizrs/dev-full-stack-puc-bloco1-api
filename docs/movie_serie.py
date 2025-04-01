get_movie_serie_doc = {
    "tags": ["Movie/Serie"],
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": False,
            "description": "ID do filme/série (opcional para buscar todos)"
        },
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Token de autorização (Bearer)"
        }
    ],
    "responses": {
        200: {
            "description": "Lista de filmes/séries ou um único filme/série",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "title": {"type": "string"},
                        "release_date": {"type": "string", "format": "date"},
                        "average_rating": {"type": "number"}
                    }
                }
            }
        },
        401: {"description": "Token inválido ou expirado"},
        404: {"description": "Recurso não encontrado"}
    }
}

create_movie_serie_doc = {
    "tags": ["Movie/Serie"],
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "release_date": {"type": "string", "format": "date"},
                    "duration": {"type": "string"},
                    "chapters": {"type": "integer"},
                    "seasons": {"type": "integer"},
                    "classification": {"type": "string"},
                    "synopsis": {"type": "string"},
                    "director": {"type": "string"},
                    "genre": {"type": "string"},
                    "type": {"type": "integer"},
                    "status": {"type": "boolean"},
                    "image": {"type": "string"}
                }
            }
        },
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Token de autorização (Bearer)"
        }
    ],
    "responses": {
        201: {"description": "Filme/Série criado com sucesso"},
        401: {"description": "Token inválido ou expirado"},
        400: {"description": "Erro na criação do recurso"}
    }
}

update_movie_serie_doc = {
    "tags": ["Movie/Serie"],
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do filme/série para atualizar"
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "release_date": {"type": "string", "format": "date"},
                    "duration": {"type": "string"},
                    "chapters": {"type": "integer"},
                    "seasons": {"type": "integer"},
                    "classification": {"type": "string"},
                    "synopsis": {"type": "string"},
                    "director": {"type": "string"},
                    "genre": {"type": "string"},
                    "type": {"type": "integer"},
                    "status": {"type": "boolean"},
                    "image": {"type": "string"}
                }
            }
        },
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Token de autorização (Bearer)"
        }
    ],
    "responses": {
        200: {"description": "Filme/Série atualizado com sucesso"},
        401: {"description": "Token inválido ou expirado"},
        404: {"description": "Filme/Série não encontrado"}
    }
}

delete_movie_serie_doc = {
    "tags": ["Movie/Serie"],
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do filme/série para deletar"
        },
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Token de autorização (Bearer)"
        }
    ],
    "responses": {
        200: {"description": "Filme/Série deletado com sucesso"},
        401: {"description": "Token inválido ou expirado"},
        404: {"description": "Filme/Série não encontrado"}
    }
}