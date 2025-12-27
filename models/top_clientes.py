from odoo import models, fields


class TopClientes(models.Model):
    _name = "rpt.top_10_clientes"
    _description = "Top 10 clientes"
    _auto = False
    _table = "vw_top_clientes"

    id = fields.Id(string="ID", readonly=True)
    nombre = fields.Char(string="Nombre", required=True)
    apellido1 = fields.Char(string="Primer Apellido", required=True)
    apellido2 = fields.Char(string="Segundo Apellido")
    email = fields.Char(string="Email", required=True)
    telefono = fields.Char(string="Teléfono")
    pais = fields.Char(string="País")
    fecha_alta = fields.Date(string="Fecha de Alta")
    total_gastado = fields.Float(string="Total gastado")

    def print_report(self):
        """Genera el informe PDF de clientes con pedidos abiertos"""
        return self.env.ref('sge.action_top_clientes_report').report_action(self)
