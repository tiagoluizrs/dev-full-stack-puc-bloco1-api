rating_doc = {
    "tags": ["Rating"],
    "security": [{"BearerAuth": []}],  # Define que é necessário o token
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do filme/série para avaliar"
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "user_id": {"type": "integer"},
                    "rating": {"type": "integer"}
                }
            }
        },
        {
            "name": "Authorization",  # Cabeçalho do token
            "in": "header",
            "type": "string",
            "required": True,
            "description": "Token de autorização (Bearer)"
        }
    ],
    "responses": {
        200: {"description": "Avaliação realizada com sucesso"},
        401: {"description": "Token inválido ou expirado"},
        404: {"description": "Filme/Série ou usuário não encontrado"}
    }
}