#!/usr/bin/python

class FilterModule(object):
    def filters(self):
        return {
            'elvis_filter': self.elvis_filter
        }

    def elvis_filter(self, input):
        if not input:
            return list()
        
        return input