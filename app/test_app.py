import unittest
import json
from app import app, EQUAL, BEFORE, AFTER, STRING_RESPONSE

class TestSoftwareComparison(unittest.TestCase):
    
    def base_comparison(self, version_1, version_2, comparison):
        expected_response = STRING_RESPONSE % (version_1, comparison, version_2)
        params = {'version_1': version_1, 'version_2': version_2}
        tester = app.test_client(self)

        response = tester.get('/check_versions', json=params)

        return response, expected_response
    
    def test_methods_not_allowed(self):
        tester = app.test_client(self)

        response = tester.post('/check_versions')
        self.assertEqual(response.status_code, 405)

        response = tester.delete('/check_versions')
        self.assertEqual(response.status_code, 405)

        response = tester.put('/check_versions')
        self.assertEqual(response.status_code, 405)
    
    def test_no_parameters(self):
        tester = app.test_client(self)
        response = tester.get('/check_versions')

        self.assertEqual(response.status_code, 400)
    
    def test_missing_parameters(self):
        tester = app.test_client(self)
        response = tester.get('/check_versions', json={'version_2':'22'})

        self.assertEqual(response.status_code, 400)

    def test_before_version_0_format(self):
        response, expected_response = self.base_comparison('1', '3', BEFORE)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)

    def test_before_version_0_0_format(self):
        response, expected_response = self.base_comparison('1.1', '3.5', BEFORE)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)
    
    def test_before_version_0_0_0_format(self):
        response, expected_response = self.base_comparison('1.1.9', '3.1.1', BEFORE)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)
    
    def test_before_version_0_0_0_0_format(self):
        response, expected_response = self.base_comparison('1.1.9.6', '3.1.1.2', BEFORE)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)
    
    def test_after_version_0_format(self):
        response, expected_response = self.base_comparison('10', '3', AFTER)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)
    
    def test_after_version_0_0_format(self):
        response, expected_response = self.base_comparison('10.5', '3.1', AFTER)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)

    def test_after_version_0_0_0_format(self):
        response, expected_response = self.base_comparison('10.5.9', '3.1.1', AFTER)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)

    def test_equal_version_0_format(self):
        response, expected_response = self.base_comparison('1', '1', EQUAL)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)
    
    def test_equal_version_0_0_format(self):
        response, expected_response = self.base_comparison('1.5', '1.5', EQUAL)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)
    
    def test_equal_version_0_0_0_format(self):
        response, expected_response = self.base_comparison('1.5.7', '1.5.7', EQUAL)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)
    
    def test_equal_version_0_0_0_format_bad_request(self):
        response, expected_response = self.base_comparison('aaa.5.7', 'aaa.5.7', EQUAL)

        self.assertEqual(response.status_code, 400)


class TestSoftwareBasicComparison(unittest.TestCase):
    
    def base_comparison(self, version_1, version_2, comparison):
        expected_response = STRING_RESPONSE % (version_1, comparison, version_2)
        params = {'version_1': version_1, 'version_2': version_2}
        tester = app.test_client(self)

        response = tester.get('/check_versions_basic', json=params)

        return response, expected_response
    
    def test_methods_not_allowed(self):
        tester = app.test_client(self)

        response = tester.post('/check_versions_basic')
        self.assertEqual(response.status_code, 405)

        response = tester.delete('/check_versions_basic')
        self.assertEqual(response.status_code, 405)

        response = tester.put('/check_versions_basic')
        self.assertEqual(response.status_code, 405)
    
    def test_no_parameters(self):
        tester = app.test_client(self)
        response = tester.get('/check_versions_basic')

        self.assertEqual(response.status_code, 400)
    
    def test_missing_parameters(self):
        tester = app.test_client(self)
        response = tester.get('/check_versions_basic', json={'version_2':'22'})

        self.assertEqual(response.status_code, 400)
    
    def test_before_version_0_format(self):
        response, expected_response = self.base_comparison('1', '3', BEFORE)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)

    def test_before_version_0_0_format(self):
        response, expected_response = self.base_comparison('1.1', '3.5', BEFORE)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)
    
    def test_before_version_0_0_0_format(self):
        response, expected_response = self.base_comparison('1.1.9', '3.1.1', BEFORE)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)
    
    def test_before_version_0_0_0_0_format_bad_request(self):
        response, _ = self.base_comparison('1.1.9.6', '3.1.1.2', BEFORE)

        self.assertEqual(response.status_code, 400)
    
    def test_after_version_0_format(self):
        response, expected_response = self.base_comparison('10', '3', AFTER)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)
    
    def test_after_version_0_0_format(self):
        response, expected_response = self.base_comparison('10.5', '3.1', AFTER)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)

    def test_after_version_0_0_0_format(self):
        response, expected_response = self.base_comparison('10.5.9', '3.1.1', AFTER)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)

    def test_equal_version_0_format(self):
        response, expected_response = self.base_comparison('1', '1', EQUAL)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)
    
    def test_equal_version_0_0_format(self):
        response, expected_response = self.base_comparison('1.5', '1.5', EQUAL)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)
    
    def test_equal_version_0_0_0_format(self):
        response, expected_response = self.base_comparison('1.5.7', '1.5.7', EQUAL)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['comparison'], expected_response)

    def test_equal_version_0_0_0_format_letters(self):
        response, _ = self.base_comparison('1.5a.7', '1.5a.7', EQUAL)

        self.assertEqual(response.status_code, 400)

if '__main__' == __name__:
    unittest.main()