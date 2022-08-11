nl = '\n'

def build_error(message: str, **kwargs) -> RuntimeError:
    return RuntimeError(f'''{message}\n {' '.join(map(lambda x: f'{x}:{str(kwargs[x])}{nl}', kwargs))}''')
