from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'telemetry.views.home', name='home'),
    # url(r'^telemetry/', include('telemetry.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', 'telemetry.alpha.views.cars'),
    url(r'^cars/?$', 'telemetry.alpha.views.cars'),
    url(r'^api/car/([0-9]+)/?$', 'telemetry.alpha.views.car_json'),
    url(r'^api/cars/?$', 'telemetry.alpha.views.cars_json'),
    url(r'^car/([0-9]+)/?$', 'telemetry.alpha.views.car'),
    url(r'^post/?$', 'telemetry.alpha.views.post'),
)
