__all__ =[
    'Todo',
]

VERSION = '0.1.1'


class classproperty(object):
        def __init__(self, getter):
            self.getter = getter

        def __get__(self, instance, owner):
           return self.getter(owner)


class Todo:
    items = []
    completed = []

    @classmethod
    def add(cls, task):
        cls.items.append(task)
        return(True, '{task} is added '.format(task=task))

    @classproperty
    def list(cls):
        for index, task in enumerate(cls.items, 1):
            print('{:04d} : {}'.format(index, task))


    @classmethod
    def complete(cls, index):
        index = index - 1
        removed_task = cls.items.pop(index)
        cls.completed.append(removed_task)
        return(True, '{} is completed!'.format(removed_task))

    @classproperty
    def completed_list(cls):
        for index, task in enumerate(cls.completed, 1):
            print('{:04d} : {}'.format(index, task))


if __name__ == '__main__':


    import sys
    sys.argv.append('-v')
    import doctest
    doctest.testmod()
