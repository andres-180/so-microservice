import pytest
from op_stats.app import app
from op_stats.stats import Stats

@pytest.fixture
def client():
  return app.test_client()

def test_get_cpu_percent(mocker,client):
  mocker.patch.object(Stats, 'get_cpu_percent',return_value=100)
  response=client.get('/v1/stats/cpu')
  assert response.data.decode('utf-8')=='{"cpu_percent": 100}'
  assert response.status_code==200
 
def test_get_available_memory(mocker, client):
  mocker.patch.object(Stats, 'get_available_memory', return_value=2000)
  response = client.get('/v1/stats/memory')
  assert response.data.decode('utf-8') == '{"memoria_disponible(MB)": 2000}'
  assert response.status_code == 200


def test_get_disk_space(mocker, client):
  mocker.patch.object(Stats, 'get_disk_space', return_value=1000)
  response = client.get('/v1/stats/disk')
  assert response.data.decode('utf-8') == '{"espacio_en_disco(MB)": 1000}'
  assert response.status_code == 200

def test_dummy():
  assert 1==1
