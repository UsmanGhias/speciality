# -*- coding: utf-8 -*-
{
    'name': 'Business Specialities & Skill Qualifications',
    'version': '18.0.1.0.0',
    'category': 'Productivity',
    'summary': 'Define and manage reusable business specialities, skill domains, and partner expertise tags.',
    'description': """
Business Specialities & Skill Qualifications
============================================
Create and maintain a standardized catalog of business specialities, industry domains, and technical qualifications.

Key Features:
-------------
* Centralized business speciality catalog with unique technical codes and custom ordering
* Multi-lingual display names and descriptions
* Partner integration: tag customers, vendors, contractors, and consultants with relevant specialities
* Fast search, active/archived state management, and contact filtering by speciality
* Drag-and-drop sequence handling for priority ranking
    """,
    'author': 'CODCrafters, Usman Ghias',
    'website': 'https://usmanghias.co.uk',
    'support': 'support@codcrafters.org',
    'license': 'OPL-1',
    'price': 14.00,
    'currency': 'EUR',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/speciality_views.xml',
        'views/res_partner_views.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
