"""The Django url to handler mappings.


:Authors: Sana dev team
:Version: 2.0
"""
from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import redirect_to
from piston.resource import Resource
from sana.mds.handlers import *
from sana.mds.signals import *

concept_handler = Resource(ConceptHandler)
relationship_handler = Resource(RelationshipHandler)
relationshipcategory_handler = Resource(RelationshipCategoryHandler)
device_handler = Resource(DeviceHandler)
encounter_handler = Resource(EncounterHandler)
notification_handler = Resource(NotificationHandler)
observation_handler = Resource(ObservationHandler)
observer_handler = Resource(ObserverHandler)
procedure_handler = Resource(ProcedureHandler)
subject_handler = Resource(SubjectHandler)
requestlog_handler = Resource(RequestLogHandler)

# non-restful urls
urlpatterns = patterns(    
    '',
    url(r'^$',
        'sana.mds.views.home',
        name="mds-home"),
    
    #(r'^databrowse/(.*)', databrowse.site.root),           
)    

#patterns for REST calls
extra_patterns = patterns(
    '',
    
    # notification
    url(r'^notification/$', notification_handler, name='notification-list'),
    url(r'^notification/(?P<uuid>[^/]+)/$', notification_handler, name='notification'),
    
    # request logs
    url(r'^requestlog/$', requestlog_handler, name='requestlog-list'),
    url(r'^requestlog/(?P<uuid>[^/]+)/$', requestlog_handler, name='requestlog'),
    
    # concepts
    url(r'^concept/$', concept_handler, name='concept-list'),
    url(r'^concept/(?P<uuid>[^/]+)/$', concept_handler, name='concept'),
    
    # concept relationships
    url(r'^relationship/$', relationship_handler,name='relationship-list'),
    url(r'^relationship/(?P<uuid>[^/]+)/$', relationship_handler,name='relationship'),
    
    # concept relationship categories
    url(r'^relationshipcategory/$', relationshipcategory_handler,
        name='relationshipcategory-list'),
    url(r'^relationshipcategory/(?P<uuid>[^/]+)/$', relationshipcategory_handler,
        name='relationshipcategory'),
    
    # devices
    url(r'^device/$', device_handler, name='device-list'),
    url(r'^device/(?P<uuid>[^/]+)/$', device_handler, name='device'),
    
    # encounters
    url(r'^encounter/$', encounter_handler, name='encounter-list'),
    url(r'^encounter/(?P<uuid>[^/]+)/$', encounter_handler, name='encounter'),
    
    # observations
    url(r'^observation/$', observation_handler, name='observation-list'),
    url(r'^observation/(?P<uuid>[^/]+)/$', observation_handler, name='observation'),
    
    # observers
    url(r'^observer/$', observation_handler, name='observer-list'),
    url(r'^observer/(?P<uuid>[^/]+)/$', observer_handler, name='observer'),
    
    # procedures
    url(r'^procedure/$', procedure_handler, name='procedure-list'),
    url(r'^procedure/(?P<uuid>[^/]+)/$', procedure_handler, name='procedure'),
    
    # subjects
    url(r'^subject/$', subject_handler, name='subject-list'),
    url(r'^subject/(?P<uuid>[^/]+)/$', subject_handler, name='subject'),
    
)

# add the non-RESTful urls
urlpatterns += extra_patterns