import frappe
import os
# bench --site al-khidmat.com execute akf_design.install.after_install
def after_install():
	old_file_path = "/home/frappe/frappe-alkhidmat/apps/frappe/frappe/www/login.html"
	new_file_path = "/home/frappe/frappe-alkhidmat/apps/frappe/frappe/www/login_stop.html"
	try:
		os.rename(old_file_path, new_file_path)
		print(f"File renamed from '{old_file_path}' to '{new_file_path}'")
	except FileNotFoundError:
		print(f"Error: File not found at '{old_file_path}'")
	except Exception as e:
		print(f"An error occurred: {e}")