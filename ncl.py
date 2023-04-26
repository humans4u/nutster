#!/usr/bin/env python3
import sys
from nutster.tests import pipeline
import nutster.utils.cmd as cmd 

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if str(sys.argv[1]) == "doctor":
            cmd.info("Running minimal tests to check",
                     "if your system can run nutster") 
            cmd.info("Checking imports")
            try:
                import netifaces
                import unittest
            except:
                cmd.fatal("Some modules are missing")
                sys.exit(-1)

            cmd.info("Tests passed, ready to use")
            sys.exit(0)

    import nutster.cmd
