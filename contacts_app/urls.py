from django.urls import path
from contacts_app import views

# app_name = 'contacts_app' # url namespacing
urlpatterns = [
    path('',views.homepageview,name='index'),
    path('add_contact/',views.addContactView,name='add_contact'),
    path('view_contact/',views.retrieveContacts,name='view_contact'),
    path('contact_detail/<int:contact_id>/',views.contactDetailView,
         name='contact_detail'),
    path('update-contact/<int:contact_id>/',views.updateView,
         name='update-contact'),
    path('delete-contact/<int:contact_id>/',views.deleteView,
         name='delete-contact'),
    path('search/', views.searchContacts, name='search'),
]