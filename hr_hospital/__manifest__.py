# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """
        Hospital System""",

    'description': """
        Hospital System
    """,

    'author': "Dmytro Stopchak",
    'category': 'Uncategorized',
    'version': '15.0.1.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menus.xml',
        'views/contact_person_views.xml',
        'views/disease_type_views.xml',
        'views/doctor_views.xml',
        'views/patient_study_views.xml',
        'views/personal_doctor_history_views.xml',
        'views/study_type_views.xml',
        'views/diagnosis_views.xml',
        'views/disease_views.xml',
        'views/hr_hospital_menus.xml',
        'views/patient_views.xml',
        'views/sample_type_views.xml',
        'views/visit_views.xml',
        'data/hr_hospital_data.xml',
        'wizard/set_personal_doctor_view.xml'
    ],

    # only loaded in demonstration mode
    'demo': [],
    'application': True,
    'license': 'LGPL-3',
}
