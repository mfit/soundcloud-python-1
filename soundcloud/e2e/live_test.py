import unittest
from soundcloud import Client
from .settings import (
    CLIENT_SECRET,
    CLIENT_ID,
    ACCESS_TOKEN,
    # REFRESH_TOKEN,
    # REDIRECT_URI,
    TRACK_ID,
)


@unittest.skipUnless(ACCESS_TOKEN is not None, "No ACCESS_TOKEN configured")
def test_get_tracks():
    cl = Client(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN
    )
    res = cl.get("/me/tracks")
    assert res.status_code == 200

    track_ids = [track.id for track in res]
    print(track_ids)


@unittest.skipUnless(TRACK_ID is not None, "No TRACK_ID configured")
def test_get_track_detail():
    cl = Client(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN
    )
    res = cl.get("/tracks/%s" % TRACK_ID)
    assert res.status_code == 200


@unittest.skipUnless(TRACK_ID is not None, "No TRACK_ID configured")
def test_put_track_metadata():
    cl = Client(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN
    )
    res = cl.put("/tracks/%s" % TRACK_ID, metadata={"title": "hello live test"})
    assert res.status_code == 200


@unittest.skipUnless(TRACK_ID is not None, "No TRACK_ID configured")
def test_put_metadata_with_track_uri():
    cl = Client(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN
    )
    res = cl.get("/tracks/%s" % TRACK_ID)
    res = cl.put(res.uri, metadata={"title": "updated with track.uri"})
    assert res.status_code == 200
