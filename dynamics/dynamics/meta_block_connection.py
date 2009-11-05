#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard Lincoln
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANDABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" 
"""

# <<< imports
# @generated
from dynamics.element import Element



from google.appengine.ext import db
# >>> imports

class MetaBlockConnection(Element):
    # <<< meta_block_connection.attributes
    # @generated
    # Used for standard connection situations where multiple blocks of same class or same MetaBlock::blockkind have to be connected. The slotnames used are defined in the Reference Manual for Exchanging Standard Power System Dynamic Models. Application: Cross-compound or Combined Cycle connections. 
    slotname = db.StringProperty()

    # >>> meta_block_connection.attributes

    # <<< meta_block_connection.references
    # @generated
    # >>> meta_block_connection.references

    # <<< meta_block_connection.operations
    # @generated
    # >>> meta_block_connection.operations

# EOF -------------------------------------------------------------------------
