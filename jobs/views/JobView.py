from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from bpo.settings import DEFAULT_PAGE_SIZE
from jobs.forms import JobModelForm, JobLocationModelForm as LocationModelForm
from jobs.models import Job


class JobListView(ListView):
    template_name = 'jobs/jobs_list.html'

    paginate_by = DEFAULT_PAGE_SIZE

    model = Job

    context_object_name = 'job_list'


class JobCreateView(CreateView):
    model = Job

    form_class = JobModelForm

    context_object_name = 'job'

    template_name = 'jobs/job_form.html'

    location_form = LocationModelForm

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()

        if form.is_valid() and self.location_form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_form(self, form_class=None):

        self.location_form = LocationModelForm(**self.get_form_kwargs())

        return super().get_form(form_class)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'location_form' not in context:
            context['location_form'] = self.location_form

        return context

    def form_valid(self, form):

        form.instance.user = self.request.user

        response = super().form_valid(form)

        self.location_form.instance.job = form.instance

        self.location_form.save()

        return response

    def form_invalid(self, form):

        return super().form_invalid(form)


class JobUpdateView(UpdateView):
    model = Job

    context_object_name = 'job'

    template_name = 'job_create_form'

    pass


class JobDeleteView(DeleteView):
    model = Job

    context_object_name = 'job'

    template_name = 'job_create_form'

    pass
