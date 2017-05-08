from django.shortcuts import render, get_object_or_404
from .models import WorkRequest


def request_list(request):
    request_list = WorkRequest.objects.all().order_by('created_date')
    return render(request, 'workrequest/request_list.html', {'request_list': request_list})

def edit_request(request, pk):
    edit_request = get_object_or_404(WorkRequest, pk=pk)
    return render(request, 'workrequest/edit_request.html', {'edit_request': edit_request})
