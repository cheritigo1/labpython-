schema = {
    "type": "object",
    "properties": {
        "movies": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "year": {"type": "integer"},
                    "cast": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "role": {"type": "string"}
                            },
                            "required": ["name", "role"]
                        }
                    }
                },
                "required": ["title", "year", "cast"]
            }
        }
    },
    "required": ["movies"]
}
