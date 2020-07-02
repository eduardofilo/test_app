import pytest

from django.urls import reverse

from dictionary.models import Word


@pytest.mark.django_db
def test_db(client, django_db_setup):
    assert Word.objects.all().count() == 10000


@pytest.mark.django_db
def test_word_list_view(client):
    url = reverse('dictionary:word_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_word_create_view(client):
    url = reverse('dictionary:word_create')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_word_update_view_1(client):
    url = reverse('dictionary:word_update', args=[1])
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db
def test_word_update_view_2(client):
    url = reverse('dictionary:word_update', args=[34])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_word_delete_view(client):
    url = reverse('dictionary:word_delete', args=[34])
    response = client.get(url)
    assert response.status_code == 302
