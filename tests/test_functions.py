#!/usr/bin/env python3

from functions import create_issue
from gitlab import Gitlab
import requests
import requests_mock
import json
from tests import gitlab_fixtures as gf


class Test_GitLab_Functions:

    def set_up(self):
        # Create a fake session
        session = requests.Session()
        # Create a fake adapter
        adapter = requests_mock.Adapter()
        # Mount the adapter to a session with a fake URL
        session.mount("http://localhost", adapter)
        # Register your fake projects endpoint
        adapter.register_uri(
            "GET",
            "/api/v4/projects/1",
            json=gf.test_project,
            headers={"content-type": "application/json"},
        )
        # Register your fake issues endpoint
        adapter.register_uri(
            "POST",
            "/api/v4/projects/1/issues",
            json=gf.test_issue,
            headers={"content-type": "application/json"},
        )

        # Create fake gitlab connection using your fake session
        # https://python-gitlab.readthedocs.io/en/v4.4.0/api-usage-advanced.html#using-a-custom-session
        fake_gl = Gitlab(session=session, url="http://localhost", keep_base_url=True)

        return fake_gl, adapter

    def test_create_issue(self):
        fake_gl, adapter = self.set_up()
        my_project = fake_gl.projects.get(1)

        # Test the create_issue() function from functions.py
        create_issue(my_project)

        # Verify the responses from your test function are what you expected
        for matcher in adapter._matchers:
            assert matcher.called
            path = matcher._path
            if "issues" in path:
                assert (
                    "Create code"
                    in json.loads(matcher.request_history[0].text)["description"]
                )
                assert (
                    "Mock GitLab"
                    in json.loads(matcher.request_history[0].text)["title"]
                )

    def test_create_branch(self):
        pass

    def test_create_merge_request(self):
        pass

    # Todo
    def take_down(self):
        pass
