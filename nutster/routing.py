from nutster.pipeline import *




def HandlePath(mutable):
   handler = mutable['handler']
   match handler.path:
    case 'hello':
       mutable['target'] = 'hello'
    case _:
       mutable['target'] = None
   pass 