import frappe
import os
# bench --site al-khidmat.com execute akf_design.install.after_install
def after_uninstall():
	old_file_path = "/home/frappe/frappe-bench/apps/frappe/frappe/www/login.html"
	new_file_path = "/home/frappe/frappe-bench/apps/frappe/frappe/www/login_stop.html"
	try:
		os.rename(new_file_path, old_file_path)
		print(f"File renamed from '{new_file_path}' to '{old_file_path}'")
	except FileNotFoundError:
		print(f"Error: File not found at '{old_file_path}'")
	except Exception as e:
		print(f"An error occurred: {e}")