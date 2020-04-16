plainte_insert_schema = {
    'type': 'object',
    'required': ['id','etablissement', 'adresse', 'ville', 'date_visite', 'prenom', 'nom','description'],
    'properties': {
		'id': {
            'type': 'number'
        },
        'etablissement': {
            'type': 'string'
        },
        'adresse': {
            'type': 'string'
        },
        'ville': {
            'type': 'string'
        },
		'date_visite': {
            'type': 'string'
        },
        'prenom': {
            'type': 'string'
        },
        'nom': {
            'type': 'string'
        },
		'description': {
            'type': 'string'
        }
    },
    'additionalProperties': False
}
