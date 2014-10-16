import urllib2
import json
import contextlib


def cvrapi(cvr, country='dk'):
    request = urllib2.Request(
        url='http://cvrapi.dk/api?search=%d&country=%s' % (cvr, country),
        headers={
            'User-Agent': 'My project - test cvrapi via Python/Django.'})
    with contextlib.closing(urllib2.urlopen(request)) as response:
        return json.loads(response.read())


# test cvrapi
print(cvrapi(10150817))
print(cvrapi(988615625, country='no'))
