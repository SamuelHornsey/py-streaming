import sys

from streaming.sinks.base import Sink


class StdoutSink(Sink):
    def pipe(self, event_collection):
        """ send event to stdout """
        for event in event_collection:
            sys.stdout.write('%s\n' % event)
