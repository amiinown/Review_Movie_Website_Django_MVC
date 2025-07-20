from django.shortcuts import render
from django.views import View
from .models import Actor

class ActorShowAllView(View):
    template_name = 'actor/show_all_actor.html'

    def get(self, request):
        actors = Actor.objects.all().order_by('created')
        return render(request, self.template_name, {'actors':actors})
    
class ActorRolePlayedView(View):
    template_name = 'actor/show_all_actor_role_played.html'

    def get(self, request, id):
        actor = Actor.objects.get(pk=id)
        return render(request, self.template_name, {'actor':actor})