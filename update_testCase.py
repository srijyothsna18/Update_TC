from testlink import TestlinkAPIClient
from testlink.testlinkerrors import TLResponseError

class Update:
    def __init__(self):
        self.tlc = TestlinkAPIClient("http://localhost:8085/lib/api/xmlrpc/v1/xmlrpc.php", "10b2132073a17c9d4a0bc700dd778f83")

    def get_project_id(self, project_name):
        projects = self.tlc.getProjects()
        for project in projects:
            if project["name"] == project_name:
                return project["id"]
        raise ValueError(f"Project '{project_name}' not found.")

    def func(self):
        # Retrieve all test suites for the project
        res = self.tlc.getFirstLevelTestSuitesForTestProject(self.get_project_id("PCI"))
        suite_ids = [suite['id'] for suite in res]

        for suite_id in suite_ids:
            r = self.tlc.getTestCasesForTestSuite(testsuiteid=suite_id, deep=False, details="simple")

            for test_case in r:
                tc_id = test_case["id"]
                tc_full_ext_id = self.tlc.getTestCase(testcaseid=tc_id)[0]["full_tc_external_id"]
                tc_name = self.tlc.getTestCase(testcaseid=tc_id)[0]["name"]
                print(tc_id, tc_full_ext_id, tc_name)

    def update_tc(self):
        testcase_id = input("Enter the test case ID you want to update: ").strip()
        #new_summary = input("Enter the new summary for the test case: ").strip()

        try:
            # Update only the summary field
            response = self.tlc.updateTestCase(
                testcase_id,
                version=1,  # Optional, leave empty if not needed
                testcasename="Device_testing",  # Must be provided compulsory
                summary="testing a device",
                preconditions=None,  # Optional, leave empty if not needed
                steps=None,  # Optional, leave empty if not needed
                importance=None,  # Optional, leave empty if not needed
                executiontype=None,  # Optional, leave empty if not needed
                status=None,  # Optional, leave empty if not needed
                estimatedexecduration=None  # Optional, leave empty if not needed
            )
            print(f"Test case {testcase_id} updated successfully!")
            print("API Response:", response)  # Add this line to check the raw response
        except TLResponseError as e:
            print(f"Error occurred: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


# Initialize and run the update
u = Update()
print("TestCaseID TestCase_ExternalID TestCaseName\n")
u.func()
u.update_tc()
