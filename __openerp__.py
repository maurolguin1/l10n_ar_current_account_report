# -*- coding: utf-8 -*-
##############################################################################
#
#    Current Account module for OpenERP, Open Source Management Solutions.
#    Copyright (C) 2015 Latinux S.A. (<http://www.latinux.com.ar>).
#
#    This file is a part of Current Account
#
#    Current Account is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Current Account is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Current Account Reports',
    'version': '1.0',
    'depends': [
        "base",
        "account",
    ],
    'author': 'Latinux S.A.',
    'category': 'Account Modules',
    'description': """Create Current Account Report in CSV format""",
    'init_xml': [],
    'update_xml': [
        'wizard/current_account_report_view.xml'
    ],
    'demo_xml': [],
    'installable': True,
    'active': True,
}
