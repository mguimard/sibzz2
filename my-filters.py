def my_func():
    return "hello"

class FilterModule(object):

    def filters(self):
        return {
            'my_func': my_func
        }
