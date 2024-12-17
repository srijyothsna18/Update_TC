# Update_TC
This script allows you to update test cases in the TestLink system by using the **updateTestCase** function. You can specify the test case's external ID and provide the parameters you want to update.

```bash
updateTestCase(['testcaseexternalid'],
    ['version', 'testcasename', 'summary', 'preconditions', 'steps',
     'importance', 'executiontype', 'status', 'estimatedexecduration',
     'user'])
