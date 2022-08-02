from django.shortcuts import render
from django.views.generic import DetailView

from .models import Character, Voting


def index(request):
    return render(request, 'index.html')


class VotingDetailView(DetailView):

    CT_MODEL_MODEL_CLASS = {
        'voting': Voting
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'voting_model'
    template_name = 'voting_form.html'
    slug_url_kwarg = 'slug'


class CharacterDetailView(DetailView):

    CT_MODEL_MODEL_CLASS = {
        'character': Character
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'character_model'
    template_name = 'character_info.html'
    slug_url_kwarg = 'slug'



