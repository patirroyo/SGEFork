from odoo import api, models, fields, api


class Cliente(models.Model):
    _name = 'salesianos.cliente'
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    vendedor = fields.Many2one(comodel_name='salesianos.vendedor', string='vendedor') # relacion con el modelo vendedor comodel es el modelo con el que se relaciona, string es el nombre que se le da a la relacion
    

class Vendedor(models.Model):
    _name = 'salesianos.vendedor'
    name = fields.Char(required=True)
    company = fields.Char()
    fecha_incorporacion = fields.Date()
    fecha_despido = fields.Date()
    cliente = fields.One2many(comodel_name='salesianos.cliente', inverse_name='vendedor') # relacion con el modelo cliente, inverse_name es el campo que se relaciona con el modelo cliente (vendedor en este caso) y comodel_name es el modelo con el que se relaciona (cliente en este caso)
