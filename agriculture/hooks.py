from . import __version__ as app_version

app_name = "agriculture"
app_title = "Agriculture"
app_publisher = "Frappe"
app_description = "Agriculture"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "pandikunta@frappe.io"
app_license = "MIT"


required_apps = ["erpnext"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/agriculture/css/agriculture.css"
# app_include_js = "/assets/agriculture/js/agriculture.js"

# include js, css files in header of web template
# web_include_css = "/assets/agriculture/css/agriculture.css"
# web_include_js = "/assets/agriculture/js/agriculture.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "agriculture/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "agriculture.utils.jinja_methods",
# 	"filters": "agriculture.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "agriculture.install.before_install"
# after_install = "agriculture.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "agriculture.uninstall.before_uninstall"
# after_uninstall = "agriculture.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "agriculture.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"agriculture.tasks.all"
# 	],
# 	"daily": [
# 		"agriculture.tasks.daily"
# 	],
# 	"hourly": [
# 		"agriculture.tasks.hourly"
# 	],
# 	"weekly": [
# 		"agriculture.tasks.weekly"
# 	],
# 	"monthly": [
# 		"agriculture.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "agriculture.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "agriculture.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "agriculture.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"agriculture.auth.validate"
# ]

global_search_doctypes = {
	"Agriculture": [
		{'doctype': 'Weather', 'index': 1},
		{'doctype': 'Soil Texture', 'index': 2},
		{'doctype': 'Water Analysis', 'index': 3},
		{'doctype': 'Soil Analysis', 'index': 4},
		{'doctype': 'Plant Analysis', 'index': 5},
		{'doctype': 'Agriculture Analysis Criteria', 'index': 6},
		{'doctype': 'Disease', 'index': 7},
		{'doctype': 'Crop', 'index': 8},
		{'doctype': 'Fertilizer', 'index': 9},
		{'doctype': 'Crop Cycle', 'index': 10}
	]
}

domains = {
	'Agriculture': 'agriculture.agriculture.agriculture',
}

