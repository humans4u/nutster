from nutster.utils.meta import check_if_neighbour_is_valid 
import nutster.utils.cmd as cmd

class Node:
    ip = ""
    port = 8080
    sname = ""
    neighbours = []

    def __init__(self):
         pass

    def add_neighbour(self, neighbour = None):
        if not check_if_neighbour_is_valid(neighbour):
                return False
        return True

        
class Neighbour:
    ip = ""
    port = 8080
    sname = ""

    def __init__(self):
         pass

    def notify(self, pack):
         cmd.info(f'@{self.sname}:', pack)

