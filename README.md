# ImportHookDemo
A collection of simple import hooks for a demonstration

The memimport hook requires pyFileSystem (fs) to be installed

To prep an example of importing from peFileSystem's mem:// path do the following

```
import fs
memfs = fs.open_fs('mem://')
memfs.makedirs('demo')
with memfs.open('demo/__init__.py', 'w+') as demo:
    demo.write('def example():\n    return("Working")\n\n__all__ = [example]')

import memimport, sys
sys.meta_path.insert(0,memimport.MemImporter(memfs))
import demo
```
