import sys, types

class MyImplorter(object):
    def find_module(self, module, path=None):
        return self
      
    def load_module(self, name):
        mod = types.ModuleType(name)
        mod.__loader__ = self
        mod.__file__ = '/foo/bar/baz'
        mod.__package__ = name
        mod.__path__ = name.replace('.','/') + '/'
        sys.modules[name] = mod
        exec('print("Meow")\n',mod.__dict__)
        return mod
