from odoo import models, fields

class PedidosSinLineas(models.Model):
    _name = "rpt.pedidos_sin_lineas"
    _description = "Pedidos sin líneas"
    _auto = False
    _table = "vw_pedidos_sin_lineas"

    id = fields.Id(string="ID", readonly=True)
    id_cliente = fields.Char(string="ID Cliente", required=True)
    fecha = fields.Date(string="Fecha", required=True)
    estado = fields.Integer(string="Estado", required=True)
    importe_base = fields.Float(string="Importe base", required=True)
    descuento = fields.Float(string="Descuento", required=True)
    iva = fields.Float(string="IVA", required=True)
    importe_total = fields.Float(string="Importe total", required=True)

    def print_report(self):
        """Genera el informe PDF de pedidos sin líneas"""
        return self.env.ref('sge.action_pedidos_sin_lineas_report').report_action(self)
