from odoo import api, models, fields


class Cliente(models.Model):
    _name = 'salesianos.cliente'
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    vendedor = fields.Many2one(comodel_name='salesianos.vendedor', string='vendedor') # relacion con el modelo vendedor comodel es el modelo con el que se relaciona, string es el nombre que se le da a la relacion
    edad = fields.Integer()
    # restricción de campos en el modelo @api.constraints añade un decorador (for record in self) cuando se crea un objeto, los datos se guardan en self -> record, en realidad no es un bucle, solo se ejecuta una vez; el registro que se está guardando en ese momento. El record es el objeto que se está guardando de la clase cliente, poniendo el .edad se accede al campo edad y si se quiere acceder a más campos hay que ponerlos en la lista, @api.constraints('edad', 'nombre', ...)
    @api.constrains('edad', 'name') 
    def _check_edad(self):
        for record in self:
            if record.edad < 18:
                raise models.ValidationError('El cliente ' + record.name + ' debe ser mayor de edad')
            elif record.edad > 100:
                raise models.ValidationError('El cliente ' + record.name + ' no puede tener mas de 100 años')
            else:
                pass

    

class Vendedor(models.Model):
    _name = 'salesianos.vendedor'
    name = fields.Char(required=True)
    company = fields.Char()
    fecha_incorporacion = fields.Date()
    fecha_despido = fields.Date()
    cliente = fields.One2many(comodel_name='salesianos.cliente', inverse_name='vendedor') # relacion con el modelo cliente, inverse_name es el campo que se relaciona con el modelo cliente (vendedor en este caso) y comodel_name es el modelo con el que se relaciona (cliente en este caso)