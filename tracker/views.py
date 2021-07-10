from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RatingForm
from .services import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


def search(request):
    all_found = []
    response = myshows_search(request.GET.get("search", ""))
    for result in response["result"]:
        found = {'id': result["id"], 'title_eng': result["titleOriginal"]}
        all_found.append(found)
    context = {'all_found': all_found}
    return render(request, 'tracker/search.html', context)


@login_required
def index(request):
    user = request.user
    form_rating = RatingForm()
    serial_change_id = None
    if 'del_later' in request.POST:
        myshows_id = request.POST['del_later']
        delete_seriallater(myshows_id, user)
    if 'del_complete' in request.POST:
        myshows_id = request.POST['del_complete']
        delete_serialcomplete(myshows_id, user)
    if 'set_rating' in request.POST:
         form_rating = RatingForm(request.POST)
         if form_rating.is_valid():
             myshows_id = request.POST['set_rating']
             rating = request.POST['rating']
             set_rating(myshows_id, user.id, rating)
    if 'change_rating' in request.POST:
        serial_change_id = int(request.POST['change_rating'])
    serials_later_page = pagination(
        serials=set_all_seriallater(user),
        page=request.GET.get('page1'))
    serials_complete_page = pagination(
        serials=set_all_serialcomplete(user),
        page=request.GET.get('page2'))
    context = {
        'serials_later': serials_later_page,
        'serials_complete': serials_complete_page,
        'form_rating': form_rating,
        'serial_change_id': serial_change_id
        }
    return render(request, 'tracker/index.html', context)


def detail(request, id):
    user = request.user
    response = myshows_getbyid(id)
    context = response['result']
    context['show_button_later'] = set_button_later(id, user.id)
    context['show_button_complete'] = set_button_complete(id, user.id)
    if 'add_later' in request.POST:
        create_seriallater(response, user)
        return redirect('detail', id=id)
    if 'add_complete' in request.POST:
        create_serialcomplete(response, user)
        return redirect('detail', id=id)
    return render(request, 'tracker/detail.html', context)


class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login/"
    template_name = "registration/register.html"
    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)
    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def start(request):
    return render(request, 'tracker/start.html')
