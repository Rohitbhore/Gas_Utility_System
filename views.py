from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_status', request_id=service_request.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def request_status(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    return render(request, 'request_status.html', {'service_request': service_request})
