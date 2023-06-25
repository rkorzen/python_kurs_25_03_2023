from django.test import TestCase
from courses import factories
from django.urls import reverse



class TestTemplateCourseDetail(TestCase):


    def test_template_course_detail_enrolmment_button_available_for_logged_in_user(self):
        user = factories.UserFactory()
        course = factories.CourseFactory()
        detail_url = reverse("course-detail", kwargs={"pk": course.id})
        self.client.force_login(user)

        response = self.client.get(detail_url)
        self.assertContains(response, '<button type="submit" class="btn btn-primary">Zapisz się</button>')


    def test_template_course_detail_enrollmemt_button_is_hide_for_not_logged_in_user(self):
        course = factories.CourseFactory()
        detail_url = reverse("course-detail", kwargs={"pk": course.id})
        response = self.client.get(detail_url)
        self.assertNotContains(response, '<button type="submit" class="btn btn-primary">Zapisz się</button>')


    def test_template_course_detail_enrolmment_button_not_available_for_logged_and_enrolled_in_user(self):
        user = factories.UserFactory()
        course = factories.CourseFactory()
        factories.EnrollmentFactory(user=user, course=course)
        detail_url = reverse("course-detail", kwargs={"pk": course.id})
        self.client.force_login(user)
        response = self.client.get(detail_url)
        self.assertNotContains(response, '<button type="submit" class="btn btn-primary">Zapisz się</button>')