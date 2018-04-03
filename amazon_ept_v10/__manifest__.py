{
    'name': 'Amazon Odoo Connector',
    'version': '10.0',
    'category': 'Sales',
    'summary' : 'Integrate & Manage your all your Amazon seller account operations from Odoo',
    'author': 'Emipro Technologies Pvt. Ltd.',
    'website': 'http://www.emiprotechnologies.com/',
    'maintainer': 'Emipro Technologies Pvt. Ltd.',
    'depends': ['auto_invoice_workflow_ept', 'delivery', 'web','sale_stock'],
    'data': [
             'security/res_groups.xml',
             'security/ir.model.access.csv',
             'view/res_config_view.xml',
             'view/product_brand_view.xml',
             'view/base_browse_node.xml',
             'view/browse_node.xml',
             'view/product_view.xml',
             'view/process_import_export.xml',
             'view/sales_view.xml',
             'report/sale_report_view.xml',
             'view/order_refund_view.xml',
             'view/stock_view.xml',
             'view/invoice_view.xml',
             'view/feed_submission_history.xml',
             'view/amazon_file_process_job.xml',
             'view/amazon_report_wizard.xml',             
             'view/amazon_seller.xml',
             'view/instance_view.xml',                                                
             'view/auto_work_flow_configuration.xml',
             'view/tax_code_view.xml',
             'view/ir_cron.xml',             
             'view/product_wizard_view.xml',
             'view/cancel_order_wizard_view.xml',
             'view/res_country.xml',
             'view/web_templates.xml',
             'view/stock_quant_package.xml',
             'view/stock_warehouse.xml',
             'view/settlement_report.xml',             
             'view/amazon_transaction.xml',      
             'view/delivery.xml',
             'view/active_product_listing_view.xml',
             'view/account_fiscal_position.xml',
             'view/amazon_category.xml',
             'view/amazon_category_data.xml',
             'view/product_attribute.xml',
             'view/ir_sequence.xml',
             'view/sale_order_report_view.xml',             
             'data/amazon.base.browse.node.ept.csv',
             'data/amazon.uom.type.ept.csv',
             'data/amazon.uom.value.ept.csv',             
             'data/amazon.attribute.ept.csv',
             'data/amazon.attribute.value.ept.csv',
             'data/amazon.tax.code.ept.csv',
             'data/amazon.cspia.warning.ept.csv',
             'data/amazon.payment.type.option.ept.csv',
             'data/amazon.tsd.language.ept.csv',
             'data/amazon.tsd.warning.ept.csv',
             'data/amazon.variation.theme.ept.csv',
             'data/amazon.transaction.type.csv',
             'licence/renew_amazon_app.xml',
             ],
    'description': """

    """,
    'images': ['static/description/main_screen.jpeg'],
    'installable': True,
    'auto_install': False,
    'live_test_url':'https://shop.emiprotechnologies.com/amazon-odoo-connector.html',
    'application' : True,
    'price': 450.00,
    'currency': 'EUR',
}