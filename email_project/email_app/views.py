from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmailForm
from .models import EmailRecord
from .tasks import send_email_task

def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_email_task.delay(recipient, subject, message)
            
            messages.success(request, f'Задание на отправку email на {recipient} добавлено в очередь!')
            return redirect('send_email')
    else:
        form = EmailForm()
    
    # Получаем список последних отправленных писем
    email_records = EmailRecord.objects.order_by('-sent_at')[:10]
    
    return render(request, 'email_app/send_email.html', {
        'form': form,
        'email_records': email_records
    })