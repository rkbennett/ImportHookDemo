import sys, types

class MyImporter(object):
    def find_module(self, module, path=None):
        return self
      
    def load_module(self, name):
        mod = types.ModuleType(name)
        mod.__loader__ = self
        mod.__file__ = '/foo/bar/baz'
        mod.__package__ = name
        mod.__path__ = name.replace('.','/') + '/'
        sys.modules[name] = mod
        exec('print("Meow")\ndef foo():\n  print("Meow")',mod.__dict__)
        return mod
