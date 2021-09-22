from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from models import Row, RowSession, Player, PersonalFrame, PersonalThrow
from forms import RowSessionCreateForm, PlayerForm


def make_throws(request, pk):
    if request.is_ajax and request.method == "POST":
        data = request.POST
        player_pk = int(data.get("player"))
        frame_name = data.get("frame_name")
        player = Player.objects.get(pk=player_pk)
        frame = PersonalFrame.objects.create(name=frame_name, player=player)
        throw_1 = data.get("throw_1")
        throw_2 = data.get("throw_2")
        if throw_1 == "X":
            PersonalThrow.objects.create(
                frame=frame,
                name="Throw Strike",
                value=throw_1,
            )
            return JsonResponse({"status":"success"})
        if throw_2 == "/":
            PersonalThrow.objects.create(
                frame=frame,
                name="Throws Spare",
                value=throw_1,
            )
            return JsonResponse({"status":"success"})
        PersonalThrow.objects.create(
            frame=frame,
            name="Throw one",
            value=throw_1,
        )
        PersonalThrow.objects.create(
            frame=frame,
            name="Throw two",
            value=throw_2,
        )
        return JsonResponse({"status":"success"})



# Create your views here.
class RowListView(ListView):

    template_name = "row_list.html"

    model = Row
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title":"List of row",
            })
        print(dict(context))
        return context


class RowDetailView(DetailView):

    template_name = "row_detail.html"
    model = Row

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class RowSessionDetailView(DetailView):

    template_name = "row_session_detail.html"

    model = RowSession

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class RowSessionUpdateView(UpdateView):

    template_name = "row_session_update.html"
    model = RowSession
    form_class = RowSessionCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = context["object"]
        players = object.players.all()
        if object.players.all():
            list_of_entry = [[entry, PlayerForm(instance=entry)] for entry in players]
            context.update({"list_of_entry": list_of_entry})
        context.update({"player_form": PlayerForm})
        print(context)
        return context


class RowSessionCreateView(CreateView):

    template_name = "row_session_create.html"

    model = RowSession
    form_class = RowSessionCreateForm


    def get(self, request, *args, **kwargs):
        data = request.GET
        user = User.objects.get(pk=request.session["_auth_user_id"])
        if data:
            row = Row.objects.get(pk = int(data.get("row")))
            self.initial = {"row": row, "user":user}
        return super().get(request, *args, **kwargs)

class PlayerUpdateView(UpdateView):

    template_name = "row_session_update.html"
    model = Player
    form_class = PlayerForm

class PlayerCreateView(CreateView):

    template_name = "row_session_create.html"

    model = Player
    form_class = PlayerForm
