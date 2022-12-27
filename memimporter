import types
import sys
import fs

class MemImporter(object):
    def __init__(self, fs_obj):
        self.fs = fs_obj

    def find_module(self, module, path=None):
        if self.fs.isfile(f'/{module.replace(".","/")}/__init__.py') or self.fs.isfile(f'/{module.replace(".","/")}.py'):
            return self
        else:
            return None
    
    def load_module(self, name):
        mod = types.ModuleType(name)
        mod.__loader__ = self
        if self.fs.isfile(f'/{name.replace(".","/")}.py'):
            filename = f'/{name.replace(".","/")}.py'
        else:
            filename = f'/{name.replace(".","/")}/__init__.py'
        mod_content = self.fs.open(filename,'r').read()
        mod.__file__ = filename
        mod.__package__ = name
        mod.__path__ = 'mem:/' + '/'.join(filename.split('/')[:-1]) + '/'
        sys.modules[name] = mod
        exec(mod_content, mod.__dict__)
        return mod
