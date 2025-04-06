register_doc = {
    "tags": ["Autenticação"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "email": {"type": "string"},
                    "password": {"type": "string"}
                }
            }
        }
    ],
    "responses": {
        201: {
            "description": "Usuário criado com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string"},
                    "created_at": {"type": "string", "format": "date"},
                    "updated_at": {"type": "string", "format": "date"},
                }
            }
        },
        400: {"description": "Usuário já existe"},
        404: {"description": "Erro ao processar a solicitação"}
    }
}

login_doc = {
    "tags": ["Autenticação"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "email": {"type": "string"},
                    "password": {"type": "string"}
                }
            }
        }
    ],
    "responses": {
        200: {
            "description": "Login realizado com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "user": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "email": {"type": "string"},
                            "created_at": {"type": "string", "format": "date"},
                            "updated_at": {"type": "string", "format": "date"},
                        }
                    },
                    "token": {"type": "string"}
                }
            }
        },
        404: {"description": "Usuário não encontrado"}
    }
}