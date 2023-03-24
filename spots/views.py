from django.shortcuts import render,redirect,reverse
from .models import SurfSpots,Comment
from .filters import SpotFilter
from django.contrib.auth.decorators import login_required
from . import forms


def home_page(request):
    spot_filter = SpotFilter(request.GET, queryset=SurfSpots.objects.all())
    #surf_spots = SurfSpots.objects.all()
    context = {
        'form': spot_filter,
        'surf_spots': spot_filter.qs,
    }
    return render(request, 'spots/spot_list.html',context)

def spot_detail(request, slug):
    spot = SurfSpots.objects.get(slug=slug)
    return render(request, 'spots/spot_detail.html', {"spot": spot})

@login_required(login_url="/accounts/login/")
def add_comment(request,slug):
    spot = SurfSpots.objects.get(slug=slug)
    if request.method == "POST":
        comment_form = forms.AddComment(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.post = spot
            instance.save()
            return redirect("spots:detail",slug=slug)
    else:
        form = forms.AddComment()
        return render(request, 'spots/add_comment.html',{'spot': spot,'form':form})