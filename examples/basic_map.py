from streaming.app import App
from streaming.operations import MapFunction, FilterFunction

# create a streaming app
app = App(name='My Stream Processor')

class MapProcessor(MapFunction):
    def map(self, event):
        return f'mapped-{event}'

class FilterProcessor(FilterFunction):
    def filter(self, event):
        if 'event' in event:
            return True

        return False

@app.stream()
def stream_processor(data_stream):
    events = ['event1', 'event2', 'event3', 'bad']
    print(f'input events = {events}')

    data_stream.source_from_collection(events)

    data_stream.filter(FilterProcessor()) \
          .map(MapProcessor())

    data_stream.print()