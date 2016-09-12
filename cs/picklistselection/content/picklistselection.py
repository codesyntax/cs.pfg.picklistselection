from Products.CMFCore.permissions import View
"""Definition of the PickListSelection content type
"""

from zope.interface import implements
from Products.Archetypes.Widget import PicklistWidget
from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.PloneFormGen.content.fields import BaseFormField, FGLinesField
# -*- Message Factory Imported Here -*-
from Products.PloneFormGen.content.fieldsBase import *
from cs.picklistselection.interfaces import IPickListSelection
from cs.picklistselection.config import PROJECTNAME

PickListSelectionSchema = BaseFieldSchemaLinesDefault.copy() + atapi.Schema((
        vocabularyField,
        vocabularyOverrideField,
        StringField('fgFormat',
            searchable=0,
            required=0,
            default='select',
            enforceVocabulary=1,
            vocabulary='formatVocabDL',
            widget=SelectionWidget(
                label='Presentation Widget',
                ),
        ),
    ))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

PickListSelectionSchema['title'].storage = atapi.AnnotationStorage()
PickListSelectionSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(PickListSelectionSchema, moveDiscussion=False)


class PickListSelection(FGLinesField):
    """Description of the Example Type"""
    implements(IPickListSelection)

    meta_type = "PickListSelection"
    schema = PickListSelectionSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    del schema['fgFormat']
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    def __init__(self, oid, **kwargs):
        """ initialize class """

        BaseFormField.__init__(self, oid, **kwargs)

        # set a preconfigured field as an instance attribute
        self.fgField = LinesVocabularyField('fg_lines_field',
            searchable=0,
            required=0,
            write_permission = View,
            widget=PicklistWidget(),
            )

atapi.registerType(PickListSelection, PROJECTNAME)
