# -*- coding: utf-8 -*-
#
# This file is part of Zenodo.
# Copyright (C) 2015 CERN.
#
# Zenodo is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Zenodo is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Zenodo; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.


"""Resolve Subject helper functions."""

import re


resolver_regexp = "\((?P<scheme>\w+)\)(?P<identifier>\S+)"


def resolve_subject(val, part):
    p = re.compile(resolver_regexp)
    m = p.search(val)
    if m:
        if part == 'identifier':
            identifier = m.group('identifier')
            if m.group('scheme') == 'gnd':
                return "gnd:{0}".format(identifier)
            return identifier
        elif part == 'scheme':
            return m.group('scheme')
        else:
            return ""
    else:
        return ""
