import unittest
from nutster.pipeline import Pipeline, Process, PipelineExecutionError

def _add_five(mutable):
    return mutable+5, True

def _divide_by_two(mutable):
    return mutable/2, True

add_five_process = Process("add_five")
add_five_process.fn = _add_five

divide_by_two_process = Process("divide_by_two")
divide_by_two_process.fn = _divide_by_two

class PipelineTests(unittest.TestCase):
    pipeline = Pipeline("TestingPipeline", 5)
    
    def setUp(self):
        self.pipeline.add_process(add_five_process)
        self.pipeline.add_process(divide_by_two_process)
    
    def test_run(self):
        try:
            res = self.pipeline.run()
            self.assertEqual(res, 5)
        except Exception as e:
            self.assertEqual(type(e), PipelineExecutionError)

if __name__ == "__main__":
    unittest.main()