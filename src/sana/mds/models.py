'''
Created on Aug 7, 2012

@author: Sana Dev Team
'''
from django.db import models

from sana.core.models.concept import Concept as BaseConcept
from sana.core.models.concept import Relationship as BaseRelationship
from sana.core.models.concept import Relationship as BaseRelationshipCategory
from sana.core.models.device import Device as BaseDevice
from sana.core.models.encounter import Encounter  as BaseEncounter
from sana.core.models.notification import Notification as BaseNotification
from sana.core.models.observation import Observation  as BaseObservation
from sana.core.models.observer import Observer as BaseObserver
from sana.core.models.procedure import Procedure as BaseProcedure
from sana.core.models.requestlog import RequestLog as BaseRequestLog
from sana.core.models.subject import Subject as BaseSubject

__all__ = ['Concept', 'Relationship','RelationshipCategory',
           'Device', 
           'Encounter', 
           'Notification',
           'Observation', 
           'Observer',
           'Procedure',
           'RequestLog',
           'Subject',]

class Concept(BaseConcept):
    parent_ptr = models.OneToOneField(BaseConcept, parent_link=True,
                             related_name="%(app_label)s_%(class)s_related")


class Relationship(BaseRelationship):
    parent_ptr = models.OneToOneField(BaseRelationship, parent_link=True,
                             related_name="%(app_label)s_%(class)s_related")


class RelationshipCategory(BaseRelationshipCategory):
    parent_ptr = models.OneToOneField(BaseRelationshipCategory, parent_link=True,
                             related_name="%(app_label)s_%(class)s_related")


class Device(BaseDevice):
    parent_ptr = models.OneToOneField(BaseDevice, parent_link=True,
                             related_name="%(app_label)s_%(class)s_related")


class Encounter(BaseEncounter):
    parent_ptr = models.OneToOneField(BaseEncounter, parent_link=True,
                             related_name="%(app_label)s_%(class)s_related")


class Notification(BaseNotification):
    parent_ptr = models.OneToOneField(BaseNotification, parent_link=True,
                             related_name="%(app_label)s_%(class)s_related")


class Observation(BaseObservation):
    parent_ptr = models.OneToOneField(BaseObservation, parent_link=True,
                             related_name="%(app_label)s_%(class)s_related")


class Observer(BaseObserver):
    parent_ptr = models.OneToOneField(BaseObserver, parent_link=True,
                             related_name="%(app_label)s_%(class)s_related")

class Procedure(BaseProcedure):
    parent_ptr = models.OneToOneField(BaseProcedure, parent_link=True,
                             related_name="%(app_label)s_%(class)s_related")


class RequestLog(BaseRequestLog):
    parent_ptr = models.OneToOneField(BaseRequestLog, parent_link=True,
                             related_name="%(app_label)s_%(class)s_related")


class Subject(BaseSubject):
    parent_ptr = models.OneToOneField(BaseSubject, parent_link=True,
                                related_name="%(app_label)s_%(class)s_related")
