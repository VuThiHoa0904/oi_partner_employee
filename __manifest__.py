# -*- coding: utf-8 -*-
{
    "name": "Contacts Employee Filter",
    "summary": "Contacts Employee Filter",
    "version": "12.0.1",
    'category': 'Human Resources',
    "website": "https://sthc.com.vn/",
	"description": """
		* add employee filter to contacts
		* Employee User/Home Address match check
		* User link to only one employee check
		* Contact link to only one employee check
		* unset default customer for employee
    """,
	'images':[
        
	],
    "author": "HTC",
    "installable": True,
    "depends": [
        'hr'
    ],
    "data": [
        'view/res_partner.xml',
        'view/hr_employee.xml',
        'view/action.xml'
    ],
    'post_init_hook' : 'post_init_hook',
    'odoo-apps' : True      
   
}

