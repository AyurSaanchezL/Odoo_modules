from odoo import models, fields

class FacturasVencidas(models.Model):
    _name = "rpt.facturas_vencidas"
    _description = "Pedidos sin líneas"
    _auto = False
    _table = "vw_facturas_vencidas"

    id = fields.Id(string="ID", readonly=True)
    id_pedido = fields.Id(string="ID Pedido", required=True)
    fecha_emision = fields.Date(string="Fecha de emisión", required=True)
    fecha_vencimiento = fields.Date(string="Fecha de vencimiento", required=True)
    estado_pago = fields.Integer(string="Estado del pago", required=True)

    def print_report(self):
        """Genera el informe PDF de las facturas vencidas"""
        return self.env.ref('sge.action_facturas_vencidas_report').report_action(self)
