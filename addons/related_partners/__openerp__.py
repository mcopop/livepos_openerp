# -*- coding: utf-8 -*-
{
    "name" : "Related Partners",
    "version" : "1.0",
    "author" : "Grupo CITEC",
    "category": 'CITEC Plugins',
    'complexity': "easy",
    "description": """
CITEC Plugins - Related Partners
====================================
This modules allow to make relationships between partners

for OpenERP 7.0

Programado pelo Grupo CITEC Ltda.
v1.0
    """,
    'website': 'http://www.grupocitec.com',
    "depends" : [
    	"base", 
	],
    'init_xml': [],
    'update_xml': [
        'view/res_partner_view.xml',
    ],
    'data': [
        'security/ir.model.access.csv',
    ],
    'demo_xml': [],
    'test': [],
    'application': False,
    'installable': True,
    'css': [
    ],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
