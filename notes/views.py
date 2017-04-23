from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Note
from django.shortcuts import redirect

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'notes/home.html'
    context_object_name = 'all_notes'

    def get_queryset(self):
        return Note.objects.all()

class DetailView(generic.DetailView):
    model = Note
    template_name = 'notes/detail.html'

class NoteCreate(CreateView):
    model = Note
    fields = ['note_title', 'brief', 'body', 'note_logo']

class NoteUpdate(UpdateView):
    model = Note
    fields = ['note_title', 'brief', 'body', 'note_logo']

class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('notes:home')

class UserFormView(View):
    form_class = UserForm
    template_name = 'notes/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned/ normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User Objects if credentioals are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('notes:home')
        return render(request, self.template_name, {'form': form})

def logout_view(request):
    logout(request)
    return redirect('notes:home')













