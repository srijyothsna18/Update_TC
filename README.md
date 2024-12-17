# Update_TC
This script allows you to update test cases in the TestLink system by using the **updateTestCase** function. You need to specify the **test case's external ID** and provide the parameters you want to update and keep remaining as None

```bash
updateTestCase(['testcaseexternalid'],
    ['version', 'testcasename', 'summary', 'preconditions', 'steps',
     'importance', 'executiontype', 'status', 'estimatedexecduration',
     'user'])
