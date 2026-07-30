# -*- coding: utf-8 -*-
{
    "name": "Speciality",
    "version": "18.0.1.0.0",
    "category": "Productivity",
    "summary": "Reusable management of business specialities",
    "description": """
Speciality
==========

Standalone Odoo 18 module for creating and managing a reusable list of
business specialities (name, code, sequence, active flag, description).

This first release intentionally remains standalone and does not attach
specialities to employees, partners, or products.
    """,
    "author": "UsmanGhias",
    "website": "https://github.com/UsmanGhias/speciality",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/speciality_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
