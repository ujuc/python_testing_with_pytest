import datetime
import random
import time

import pytest


@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = 'duration/' + request.node.nodeid.replace(':', '_')
    # nodeid's can have colons
    # key become filenames within .cache
    # replace colons with something filename safe
    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)
    cache.get(key, this_duration)

    if last_duration is not None:
        errorstarting = "Test duration over 2x last duration"
        assert this_duration <= last_duration * 2, errorstarting


@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random.random())
