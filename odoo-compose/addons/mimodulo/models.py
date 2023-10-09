from odoo import models, fields, api

class ventas(models.Model):
    _name = 'ventas_cole.ventas' # nombre del modelo y crea la tabla ventas_cole.ventas
    _description = 'ventas_cole.ventas'

    name = fields.Char() #la api de fields es para crear los campos, asi de facil
    descripcion = fields.Char()
    precio = fields.Integer()
    cantidad = fields.Integer()
    total = fields.Integer()
    cliente = fields.Char()
    vendedor = fields.Many2one('ventas_cole.vendedores')#un vendedor puede tener muchas ventas, para ello se usa el many2one
    factura = fields.Char()
    fecha = fields.Date()
    total_con_decimales = fields.Float()

class vendedores(models.Model):
    _name = 'ventas_cole.vendedores'
    _description = 'ventas_cole.vendedores'

    name = fields.Char()
    apellido = fields.Char()
    dni = fields.Char()
    ventas = fields.One2many('ventas_cole.ventas', 'vendedor')#un vendedor puede tener muchas ventas, para ello se usa el one2many

