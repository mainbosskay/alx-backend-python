#!/usr/bin/env python3
"""Module for function to test client file"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from requests import HTTPError
from typing import Dict
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Unittest for function GithubOrgClient"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, mockResp: Dict, mockGet: MagicMock) -> None:
        """Testing for GithubOrgClient class the org method"""
        mockGet.return_value = MagicMock(return_value=mockResp)
        instClient = GithubOrgClient(org)
        self.assertEqual(instClient.org(), mockResp)
        mockGet.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self) -> None:
        """Testing for GithubOrgClient class the public_repos_url method"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as prptyMock:
            prptyMock.return_value = {
                    'repos_url': "https://api.github.com/users/google/repos"
            }
            self.assertEqual(GithubOrgClient("google")._public_repos_url,
                             "https://api.github.com/users/google/repos")

    @patch("client.get_json")
    def test_public_repos(self, mockget_json: MagicMock) -> None:
        """Testing for GithubOrgClient class the public_repos method"""
        mockResp = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mockget_json.return_value = mockResp["repos"]
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mockReposUrl:
            mockReposUrl.return_value = mockResp["repos_url"]
            self.assertEqual(GithubOrgClient("google").public_repos(),
                             ["episodes.dart", "kratu"])
            mockReposUrl.assert_called_once()
        mockget_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False)
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Test for GithubOrgClient class the has_license method"""
        instClient = GithubOrgClient("google")
        has_licenseResult = instClient.has_license(repo, key)
        self.assertEqual(has_licenseResult, expected)

    @parameterized_class([
        {
            "org_payload": TEST_PAYLOAD[0][0],
            "repos_payload": TEST_PAYLOAD[0][1],
            "expected_repos": TEST_PAYLOAD[0][2],
            "apache2_repos": TEST_PAYLOAD[0][3]
        }
    ])
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """Integration testing for GithubOrgClient function"""
        @classmethod
        def setUpClass(cls) -> None:
            """SetsUp before running tests the class-level fixtures"""
            mock_ routes = {
                "https://api.github.com/orgs/google": cls.org_payload,
                "https://api.github.com/orgs/google/repos": cls.repos_payload
            }

            def mock_response(url):
                """Getting and returns mock response for given url request"""
                if url in mock_routes:
                    return Mock(**{"json.return_value": mock_routes[url]})
                return HTTPError
            cls.get_patcher = patch("requests.get", side_effect=mock_response)
            cls.get_patcher.start()

        @classmethod
        def tearDownClass(cls) -> None:
            """Deleting class-level fixtures after running all tests"""
            cls.get_patcher.stop()

        def test_public_repos(self) -> None:
            """Testing GithubOrgClient class the public_repos method"""
            self.assertEqual(GithubOrgClient("google").public_repos(),
                             self.expected_repos)

        def test_public_repos_with_license(self) -> None:
            """Testing for class the public_repos_with_license method"""
            self.assertEqual(
                GithubOrgClient("google").public_repos(license="apache-2.0"),
                self.apache2_repos)
