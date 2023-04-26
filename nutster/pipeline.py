import nutster.utils.cmd as cmd

class PipelineExecutionError(Exception):
    pass

class Process():
    fn = None
    def __init__(self, name):
        self.name = name

    def run(self, mutable):
        if self.fn == None:
            return None, False
        
        return self.fn(mutable)

class Pipeline():
    _processes = []

    def __init__(self, name, mutable=None):
        self.name = name
        self._mutable = mutable if mutable else None

    def add_process(self, process=None):
        if not process:
            return False

        self._processes.append(process)
        return True
    
    def run(self):
        for proc in self._processes:
            cmd.debug(self.name, ": running", proc.name)

            mutable, success = proc.run(self._mutable)
            if not success: 
                cmd.fatal(proc.name, "failed running.")
                raise PipelineExecutionError
            cmd.debug(proc.name, "was successful.")
            self._mutable = mutable

        return self._mutable 