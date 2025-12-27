from odoo import models, fields


class ClientesPedidosAbiertos(models.Model):
    _name = "rpt.clientes_pedidos_abiertos"
    _description = "Clientes con pedidos abiertos"
    _auto = False
    _table = "vw_clientes_pedidos_abiertos"

    id = fields.Id(string="ID", readonly=True)
    nombre = fields.Char(string="Nombre", required=True)
    apellido1 = fields.Char(string="Primer Apellido", required=True)
    apellido2 = fields.Char(string="Segundo Apellido")
    email = fields.Char(string="Email", required=True)
    telefono = fields.Char(string="Teléfono")
    pais = fields.Char(string="País")
    fecha_alta = fields.Date(string="Fecha de Alta")
    pedidos_abiertos = fields.Integer(string="Pedidos abiertos")

    def print_report(self):
        """Genera el informe PDF de clientes con pedidos abiertos"""
        return self.env.ref('sge.action_clientes_p_abiertos_report').report_action(self)
