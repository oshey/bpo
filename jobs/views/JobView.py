from django.views.generic import ListView

from jobs.models import Job


class JobListView(ListView):
    template_name = 'jobs/jobs_list.html'

    paginate_by = 15

    model = Job

    pass