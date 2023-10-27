# ImportHookDemo
A collection of simple import hooks for a demonstration

## Simplehook
![image](https://github.com/rkbennett/ImportHookDemo/assets/44292326/94bba764-aeec-4ab1-a901-19edf24ada9d)

## MyImporter
![image](https://github.com/rkbennett/ImportHookDemo/assets/44292326/c070030d-eb46-4f03-9c42-010d93c739e2)


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

Example usage
![image](https://user-images.githubusercontent.com/44292326/209714185-a85ab6fb-e38c-4799-9604-8340f2ec1d6c.png)
