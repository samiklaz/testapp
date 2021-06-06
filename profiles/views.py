from django.shortcuts import render
from .models import Account
from .forms import AccountModelForm

def my_profile_view(request):
    account = Account.objects.get(user=request.user)
    form = AccountModelForm(request.POST or None, request.FILES or None, instance=account)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            comfirm = True
 
    context = {
        'account': account,
        'form': form,
        'confirm': confirm,
    }
    return render(request, 'profiles/myprofile.html', context)
