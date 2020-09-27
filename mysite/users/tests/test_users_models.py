from django.test import TestCase
from .models import CustomUser
from datetime import datetime
from model_bakery import baker

# for pytest only:
import pytest
from django.urls import reverse


@pytest.mark.django_db
# django_user_model takes model defined in settings.AUTH_USER_MODEL
def test_user_detail(client, django_user_model):
    user = django_user_model.objects.create(
        username="some_username", password="some_password"
    )
    url = reverse("user-detail-view", kwargs={"pk": user.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert "some_username" in response.content
