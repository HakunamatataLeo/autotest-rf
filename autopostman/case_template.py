import requests


def _POST(self):
    url = self.param['url']
    headers = self.param['headers']
    body = self.param['body']
    expect = self.param['expect']

    r = requests.post(url, headers=headers, json=body)
    assert r.ok
    resp_data = r.json()
    for k, v in expect.iteritems():
        assert resp_data[k] == v


def _GET(self):
    url = self.param['url']
    headers = self.param['headers']
    body = self.param['body']
    expect = self.param['expect']

    r = requests.get(url, headers=headers, json=body)
    assert r.ok
    resp_data = r.json()
    for k, v in expect.iteritems():
        assert resp_data[k] == v
