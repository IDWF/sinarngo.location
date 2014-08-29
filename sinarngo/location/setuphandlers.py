from collective.grok import gs
from sinarngo.location import MessageFactory as _

@gs.importstep(
    name=u'sinarngo.location', 
    title=_('sinarngo.location import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinarngo.location.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
