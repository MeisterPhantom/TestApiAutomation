schema_get_list_pokemon_response = {
    "type": "object",
    "properties": {
        "count": {"type": "number"},
        "next": {"type": "string"},
        "previous": {"type": "string"},
        "results": {
            "type": "array",
            "name": {"type": "string"},
            "url": {"type": "string"}
        }
    }
}
