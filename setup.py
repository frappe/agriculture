from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in agriculture/__init__.py
from agriculture import __version__ as version

setup(
	name="agriculture",
	version=version,
	description="Agriculture",
	author="Frappe",
	author_email="pandikunta@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
