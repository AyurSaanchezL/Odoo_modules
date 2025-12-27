from odoo import models, fields


class VentasMes(models.Model):
    _name = "rpt.ventas_mes"
    _description = "Productos más vendidos de cada categoría"
    _auto = False
    _table = "vw_ventas_mes"

    id = fields.Id(string="ID", readonly=True)
    mes = fields.Integer(string="Mes", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    total_vendido = fields.Integer(string="Total vendido", required=True)
    precio_total = fields.Float(string="Precio total")

    def print_report(self):
        """Genera el informe PDF de los productos más vendidos por categoría"""
        return self.env.ref('sge.action_ventas_mes_report').report_action(self)
