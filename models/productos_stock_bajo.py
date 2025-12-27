from odoo import models, fields

class ProductosBajoStock(models.Model):
    _name = "rpt.productos_stock_bajo"
    _description = "Productos con stock bajo"
    _auto = False
    _table = "vw_productos_stock_bajo"

    id = fields.Id(string="ID", readonly=True)
    nombre = fields.Char(string="Nombre", required=True)
    categoria = fields.Char(string="Categoría", required=True)
    precio = fields.Float(string="Precio")
    stock = fields.Integer(string="Stock", required=True)
    id_proveedor = fields.Id(string="ID Proveedor")

    def print_report(self):
        """Genera el informe PDF de productos con stock bajo"""
        return self.env.ref('sge.action_productos_stock_bajo_report').report_action(self)
