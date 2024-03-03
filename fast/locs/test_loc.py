from fastapi.testclient import TestClient
from fastapi import status, HTTPException

from fast.locs.loc import app, Location, get_location_404

locations= {
    "al": Location(name="ali", location="Karachi"),
    "zi": Location(name="zi", location="UK")
}

def fake_get_location_404(name:str)-> Location:
    loc = locations.get(name.lower())
    if not loc:
        raise HTTPException(status_code=404, detail=f"No location found for {name}")
    return loc

app.dependency_overrides[get_location_404] = fake_get_location_404

client = TestClient(app)


def test_read_location():
    response = client.get('/location/al')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == { 'name': 'ali', 'location':'Karachi'}
    
def test_404_location():
    response = client.get('/api/location/zz')
    assert response.status_code == status.HTTP_404_NOT_FOUND
    
