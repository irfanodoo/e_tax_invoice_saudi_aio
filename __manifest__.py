{
    'name': 'Electronic invoice KSA - Sale, Purchase, Invoice, Credit Note',
    'version': '14.2.2.12.2021',
    'sequence':1,
    'category': 'Accounting',
    'summary': 'Electronic invoice KSA - Sale, Purchase, Invoice, Credit Note',
    
    'description': """
     Electronic invoice KSA - Sale, Purchase, Invoice, Credit Note
     Using this module you can print Saudi electronic invoice for Sale, Purchase, Invoice and  POS Order Invoice Report.
     According to Saudi Government QR code with Display Saudi Tax detials, Customer Name, Customer Vat, Invoice Date, Total of VAT, Totaol of Amount.
     """,
    "author" : "odoobridge",
    "email": 'odoobridge@gmail.com',
    "license": 'OPL-1',
    'depends': ['sale_management','purchase', 'account'],

    'data': [
        'report/vat_invoice_report_print.xml',
        'report/vat_report_action_call.xml',
        'report/vat_sale_report_print.xml',
        'report/vat_purchase_report_print.xml',
        'report/simpli_vat_invoice_report.xml',
        'report/simpli_vat_invoice_report_pos.xml',
        'views/sale_purchase_invoice_view.xml',
        # 'report/invoice_default_attach.xml',
    ],
    'price': 81,
    'currency': 'USD',
    "live_test_url" : "https://youtu.be/foB1JwMIIC8",    
    "images": ['static/description/off.gif'],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}





