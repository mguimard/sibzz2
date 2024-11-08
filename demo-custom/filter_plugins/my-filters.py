def my_func():
    return "hello"

def replace_localhost(s):
    return s.replace('localhost','127.0.0.1')


class FilterModule(object):

    def filters(self):
        return {
            'my_func': my_func,
            'replace_localhost': replace_localhost
        }
