from django.test import TestCase

from accounts.models import User
from jobs.models import Job, JobLocation


class JobTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='bob', email='bob@gmail.com')

    def get_job(self):

        job_data = {
            'user': self.user,
            'emp': 'Conduent, Inc.',
            'title': 'Customer Service',
            'ref_code': 'serv.',
            'summary': 'test',
            'content': 'test',
        }

        job = Job(job_data)

        job.save()

        return job

    def test_location(self):

        location_data = {
            'job': self.get_job(),
            'address_1': 'Test Location',
            'city': 'Montego Bay',
            'state': 'St. James.',
            'country': 'jm',
        }

        location = JobLocation(location_data)

        location.save()

        self.assertTrue(location.job.id == 1)