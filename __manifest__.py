{
    'name': 'Informes y Consultas SGE',
    'version': '1.0',
    'author': 'Ayur Sánchez Lozano',
    'category': 'Reporting',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',

        'views/clientes_pedidos_abiertos_view.xml',
        'views/ventas_categoria_view.xml',
        'views/ventas_mes_view.xml',
        'views/top_clientes_view.xml',
        'views/productos_stock_bajo_view.xml',
        'views/productos_stock_negativo_view.xml',
        'views/pedidos_sin_lineas_view.xml',
        'views/facturas_vencidas_view.xml',

        'views/menu.xml',

        'report/ventas_categoria_report_action.xml',
        'report/ventas_categoria_report_template.xml',
        'report/ventas_mes_report_action.xml',
        'report/ventas_mes_report_template.xml',

        'report/facturas_vencidas_report_action.xml',
        'report/facturas_vencidas_report_template.xml',

        'report/pedidos_sin_lineas_report_action.xml',
        'report/pedidos_sin_lineas_report_template.xml',

        'report/productos_stock_bajo_report_action.xml',
        'report/productos_stock_bajo_report_template.xml',
        'report/productos_stock_negativo_report_action.xml',
        'report/productos_stock_negativo_report_template.xml',

        'report/top_clientes_report_action.xml',
        'report/top_clientes_report_template.xml',
        'report/clientes_pedidos_abiertos_report_action.xml',
        'report/clientes_pedidos_abiertos_report_template.xml',
    ],
    'installable': True,
}
