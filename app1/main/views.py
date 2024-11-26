from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    
    contacts = Contact.objects.all().order_by('-is_favorite', 'name')
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()

    return render(request, 'main/contact_list.html', {'contacts': contacts, 'form': form})

def delete_contact(request):
    if request.method == 'POST':
        contact_id = request.POST.get('contact_id')
        Contact.objects.filter(id=contact_id).delete()
        return redirect('contact_list')

def toggle_favorite(request):
    if request.method == 'POST':
        contact_id = request.POST.get('contact_id')
        contact = Contact.objects.get(id=contact_id)
        contact.is_favorite = not contact.is_favorite
        contact.save()
        return JsonResponse({'is_favorite': contact.is_favorite}) 

