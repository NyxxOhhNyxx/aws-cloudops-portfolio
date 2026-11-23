from app import app


def test_homepage_renders_personal_site():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Nikolas" in response.data
    assert b"CloudOps" in response.data
    assert b"Dender19" in response.data
    assert b"VS Direct" in response.data
    assert b"Online banking" in response.data or b"Banking simulation" in response.data
    assert b"wasielewski.nikolas@outlook.com" in response.data


def test_project_pages():
    client = app.test_client()
    for slug, title in [("cloudops", "CloudOps"), ("banking", "Online banking"),
                        ("windows-server", "Windows Server"), ("calculator", "calculator")]:
        response = client.get("/projects/" + slug)
        assert response.status_code == 200
        assert title.encode() in response.data


def test_missing_project_returns_404():
    response = app.test_client().get("/projects/does-not-exist")
    assert response.status_code == 404


def test_health_contract_unchanged():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    body = response.get_json()
    assert body["status"] == "healthy"
    assert body["service"] == "cloudops"
    assert "timestamp" in body


def test_assets_and_security_headers():
    client = app.test_client()
    for resource in ["/static/css/styles.css", "/static/js/site.js", "/static/img/portrait.svg"]:
        assert client.get(resource).status_code == 200
    assert client.get("/").headers["X-Content-Type-Options"] == "nosniff"
