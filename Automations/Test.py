#type:ignore
from Icii import *

class Test(PythonAutomation): 
    def ApplyAutomation(self):


        count = self.Items.Get('count', 0) | -1

        with self.CodeCellStart:
            test_iteration = 0

        with self.CodeAfterAutomation:
            test_iteration += 1
            print(test_iteration)
            (|if test_iteration == ((count)):
                _ = test_iteration|if count > 0 |)
