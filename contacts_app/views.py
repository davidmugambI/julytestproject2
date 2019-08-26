from django.shortcuts import render, redirect, get_object_or_404
from contacts_app.forms import AddContactForm, UpdateContactForm
from django.contrib import messages
from contacts_app.models import Contact
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepageview(request):
    return render(request, 'contacts_app_templates/index.html')

@login_required
def addContactView(request):
    if request.method == 'POST':
        form  = AddContactForm(request.POST,request.FILES)
        if form.is_valid():
            instance =  form.save(commit=False)
            instance.manager = request.user
            instance.save()
            messages.success(request, 'Contact added successfully')
            return redirect('index')
    else:
        form =  AddContactForm()

    dict = {'form': form}
    return render(request, 'contacts_app_templates/add_contact.html',dict)
@login_required
def retrieveContacts(request):
    contacts = Contact.objects.filter(manager=request.user)
    return render(request, 'contacts_app_templates/display.html', {'contacts':contacts})


@login_required
def contactDetailView(request,contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contacts_app_templates/detail.html', {'contact': contact})

@login_required
def updateView(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = UpdateContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            data = form.save(commit=False)
            data.manager = request.user
            data.save()
            messages.success(request, 'Contact sucessfully updated')
            return redirect('view_contact')
    else:
        form = UpdateContactForm(instance=contact)

    return render(request, 'contacts_app_templates/update.html', {'form': form})
    # create url for this
@login_required
def deleteView(request,contact_id):
    contact = get_object_or_404(Contact, id=contact_id).delete()
    return redirect('view_contact')
@login_required
def searchContacts(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Contact.objects.filter(
            Q(name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(phone__icontains=search_term) |
            Q(info__icontains=search_term)
        )
        context = {
            'search_term': search_term,
            'contacts': search_results.filter(manager=request.user)
        }
        return render(request, 'contacts_app_templates/index.html', context)
    else:
        return redirect('view_contact')