from django.conf.urls import include, patterns, url

from tastypie.api import Api
from api.resources import JSONDocumentResource

v1_api = Api(api_name='v1')
v1_api.register(JSONDocumentResource())

urlpatterns = patterns('',
                       (r'^api/', include(v1_api.urls)),
                       url(r'^$', 'dashboard.views.dashboard', name='index'),
                       url(r'^home$', 'dashboard.views.home', name='home'),
                       url(r'^mapping_checks$',
                           'dashboard.views.mapping_checks',
                           name='mapping_checks'),
                       url(r'^age_distribution$',
                           'dashboard.views.age_distribution',
                           name='age_distribution'),
                       url(r'^survey_completed$',
                            'dashboard.views.survey_completed',
                            name='survey_completed'),
                        url(r'^survey_completed_teams$',
                            'dashboard.views.survey_completed_teams',
                            name='survey_completed_teams'),
                        url(r'^survey_completed_states$',
                            'dashboard.views.survey_completed_states',
                            name='survey_completed_states'),                            
                       )
