import requests


def _POST(self):
    url = self.param['url']
    headers = self.param['headers']
    body = self.param['body']
    expect = self.param['expect']

    r = requests.post(url, headers=headers, data=body)
    assert r.ok
    print body
    resp_data = r.json()
    for k, v in expect.iteritems():
        assert resp_data[k] == v, "%s" % resp_data


def _GET(self):
    url = self.param['url']
    headers = self.param['headers']
    body = self.param['body']
    expect = self.param['expect']

    r = requests.get(url, headers=headers, data=body)
    assert r.ok
    resp_data = r.json()
    for k, v in expect.iteritems():
        assert resp_data[k] == v
