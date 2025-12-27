from odoo import models, fields

class ProductosStockNegativo(models.Model):
    _name = "rpt.productos_stock_negativo"
    _description = "Productos con stock negativo"
    _auto = False
    _table = "vw_productos_stock_negativo"

    id = fields.Id(string="ID", readonly=True)
    nombre = fields.Char(string="Nombre", required=True)
    categoria = fields.Char(string="Categoría", required=True)
    precio = fields.Float(string="Precio")
    stock = fields.Integer(string="Stock", required=True)
    id_proveedor = fields.Id(string="ID Proveedor")

    def print_report(self):
        """Genera el informe PDF de productos con stock negativo"""
        return self.env.ref('sge.action_productos_stock_negativo_report').report_action(self)
