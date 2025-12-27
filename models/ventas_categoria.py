from odoo import models, fields


class VentasCategoria(models.Model):
    _name = "rpt.ventas_categoria"
    _description = "Productos más vendidos de cada categoría"
    _auto = False
    _table = "vw_ventas_categoria"

    id = fields.Id(string="ID", readonly=True)
    nombre = fields.Char(string="Nombre", required=True)
    categoria = fields.Char(string="Categoría", required=True)
    total_vendido = fields.Integer(string="Total vendido", required=True)
    precio_total = fields.Float(string="Precio total")

    def print_report(self):
        """Genera el informe PDF de los productos más vendidos por categoría"""
        return self.env.ref('sge.action_ventas_categoria_report').report_action(self)
