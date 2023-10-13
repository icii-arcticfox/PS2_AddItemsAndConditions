#type:ignore
from Icii import *

class Test(PythonAutomation): 
    def ApplyAutomation(self):

        with self.CodeCellStart:
            test_iteration = 0

        with self.CodeAfterAutomation:
            test_iteration += 1
            print(test_iteration)
