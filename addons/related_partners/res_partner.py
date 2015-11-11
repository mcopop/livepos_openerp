# -*- coding: utf-8 -*-
# Original file: /media/datos/openerp-dev/openerp70noalpha/openerp/addons/base/res/res_partner.py

import openerp
from openerp.osv import osv, fields
from openerp.tools.translate import _

class res_partner(osv.osv):
    _description = 'Partner'
    _name = "res.partner"
    _inherit = "res.partner"

    _columns = {
        'partner_relation_ids': fields.one2many('res.partner.relation', 'parent_id', 'Related Partner'),
    }

res_partner()

class res_partner_relation(osv.osv):
    _description = 'Partner Relationship'
    _name = "res.partner.relation"

    _columns = {
        'name': fields.char('Relationship', required=True, size=64, translate=True),
        'parent_id': fields.many2one('res.partner', 'Parent Partner', required=True),
        'partner_id': fields.many2one('res.partner', 'Child Partner', required=True),
    }

res_partner_relation()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
