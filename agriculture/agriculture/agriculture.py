from frappe import _

data = {
    'desktop_icons': [
        'Crop',
        'Crop Cycle',
        'Disease',
        'Fertilizer',
        'Soil Analysis',
        'Plant Analysis',
        'Water Analysis'
    ],
    'restricted_roles': [
        'Agriculture Manager',
        'Agriculture User'
    ],
    'modules': [
        'Agriculture'
    ],
    'properties': [
        {'doctype': 'Item', 'fieldname': 'is_fertilizer', 'property': 'hidden', 'value': '0'},
    ],
    'set_value': [
    ]
}
