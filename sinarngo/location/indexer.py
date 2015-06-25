from plone.indexer import indexer
from DateTime import DateTime
from collective import dexteritytextindexer
from sinarngo.location.vocabulary import resolve_value
from zope.interface import Interface
from five import grok

from sinarngo.location.behavior.relatedcountries import IRelatedCountries
from Products.CMFCore.interfaces import IContentish

@indexer(IContentish)
def regions(obj):

    #FIXME These mappings should be extracted into reusable CSV files.
    #Then converted into check/lookup functions from those files.
    #http://unstats.un.org/unsd/methods/m49/m49regin.htm
    
    africa = ['DZ','AO','BJ','BW','BF','BI','CM','CV','CF','TD',
              'KM','CD','CG','DJ','EG','GQ','ER','ET','GA','GM',
              'GH','GN','GW','CI','KE','LS','LR','LY','MG','MW',
              'ML','MR','MA','MZ','NA','NE','NG','RW','ST','SN',
              'SC','SL','SO','ZA','SS','SD','SZ','TZ','TG','TN',
              'UG','ZM','ZW']

    asia = [
           #Eastern Asia
           'CN','HK','MO','KP','JP','MN','KR',
           #Southern Asia
           'AF','BD','BT','IN','IR','MV','NP','PK','LK',
           #Southeast Asia
           'BN','KH','ID','LA','MY','MM','PH','SG','TH','TL','VN',
           #West Asia
           'LB'
           ]

    oceania = ['AU','NZ','NF','FJ','NC','PG','SB','VU','GU',
               'KI','FM','NR','MP','PW','AS','CK','PF','NU',
               'PN','WS','TK','TO','TV','WF']

    europe = ['BY','BG','CZ','HU','PL','MD','RO','RU','SK','UA',
              'AX','DK','EE','FO','FI','GG','IS','IE','IM','JE',
              'LV','LT','NO','SJ','SE','UK','GB',
              'AL','AD','BA','HR','GI','GR','VA','IT','MT','ME',
              'PT','SM','RS','SI','ES','MK',
              'AT','BE','FR','DE','LI','LU''MC','NL','CH']

    latinamerica_carib = ['AI','AG','AW','BS','BB','BQ','VG',
                          'KY','CU','CW','DM','DO','GD','GP',
                          'HT','JM','MQ','MS','PR','BL','KN',
                          'LC','MF','VC','SX','TT','TC','VI',
                          'BZ','CR','SV','GT','HN','MX','NI',
                          'PA',
                          'AR','BO','BR','CL','CO','EC',
                          'FK','GF','PY','PE','SR','UY',
                          'VE']

    latinamerica = ['BZ','CR','SV','GT','HN','MX','NI',
                    'PA',
                    'AR','BO','BR','CL','CO','EC','FK',
                    'GF','GY','PY','PE','SR','UY','VE']

    northern_america = ['BM','CA','GL','PM','US']
    
    regions = []
    
    #FIXME 

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

        if '009' in regions:
            pass
        else:
            for item in obj.related_countries:
                if '009' in regions:
                    pass
                else:
                    if item in oceania:
                        regions.append('009')

        if '150' in regions:
            pass
        else:
            for item in obj.related_countries:
                if '150' in regions:
                    pass
                else:
                    if item in europe:
                        regions.append('150')

        if '419' in regions:
            pass
        else:
            for item in obj.related_countries:
                if '419' in regions:
                    pass
                else:
                    if item in latinamerica_carib:
                        regions.append('419')
        
        # code 419a below is not official UN code
        if '419a' in regions:
             pass
        else:
            for item in obj.related_countries:
                if '419a' in regions:
                     pass
                else:
                    if item in latinamerica:
                        regions.append('419a')

        if '021' in regions:
            pass
        else:
            for item in obj.related_countries:
                if '021' in regions:
                    pass
                else:
                    if item in northern_america:
                        regions.append('021')

    return regions

@indexer(IContentish)
def subregions(obj):
    
    caribbean =  ['AI','AG','AW','BS','BB','BQ','VG',
                  'KY','CU','CW','DM','DO','GD','GP',
                  'HT','JM','MQ','MS','PR','BL','KN',
                  'LC','MF','VC','SX','TT','TC','VI',
                  ]

    subregions = []

    if obj.related_countries is not None:

        if '029' in subregions:
            pass
        else:
            for item in obj.related_countries:
                if '029' in subregions:
                    pass
                else:
                    if item in caribbean:
                        subregions.append('029')

    return subregions
