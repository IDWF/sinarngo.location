from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from sinarngo.location import MessageFactory as _

class IRelatedCountries(form.Schema):
    """
       Marker/Form interface for Related Countries
    """

    # -*- Your Zope schema definitions here ... -*-

    related_countries = schema.List(
            title=_(u'Related Countries'),
            value_type = schema.Choice(
                vocabulary="ploneun.vocabulary.country",
                ),
            required=False,
            )

alsoProvides(IRelatedCountries,IFormFieldProvider)
