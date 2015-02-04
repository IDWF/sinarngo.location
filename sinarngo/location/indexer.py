from plone.indexer import indexer
from DateTime import DateTime
from collective import dexteritytextindexer
from sinarngo.location.vocabulary import resolve_value
from zope.interface import Interface
from five import grok

from sinarngo.location.behavior.relatedcountries import \
IRelatedCountries
from Products.CMFCore.interfaces import IContentish

@indexer(IContentish)
def regions(obj):

    africa = ['DZ','AO','BJ','BW','BF','BI','CM','CV','CF','TD',
              'KM','CD','CG','DJ','EG','GQ','ER','ET','GA','GM',
              'GH','GN','GW','CI','KE','LS','LR','LY','MG','MW',
              'ML','MR','MA','MZ','NA','NE','NG','RW','ST','SN',
              'SC','SL','SO','ZA','SS','SD','SZ','TZ','TG','TN',
              'UG','ZM','ZW']

    #FIXME Pacific needs to be extracted out.

    asia = ['AF','BD','BT','KH','CN','KP','ID','IN','IR',
            'LA','MY','MV','MN','MM','NP','PK','PH',
            'LK','TH','TL','VN']


    latinamerica_carib = ['AI','AG','AW','BS','BB','BQ','VG',
                          'KY','CU','CW','DM','DO','GD','GP',
                          'HT','JM','MQ','MS','PR','BL','KN',
                          'LC','MF','VC','SX','TT','TC','VI']

    #FIXME Needs rest of latin america

    regions = []
    
    #FIXME really should be rewritten better

    if obj.related_countries is not None:

        if '002' in regions:
            pass
        else: 
            for item in obj.related_countries:
                if '002' in regions:
                    pass
                else:
                    if item in africa:
                        regions.append('002')

        if '142' in regions:
            pass
        else:
            for item in obj.related_countries:
                if '142' in regions:
                    pass
                else:
                    if item in asia:
                        regions.append('142')

        if '419' in regions:
            pass
        else:
            for item in obj.related_countries:
                if '419' in regions:
                    pass
                else:
                    if item in latinamerica_carib:
                        regions.append('419')


    return regions

