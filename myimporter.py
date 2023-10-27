import sys, types

class MyImporter(object):
    def __init__(self, override):
        self.override = override
  
    def find_module(self, module, path=None):
        if module in self.override:
            return self
        else:
            return None
      
    def load_module(self, name):
        mod = types.ModuleType(name)
        mod.__loader__ = self
        mod.__file__ = '/foo/bar/baz'
        mod.__package__ = name
        mod.__path__ = name.replace('.','/') + '/'
        sys.modules[name] = mod
        exec('print("Meow")\ndef foo():\n  print("Meow")',mod.__dict__)
        return mod
