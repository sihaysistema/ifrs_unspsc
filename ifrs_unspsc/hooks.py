# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ifrs_unspsc"
app_title = "IFRS_UNSPSC"
app_publisher = "Si Hay Sistema"
app_description = "IFRS Accounts and UNSPSC Item Groups"
app_icon = "octicon octicon-list-ordered"
app_color = "#862F2D"
app_email = "alainber@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ifrs_unspsc/css/ifrs_unspsc.css"
# app_include_js = "/assets/ifrs_unspsc/js/ifrs_unspsc.js"

# include js, css files in header of web template
# web_include_css = "/assets/ifrs_unspsc/css/ifrs_unspsc.css"
# web_include_js = "/assets/ifrs_unspsc/js/ifrs_unspsc.js"

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

# Website user home page (by function)
# get_website_user_home_page = "ifrs_unspsc.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ifrs_unspsc.install.before_install"
# after_install = "ifrs_unspsc.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ifrs_unspsc.notifications.get_notification_config"

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
# 		"ifrs_unspsc.tasks.all"
# 	],
# 	"daily": [
# 		"ifrs_unspsc.tasks.daily"
# 	],
# 	"hourly": [
# 		"ifrs_unspsc.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ifrs_unspsc.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ifrs_unspsc.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ifrs_unspsc.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ifrs_unspsc.event.get_events"
# }

