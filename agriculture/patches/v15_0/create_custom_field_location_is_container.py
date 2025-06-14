import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def execute():
	create_custom_fields(
		{
			"Location": [
				{
					"default": "0",
					"description": "Check if it is a hydroponic unit",
					"fieldname": "is_container",
					"fieldtype": "Check",
					"label": "Is Container"
					"insert_after": "cb_details",
				},
			]
		},
		ignore_validate=True,
	)
