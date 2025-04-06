get_movie_serie_doc = {
    "tags": ["Movie/Serie"],
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Token de autorização (Bearer)"
        },
        {
            "name": "page",
            "in": "query",
            "type": "integer",
            "required": False,
            "description": "Número da página para paginação"
        },
        {
            "name": "limit",
            "in": "query",
            "type": "integer",
            "required": False,
            "description": "Número de itens por página para paginação"
        },
        {
            "name": "type",
            "in": "query",
            "type": "integer",
            "required": False,
            "description": "Tipo 1 - Filme/2 - Movie/Tudo - Vazio)"
        }
    ],
    "responses": {
        200: {
            "description": "Detalhes de um único filme/série",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "release_date": {"type": "string", "format": "date"},
                    "duration": {"type": "number"},
                    "chapters": {"type": "number"},
                    "seasons": {"type": "number"},
                    "classification": {"type": "string"},
                    "synopsis": {"type": "string"},
                    "director": {"type": "string"},
                    "genre": {"type": "string"},
                    "type": {"type": "integer"},
                    "status": {"type": "boolean"},
                    "image": {"type": "string"},
                    "created_at": {"type": "string", "format": "date"},
                    "updated_at": {"type": "string", "format": "date"},
                    "average_rating": {"type": "number"}
                }
            }
        },
        401: {"description": "Token inválido ou expirado"},
        404: {"description": "Recurso não encontrado"}
    }
}

get_movie_serie_doc_by_id = {
    "tags": ["Movie/Serie"],
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Token de autorização (Bearer)"
        },
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do filme/série"
        }
    ],
    "responses": {
        200: {
            "description": "Detalhes de um único filme/série",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "release_date": {"type": "string", "format": "date"},
                    "duration": {"type": "number"},
                    "chapters": {"type": "number"},
                    "seasons": {"type": "number"},
                    "classification": {"type": "string"},
                    "synopsis": {"type": "string"},
                    "director": {"type": "string"},
                    "genre": {"type": "string"},
                    "type": {"type": "integer"},
                    "status": {"type": "boolean"},
                    "image": {"type": "string"},
                    "created_at": {"type": "string", "format": "date"},
                    "updated_at": {"type": "string", "format": "date"},
                    "average_rating": {"type": "number"}
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