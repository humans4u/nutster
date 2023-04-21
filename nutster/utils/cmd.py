QUIET = False
DEBUG = False
class _color:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

def _message(tag, args, isfatal=False):
    if QUIET and not isfatal:
      return 
    print('NUTSTER:', tag, end=' ')
    for arg in args:
        print(arg, end=' ')
    print()


def debug(*args):
    if not DEBUG:
        return
    tag = f'[{_color.CYAN}DEBUG{_color.END}]'
    _message(tag, args)

def info(*args):
    tag = f'[INFO]'
    _message(tag, args)

def warn(*args):
    tag = f'[{_color.YELLOW}WARN{_color.END}]'
    _message(tag, args)

def fatal(*args):
    tag = f'[{_color.RED}FATAL{_color.END}]'
    _message(tag, args, True)