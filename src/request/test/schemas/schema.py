schema_get_list_neo_response = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "links": {
                "type": "object",
                "properties": {
                    "next": {
                        "type": "string"
                    },
                    "previous": {
                        "type": "string"
                    },
                    "self": {
                        "type": "string"
                    }
                },
                "required": [
                    "next",
                    "previous",
                    "self"
                ]
            },
            "element_count": {
                "type": "integer"
            },
            "near_earth_objects": {
                "type": "object",
                "properties": {
                    "2015-09-08": {
                        "type": "array",
                        "items": [
                            {
                                "type": "object",
                                "properties": {
                                    "links": {
                                        "type": "object",
                                        "properties": {
                                            "self": {
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "self"
                                        ]
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "neo_reference_id": {
                                        "type": "string"
                                    },
                                    "name": {
                                        "type": "string"
                                    },
                                    "nasa_jpl_url": {
                                        "type": "string"
                                    },
                                    "absolute_magnitude_h": {
                                        "type": "number"
                                    },
                                    "estimated_diameter": {
                                        "type": "object",
                                        "properties": {
                                            "kilometers": {
                                                "type": "object",
                                                "properties": {
                                                    "estimated_diameter_min": {
                                                        "type": "number"
                                                    },
                                                    "estimated_diameter_max": {
                                                        "type": "number"
                                                    }
                                                },
                                                "required": [
                                                    "estimated_diameter_min",
                                                    "estimated_diameter_max"
                                                ]
                                            },
                                            "meters": {
                                                "type": "object",
                                                "properties": {
                                                    "estimated_diameter_min": {
                                                        "type": "number"
                                                    },
                                                    "estimated_diameter_max": {
                                                        "type": "number"
                                                    }
                                                },
                                                "required": [
                                                    "estimated_diameter_min",
                                                    "estimated_diameter_max"
                                                ]
                                            },
                                            "miles": {
                                                "type": "object",
                                                "properties": {
                                                    "estimated_diameter_min": {
                                                        "type": "number"
                                                    },
                                                    "estimated_diameter_max": {
                                                        "type": "number"
                                                    }
                                                },
                                                "required": [
                                                    "estimated_diameter_min",
                                                    "estimated_diameter_max"
                                                ]
                                            },
                                            "feet": {
                                                "type": "object",
                                                "properties": {
                                                    "estimated_diameter_min": {
                                                        "type": "number"
                                                    },
                                                    "estimated_diameter_max": {
                                                        "type": "number"
                                                    }
                                                },
                                                "required": [
                                                    "estimated_diameter_min",
                                                    "estimated_diameter_max"
                                                ]
                                            }
                                        },
                                        "required": [
                                            "kilometers",
                                            "meters",
                                            "miles",
                                            "feet"
                                        ]
                                    },
                                    "is_potentially_hazardous_asteroid": {
                                        "type": "boolean"
                                    },
                                    "close_approach_data": {
                                        "type": "array",
                                        "items": [
                                            {
                                                "type": "object",
                                                "properties": {
                                                    "close_approach_date": {
                                                        "type": "string"
                                                    },
                                                    "close_approach_date_full": {
                                                        "type": "string"
                                                    },
                                                    "epoch_date_close_approach": {
                                                        "type": "integer"
                                                    },
                                                    "relative_velocity": {
                                                        "type": "object",
                                                        "properties": {
                                                            "kilometers_per_second": {
                                                                "type": "string"
                                                            },
                                                            "kilometers_per_hour": {
                                                                "type": "string"
                                                            },
                                                            "miles_per_hour": {
                                                                "type": "string"
                                                            }
                                                        },
                                                        "required": [
                                                            "kilometers_per_second",
                                                            "kilometers_per_hour",
                                                            "miles_per_hour"
                                                        ]
                                                    },
                                                    "miss_distance": {
                                                        "type": "object",
                                                        "properties": {
                                                            "astronomical": {
                                                                "type": "string"
                                                            },
                                                            "lunar": {
                                                                "type": "string"
                                                            },
                                                            "kilometers": {
                                                                "type": "string"
                                                            },
                                                            "miles": {
                                                                "type": "string"
                                                            }
                                                        },
                                                        "required": [
                                                            "astronomical",
                                                            "lunar",
                                                            "kilometers",
                                                            "miles"
                                                        ]
                                                    },
                                                    "orbiting_body": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "close_approach_date",
                                                    "close_approach_date_full",
                                                    "epoch_date_close_approach",
                                                    "relative_velocity",
                                                    "miss_distance",
                                                    "orbiting_body"
                                                ]
                                            }
                                        ]
                                    },
                                    "is_sentry_object": {
                                        "type": "boolean"
                                    }
                                },
                                "required": [
                                    "links",
                                    "id",
                                    "neo_reference_id",
                                    "name",
                                    "nasa_jpl_url",
                                    "absolute_magnitude_h",
                                    "estimated_diameter",
                                    "is_potentially_hazardous_asteroid",
                                    "close_approach_data",
                                    "is_sentry_object"
                                ]
                            }
                        ]
                    }
                },
                "required": [
                    "2015-09-08"
                ]
            }
        },
        "required": [
            "links",
            "element_count",
            "near_earth_objects"
        ]
    }
