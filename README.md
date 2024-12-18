# Update_TC
This script allows you to update test cases in the TestLink system by using the **updateTestCase** function. You need to specify the **test case's external ID** and provide the parameters you want to update and keep remaining as None

```bash
updateTestCase(['testcaseexternalid'],
    ['version', 'testcasename', 'summary', 'preconditions', 'steps',
     'importance', 'executiontype', 'status', 'estimatedexecduration',
     'user'])
```
You will get the status as **ok** in the API_response if test case updated successfully

```bash
(.venv) ~/PycharmProjects/Update_TC git:[master]
python3 update_testCase.py
TestCaseID TestCase_ExternalID TestCaseName

9232 pcie-1 Device_testing
9237 pcie-2 Random Read Operation
9242 pcie-3 Previous Versions
9246 pcie-4 PCIe Device Enumeration
Enter the full external ID of TC you want to update: pcie-1
Test case pcie-1 updated successfully!
API Response: {'status_ok': True, 'msg': 'ok', 'operation': 'updateTestCase'}
```
