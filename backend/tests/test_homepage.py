from main import HomeResponse


def test_homepage():
    response_home = HomeResponse(data="foobar")
    assert isinstance(response_home, HomeResponse)
    assert response_home.data == "foobar"
