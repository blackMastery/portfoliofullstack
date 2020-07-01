from django.shortcuts import render
from django.views.generic.base import TemplateResponseMixin, View
from django.shortcuts import render
from .forms import ProjectForm

# Create your views here.




class Index(View):
    intro = "I am a  full-stack developer with an eye for detail, building client and server application for five years, with the diverse skill from HTML and javascript, with frameworks like react and angular to django, mysql, mongodb etc. With a sound agile project management discipline from years of building client-server application, there is very little that we cannot achieve in a timely manner"
    template_name = 'pages/index.html'

    def get(self, request):
        return render(request, self.template_name, {"intro": self.intro})





class Contact(View):
    template_name = 'pages/contact/contact.html'
    projectform = ProjectForm()

    def get(self, request):
        print(request.session.session_key)
        return render(request, self.template_name, {'projectform': self.projectform})
    



class Projects(View):
    template_name = 'pages/projects/project.html'

    def get(self, request):
        return render(request, self.template_name)




class Services(View):
    template_name = 'pages/services/service.html'

    def get(self, request):
        return render(request, self.template_name) 