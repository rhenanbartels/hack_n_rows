from django.conf.urls import patterns, include, url

urlpatterns = patterns('hack_n_rows.core.views',
        url(r'^$', 'home', name='home')
)
