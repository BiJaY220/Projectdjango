from django.test import TestCase
from .models import Student

# Create your tests here.
class StudentTestCase(TestCase):

    def setup(self):
        self.number_of_student = 10
        for i in range(0, self.number_of_student):
            Student.objects.create(name="mohamed", course="python")

            #course = "python and django"




        #Student.objects.create(name="mohamed", course="python")

    #def test_student_created(self):

    def test_query_set(self):
        qs = Student.objects.all()
        self.assertEqual(qs.count(), self.number_of_student)
    
    def test_queryset_exist(self):
        qs = Student.objects.all()
        #self.assertEqual(qs.exists(), True)
        self.assertTrue(qs.exists())

    # def test_arjit(self):
    #     obj = Student.objects.all()

    #     qs = Student.objects.filter(name="arjit")
    #     self.assertEqual(qs.count(), 1)
