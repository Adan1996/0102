# -*- coding: utf-8 -*-
{
    'name': "Booking Services",

    'summary': """
        Booking Services Test""",

    'description': """
        To allow users to create bookings for employees and equipments
    """,

    'author': "Syahdan Masyhuri",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'product',
        'stock',
        'event'
        ],

    # always loaded
    'data': [
        'views/menu.xml',
        'views/booking_orders.xml',
        'views/teams.xml',
        'views/product_template.xml',
        'views/calendar_events.xml',
        'views/events.xml',
        'views/serial_number.xml',
        'views/is_a_booking.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}