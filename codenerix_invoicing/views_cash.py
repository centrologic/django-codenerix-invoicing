# -*- coding: utf-8 -*-
#
# django-codenerix-pos
#
# Copyright 2017 Centrologic Computational Logistic Center S.L.
#
# Project URL : http://www.codenerix.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import IntegrityError
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.forms.utils import ErrorList
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic import View

from codenerix.middleware import get_current_user

from codenerix.views import GenList, GenCreate, GenCreateModal, GenUpdate, GenUpdateModal, GenDelete, GenDetail, GenDetailModal

from .models_cash import CashDiary, CashMovement
from .forms_cash import CashDiaryForm, CashMovementForm


# ###########################################
# CashDiary
class CashDiaryList(GenList):
    model = CashDiary
    show_details = True
    extra_context = {'menu': ['accounting', 'cashdiary'], 'bread': [_('Accounting'), _('CashDiary')]}
    default_ordering = "-opened_date"


class CashDiaryCreate(GenCreate):
    model = CashDiary
    show_details = True
    form_class = CashDiaryForm
    hide_foreignkey_button = True

    def form_valid(self, form):
        try:
            return super(CashDiaryCreate, self).form_valid(form)
        except IntegrityError as e:
            errors = form._errors.setdefault("other", ErrorList())
            errors.append(e)
            return super(CashDiaryCreate, self).form_invalid(form)


class CashDiaryCreateModal(GenCreateModal, CashDiaryCreate):
    pass


class CashDiaryUpdate(GenUpdate):
    model = CashDiary
    show_details = True
    form_class = CashDiaryForm
    hide_foreignkey_button = True

    def form_valid(self, form):
        try:
            return super(CashDiaryUpdate, self).form_valid(form)
        except IntegrityError as e:
            errors = form._errors.setdefault("other", ErrorList())
            errors.append(e)
            return super(CashDiaryUpdate, self).form_invalid(form)


class CashDiaryUpdateModal(GenUpdateModal, CashDiaryUpdate):
    pass


class CashDiaryDelete(GenDelete):
    model = CashDiary


class CashDiarySubList(GenList):
    model = CashDiary
    show_details = False
    extra_context = {'menu': ['accounting', 'cashdiary'], 'bread': [_('Accounting'), _('CashDiary')]}

    def __limitQ__(self, info):
        limit = {}
        pk = info.kwargs.get('pk', None)
        limit['link'] = Q(pos__pk=pk)
        return limit


class CashDiaryDetails(GenDetail):
    model = CashDiary
    groups = CashDiaryForm.__groups_details__()
    tabs = [
        {'id': 'CashMovement', 'name': _('Cash movement'), 'ws': 'CDNX_invoicing_cashmovements_sublist', 'rows': 'base'},
    ]


class CashDiaryDetailModal(GenDetailModal, CashDiaryDetails):
    pass


# ###########################################
# CashMovement
class CashMovementList(GenList):
    model = CashMovement
    show_details = True
    extra_context = {'menu': ['accounting', 'CashMovement'], 'bread': [_('Accounting'), _('CashMovement')]}
    default_ordering = "-date_movement"


