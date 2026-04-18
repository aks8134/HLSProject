FILE_REGISTRY = {}

def register_file(arg):
    """Decorator to register a dataset class. Can be used as @register_file or @register_file('Name')."""
    if isinstance(arg, type):
        FILE_REGISTRY[arg.__name__] = arg
        return arg
    else:
        def decorator(cls):
            FILE_REGISTRY[arg] = cls
            return cls
        return decorator

class PolyBenchFile:
    file_path = ""
    
    def get_file(self):
        with open(self.file_path, 'r') as f:
            return f.read()


@register_file("2mm")
class MM2(PolyBenchFile):
    file_path = "datasets/PolyBenchC/linear-algebra/kernels/2mm/2mm.c"

@register_file("atax")
class ATAX(PolyBenchFile):
    file_path = "datasets/PolyBenchC/linear-algebra/kernels/atax/atax.c"


class ApplicationDataset:
    def __init__(self):
        self.applications = FILE_REGISTRY

    def get_applications(self):
        code_dict = {}
        for app in self.applications:
            code_dict[app] = self.applications[app]().get_file()
        return code_dict
