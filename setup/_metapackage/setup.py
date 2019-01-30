import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-oca-hr",
    description="Meta package for oca-hr Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-hr_attendance_report_theoretical_time',
        'odoo10-addon-hr_attendance_rfid',
        'odoo10-addon-hr_contract_default_trial_length',
        'odoo10-addon-hr_contract_reference',
        'odoo10-addon-hr_emergency_contact',
        'odoo10-addon-hr_employee_address_improved',
        'odoo10-addon-hr_employee_age',
        'odoo10-addon-hr_employee_birth_name',
        'odoo10-addon-hr_employee_category_parent',
        'odoo10-addon-hr_employee_firstname',
        'odoo10-addon-hr_employee_id',
        'odoo10-addon-hr_employee_legacy_id',
        'odoo10-addon-hr_employee_phone_extension',
        'odoo10-addon-hr_employee_seniority',
        'odoo10-addon-hr_employee_social_media',
        'odoo10-addon-hr_expense_analytic_distribution',
        'odoo10-addon-hr_expense_invoice',
        'odoo10-addon-hr_expense_sequence',
        'odoo10-addon-hr_experience',
        'odoo10-addon-hr_family',
        'odoo10-addon-hr_holidays_compute_days',
        'odoo10-addon-hr_holidays_hour',
        'odoo10-addon-hr_holidays_imposed_days',
        'odoo10-addon-hr_holidays_leave_auto_approve',
        'odoo10-addon-hr_holidays_legal_leave',
        'odoo10-addon-hr_holidays_meeting_name',
        'odoo10-addon-hr_holidays_notify_employee_manager',
        'odoo10-addon-hr_holidays_settings',
        'odoo10-addon-hr_holidays_validity_date',
        'odoo10-addon-hr_language',
        'odoo10-addon-hr_payroll_cancel',
        'odoo10-addon-hr_payslip_change_state',
        'odoo10-addon-hr_period',
        'odoo10-addon-hr_public_holidays',
        'odoo10-addon-hr_recruitment_candidate_multi_applicant',
        'odoo10-addon-hr_recruitment_skill',
        'odoo10-addon-hr_skill',
        'odoo10-addon-hr_worked_days_from_timesheet',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
