import pytest

from streaming.operations import MapFunction
from streaming.app.events import EventCollection


class GoodMapFunction(MapFunction):
    def map(self, event):
        return event


class KeyedMapFunction(MapFunction):
    def map(self, event):
        return self.keyed_event(event, 1)


class BadMapFunction(MapFunction):
    pass


def test_map_call():
    test_map = GoodMapFunction()
    event_collection = EventCollection(None)
    event_collection.events = [1, 2, 3]
    event_collection = test_map(event_collection)

    assert event_collection.events == [1, 2, 3]


def test_map_type():
    test_map = GoodMapFunction()
    assert test_map.type == 'MapFunction'


def test_map_function():
    test_map = GoodMapFunction()
    event = test_map.map({'event': 'data'})

    assert event == {'event': 'data'}


def test_map_function_keyed():
    test_map = KeyedMapFunction()
    event = test_map.map('word')

    assert event == ('word', 1)


def test_map_function_abstract():
    with pytest.raises(TypeError):
        BadMapFunction()
