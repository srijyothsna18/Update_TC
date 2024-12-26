from testlink import TestlinkAPIClient
from testlink.testlinkerrors import TLResponseError



class Update:
    def __init__(self):
        self.tlc = TestlinkAPIClient("http://localhost:8085/lib/api/xmlrpc/v1/xmlrpc.php", "10b2132073a17c9d4a0bc700dd778f83")

    def get_project_id(self,project_name):
        projects = self.tlc.getProjects()
        for project in projects:
            if project["name"] == project_name:
                return project["id"]
        raise ValueError(f"Project '{project_name}' not found.")

    def list_all_suites_and_test_cases(self):
        try:
            project_id = self.get_project_id("PCI")
            top_level_suites = self.tlc.getFirstLevelTestSuitesForTestProject(project_id)

            for suite in top_level_suites:
                suite_id = suite.get("id")
                if suite_id:
                    print(f"Processing top-level suite ID: {suite_id}")
                    self.fetch_suites_and_test_cases(suite_id)

        except TLResponseError as e:
            print(f"TestLink API error while listing suites: {e}")
        except Exception as e:
            print(f"Unexpected error while listing suites: {e}")


    def fetch_suites_and_test_cases(self, suite_id, level=0):
        try:
            suite_details = self.tlc.getTestSuiteByID(suite_id)
            suite_name = suite_details.get("name", "Unknown Suite Name")
            suite_prefix = "    " * level  # Indentation for nested suites
            print(f"{suite_prefix}Suite ID: {suite_id} - Suite Name: {suite_name}")

            test_cases = self.tlc.getTestCasesForTestSuite(testsuiteid=suite_id, deep=False, details="simple")


            for test_case in test_cases:
                tc_id = test_case["id"]
                tc_data = self.tlc.getTestCase(testcaseid=tc_id)[0]
                tc_full_ext_id = tc_data["full_tc_external_id"]
                tc_name = tc_data["name"]
                print(f"{suite_prefix}  TestCase: {tc_id} {tc_full_ext_id} {tc_name}")

            # Fetch nested suites
            nested_suites = self.tlc.getTestSuitesForTestSuite(suite_id) or {}
            if nested_suites:
                for nested_suite_id, nested_suite_data in nested_suites.items():
                    if nested_suite_id.isdigit():
                        self.fetch_suites_and_test_cases(nested_suite_id, level + 1)


        except TLResponseError as e:
            print(f"TestLink API error for suite ID {suite_id}: {e}")
        except Exception as e:
            print(f"Unexpected error for suite ID {suite_id}: {e}")



    def update_test_case(self):
        try:
            testcase_id = input("Enter the test case ID you want to update: ").strip()
            # Example update data
            response = self.tlc.updateTestCase(
                testcase_id,
                version=1,
                testcasename="Device_testing",
                summary="testing a device",
                preconditions="Device must be powered on",
                steps=[
                    {"step_number": 1, "actions": "Connect device", "expected_results": "Device connected",
                     "execution_type": 1},
                    {"step_number": 2, "actions": "Start testing", "expected_results": "Tests running",
                     "execution_type": 2}
                ],
                importance=2,
                executiontype=1,
                status=1,
                estimatedexecduration="5",
                #user="admin"
            )
            print(f"Test case {testcase_id} updated successfully!")
            print("API Response:", response)

        except TLResponseError as e:
            print(f"TestLink API error while updating test case: {e}")
        except Exception as e:
            print(f"Unexpected error while updating test case: {e}")


if __name__ == "__main__":
    updater = Update()
    updater.list_all_suites_and_test_cases()
    updater.update_test_case()