class CashMovementReport(View):
    template_name = 'accounting/CashMovement_report.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        # Initialization
        context = {}
        context['menu'] = ('billing', 'CashMovementreport')
        context['bread'] = (_('Billing'), _('Cash Diary Report'))
        context['datas'] = []

        # Orders
        tickets = []
        tickets.append({
            'id': 'last7d',
            'title': _('Ultimos 7 dias'),
            # 'rows': [(x.user, x.order, x.amount) for x in CashMovement.objects.all()[:7]],
            'rows': [
                ('Hoy', 35, 498.4),
                ('Domingo', 32, 305.1),
                ('Sabado', 49, 622.3),
                ('Viernes', 45, 599.1),
                ('Jueves', 15, 115.4),
                ('Miercoles', 28, 324.3),
                ('Martes', 23, 316.7),
                ('Lunes', 15, 116.7),
                ],
        })
        tickets.append({
            'id': 'last4w',
            'title': _('Ultimas 4 semanas'),
            # 'rows': [(x.user, x.order, x.amount) for x in CashMovement.objects.all()[:4]],
            'rows': [
                ('Esta semana', 12, 125.22),
                ('Hace 1 semana', 298, 3245.88),
                ('Hace 2 semanas', 1884, 23125.43),
                ('Hace 3 semanas', 578, 6325.33),
                ('Hace 4 semanas', 778, 7145.49),
            ],
        })
        tickets.append({
            'id': 'last3m',
            'title': _('Ultimos 3 meses'),
            # 'rows': [(x.user, x.order, x.amount) for x in CashMovement.objects.all()[:3]],
            'rows': [
                ('Este mes', 139, 1842.52),
                ('Agosto', 1239, 12842.33),
                ('Julio', 439, 9842.74),
                ('Junio', 1839, 13842.14),
            ],
        })
        context['datas'].append({
            'title': _('Tickets'),
            'id': 'order',
            'columns': [_('Day'), _('Tickets'), _('Amount')],
            'graph': (0, 2),
            'lasts': tickets,
        })

        # People
        people = []
        people.append({
            'id': 'last7d',
            'title': _('Last 7 days'),
            'rows': [(x.user, x.order, x.amount) for x in CashMovement.objects.all()[:7]],
        })
        people.append({
            'id': 'last4w',
            'title': _('Last 4 weeks'),
            'rows': [(x.user, x.order, x.amount) for x in CashMovement.objects.all()[:4]],
        })
        people.append({
            'id': 'last3m',
            'title': _('Last 3 months'),
            'rows': [(x.user, x.order, x.amount) for x in CashMovement.objects.all()[:3]],
        })
        context['datas'].append({
            'title': _('People'),
            'id': 'person',
            'columns': [_('User'), _('Order'), _('Amount')],
            'graph': (0, 2),
            'lasts': people,
        })

        # Por hacer
        # 1: Tickets vendidos en el tiempo$
        # 2: Tickets vendidos por persona en el tiempo$
        # 3: Tickets cancelados en el tiempo$
        # 4: Tickets cancelados por persona en el tiempo$
        # --------------------
        # 5: Facturas en el tiempo
        # 6: Facturas por persona en el tiempo
        # --------------------
        # 7: Pedidos en el tiempo
        # 8: Pedidos por persona en el tiempo
        # --------------------
        # 9:  Motivos en el tiempo
        # 10: Motivos por persona en el tiempo

        # Render
        return render(request, self.template_name, context)


class CashMovementCreate(GenCreate):
    model = CashMovement
    show_details = True
    form_class = CashMovementForm
    hide_foreignkey_button = True

    def form_valid(self, form):
        user = get_current_user()
        form.instance.user = user
        self.request.user = user

        return super(CashMovementCreate, self).form_valid(form)


class CashMovementCreateModal(GenCreateModal, CashMovementCreate):
    pass


class CashMovementUpdate(GenUpdate):
    model = CashMovement
    show_details = True
    form_class = CashMovementForm
    hide_foreignkey_button = True


class CashMovementUpdateModal(GenUpdateModal, CashMovementUpdate):
    pass


class CashMovementDelete(GenDelete):
    model = CashMovement


class CashMovementSubList(GenList):
    model = CashMovement
    show_details = False
    extra_context = {'menu': ['accounting', 'CashMovement'], 'bread': [_('Accounting'), _('CashMovement')]}

    def __limitQ__(self, info):
        limit = {}
        pk = info.kwargs.get('pk', None)
        limit['link'] = Q(cash_diary__pk=pk)
        return limit


class CashMovementDetails(GenDetail):
    model = CashMovement
    groups = CashMovementForm.__groups_details__()
    """
    tabs = [
        {'id': 'CashMovementDay', 'name': _('CashMovement day'), 'ws': 'CashMovements_sublist', 'rows': 'base'},
    ]
    """


class CashMovementDetailModal(GenDetailModal, CashMovementDetails):
    pass