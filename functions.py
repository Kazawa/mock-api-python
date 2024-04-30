#!/usr/bin/env python3

import gitlab


# This function gets a project or list of projects, performs whatever
# logic you want on it, then do things, like create an issue.
def execute():
    # Connect to GitLab
    gl = gitlab.Gitlab("https://fake.gitlab.org", private_token="my-token")

    # Get single project
    my_project = gl.projects.get(990)

    # Create logic for your specific needs
    do_it = True
    if do_it:
        create_issue(my_project)
        # Todo Create more examples
    else:
        pass


def create_issue(project):
    project.issues.create(
        {
            "title": "Mock GitLab API",
            "description": "Create code to mock GitLab API calls.",
        }
    )


if __name__ == "__main__":
    execute()
