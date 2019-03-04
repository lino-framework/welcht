# -*- coding: UTF-8 -*-
# Copyright 2008-2019 Rumma & Ko Ltd
# This file is part of Lino Welfare.
#
# Lino Welfare is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Lino Welfare is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with Lino Welfare.  If not, see
# <http://www.gnu.org/licenses/>.

"""Choicelists for `lino_welcht.lib.pcsw`.

"""

from __future__ import print_function
from __future__ import unicode_literals

from lino.api import dd, _


class FollowedFORem(dd.ChoiceList):
    verbose_name = _("Followed by FORem")


add = FollowedFORem.add_item
add('0', _("No"), 'no')
add('1', _("Yes"), 'yes')
