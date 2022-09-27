# rustici_software_cloud_v2
REST API used for SCORM Cloud integrations.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0
- Package version: 2.1.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.
Python 3.4+

## Installation
### pip
[rustici_software_cloud_v2](https://pypi.org/project/rustici_software_cloud_v2/)

```sh
pip install rustici_software_cloud_v2
```

### GitHub
[scormcloud-api-v2-client-python](https://github.com/RusticiSoftware/scormcloud-api-v2-client-python)

```sh
pip install git+https://github.com/RusticiSoftware/scormcloud-api-v2-client-python.git
```

### Setuptools
```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import rustici_software_cloud_v2
```

## Tips and Tricks
Working with headers will require calling the `WithHttpInfo` version of the function. This allows for grabbing the header directly from the response object:
```python
# Note: This code is specifically designed to not modify any existing data
dispatch_api = scorm_cloud.DispatchApi()
response = dispatch_api.update_dispatches_with_http_info(scorm_cloud.UpdateDispatchSchema(), since=datetime.utcnow().isoformat() + 'Z')
print(response[2]['X-Total-Count'])
```

## Changelog:
Check the [changelog](https://cloud.scorm.com/docs/v2/reference/changelog/) for details of what has changed.

## Sample Code
```python
import rustici_software_cloud_v2 as scorm_cloud
from datetime import datetime, timedelta
import urllib.parse as ul
import time


# ScormCloud API credentials
# Note: These are not the same credentials used to log in to ScormCloud
APP_ID = "APP_ID"
SECRET_KEY = "SECRET_KEY"

# Sample values for data
COURSE_PATH = "/PATH/TO/COURSE/RunTimeAdvancedCalls_SCORM20043rdEdition.zip"

COURSE_ID = "PY_SAMPLE_COURSE"
LEARNER_ID = "PY_SAMPLE_COURSE_LEARNER"
REGISTRATION_ID = "PY_SAMPLE_COURSE_REGISTRATION"

# String used for output formatting
OUTPUT_BORDER = "---------------------------------------------------------\n"


def main():
    """
    This sample will consist of:
    1. Creating a course.
    2. Registering a learner for the course.
    3. Building a link for the learner to take the course.
    4. Getting the learner's progress after having taken the course.
    5. Viewing all courses and registrations.
    6. Deleting all of the data created via this sample.

    All input variables used in this sample are defined up above.
    """

    # Configure HTTP basic authorization: APP_NORMAL
    config = scorm_cloud.Configuration()
    config.username = APP_ID
    config.password = SECRET_KEY

    # Set the default configuration values for new configuration objects
    scorm_cloud.Configuration().set_default(config)

    sc = ScormCloud_Python_Sample()

    try:
        # Create a course and a registration
        course_details = sc.create_course(COURSE_ID, COURSE_PATH)
        sc.create_registration(COURSE_ID, LEARNER_ID, REGISTRATION_ID)

        # Show details of the newly imported course
        print("Newly Imported Course Details: ")
        print(course_details)



        # Create the registration launch link
        launch_link = sc.build_launch_link(REGISTRATION_ID)

        # Show the launch link
        print(OUTPUT_BORDER)
        print(f"Launck Link: {launch_link}")
        print("Navigate to the url above to take the course. Hit enter once complete.")
        input()



        # Get the results for the registration
        registration_progress = sc.get_result_for_registration(REGISTRATION_ID)

        # Show details of the registration progress
        print(OUTPUT_BORDER)
        print("Registration Progress: ")
        print(registration_progress)



        # Get information about all the courses in ScormCloud
        course_list = sc.get_all_courses()

        # Show details of the courses
        print(OUTPUT_BORDER)
        print("Course List: ")
        for course in course_list:
            print(course)



        # Get information about all the registrations in ScormCloud
        registration_list = sc.get_all_registrations()

        # Show details of the registrations
        print(OUTPUT_BORDER)
        print("Registration List: ")
        for registration in registration_list:
            print(registration)

    except (scorm_cloud.rest.ApiException, ValueError) as err:
        print(err)

    finally:
        # Delete all the data created by this sample
        sc.clean_up(COURSE_ID, REGISTRATION_ID)


class ScormCloud_Python_Sample:

    def __configure_oauth(self, scopes):
        """
        Sets the default OAuth token passed with all calls to the API.

        If a token is created with limited scope (i.e. read:registration),
        calls that require a different permission set will error. Either a
        new token needs to be generated with the correct scope, or the
        default access token can be reset to None. This would cause the
        request to be made with basic auth credentials (appId/ secret key)
        instead.

        Additionally, you could create a new configuration object and set
        the token on that object instead of the default access token. This
        configuration would then be passed into the Api object:

        config = scorm_cloud.Configuration()
        token_request = {
            'permissions': scorm_cloud.PermissionsSchema([ "write:course", "read:course" ]),
            'expiry': (datetime.utcnow() + timedelta(minutes=2)).isoformat() + 'Z'
        }
        config.access_token = app_management_api.create_token(token_request).result
        course_api = scorm_cloud.CourseApi(scorm_cloud.ApiClient(config))

        Any calls that would use this CourseApi instance would then have the
        write:course and read:course permissions passed automatically, but
        other instances would be unaffected and continue to use other means
        of authorization.

        :param scopes: List of permissions for calls made with the token.
        :type scopes: list[str]
        """

        app_management_api = scorm_cloud.ApplicationManagementApi()

        # Set permissions and expiry time of the token
        # The expiry expected for token request must be in ISO-8601 format
        expiry = (datetime.utcnow() + timedelta(minutes=2)).isoformat() + 'Z'
        permissions = scorm_cloud.PermissionsSchema(scopes)

        # Make the request to get the OAuth token
        token_request = scorm_cloud.TokenRequestSchema(permissions, expiry)
        token_result = app_management_api.create_token(token_request)

        # Set the default access token used with further API requests.
        # To remove the token, reset config.access_token back to None
        # and set the default before the next call.
        config = scorm_cloud.Configuration()
        config.access_token = token_result.result
        scorm_cloud.Configuration().set_default(config)

    def create_course(self, course_id, course_path):
        """
        Creates a course by uploading the course from your local machine.
        Courses are a package of content for a learner to consume.

        Other methods for importing a course exist. Check the documentation
        for additional ways of importing a course.

        :param course_id: Id that will be used to identify the course.
        :type course_id: str
        :param course_path: Path to the course being uploaded.
        :type course_path: str
        :returns: Detailed information about the newly uploaded course.
        :rtype: CourseSchema
        """

        # (Optional) Further authenticate via OAuth token access
        # self.__configure_oauth([ "write:course", "read:course" ])

        # This call will use OAuth with the "write:course" scope
        # if configured.  Otherwise the basic auth credentials will be used
        course_api = scorm_cloud.CourseApi()
        job_id = course_api.create_upload_and_import_course_job(course_id, file=course_path)

        # This call will use OAuth with the "read:course" scope
        # if configured.  Otherwise the basic auth credentials will be used
        job_result = course_api.get_import_job_status(job_id.result)
        while job_result.status == "RUNNING":
            time.sleep(1)
            job_result = course_api.get_import_job_status(job_id.result)

        if job_result.status == "ERROR":
            raise ValueError("Course is not properly formatted: " + job_result.message)

        return job_result.import_result.course

    def create_registration(self, course_id, learner_id, registration_id):
        """
        Creates a registration allowing the learner to consume the course
        content. A registration is the link between a learner and a single
        course.

        :param course_id: Id of the course to register the learner for.
        :type course_id: str
        :param learner_id: Id that will be used to identify the learner.
        :type learner_id: str
        :param registration_id: Id that will be used to identify the registration.
        :type registration_id: str
        """

        # (Optional) Further authenticate via OAuth token access
        # self.__configure_oauth([ "write:registration" ])

        registration_api = scorm_cloud.RegistrationApi()
        learner = scorm_cloud.LearnerSchema(learner_id)
        registration = scorm_cloud.CreateRegistrationSchema(course_id, learner, registration_id)
        registration_api.create_registration(registration)

    def build_launch_link(self, registration_id):
        """
        Builds a url allowing the learner to access the course.

        This sample will build the launch link and print it out. It will then
        pause and wait for user input, allowing you to navigate to the course
        to generate sample learner progress. Once this step has been reached,
        hitting the enter key will continue program execution.

        :param registration_id: Id of the registration the link is being built for.
        :type registration_id: str
        :returns: Link for the learner to launch the course.
        :rtype: str
        """

        # (Optional) Further authenticate via OAuth token access
        # self.__configure_oauth([ "read:registration" ])

        registration_api = scorm_cloud.RegistrationApi()
        settings = scorm_cloud.LaunchLinkRequestSchema(redirect_on_exit_url="Message")
        launch_link = registration_api.build_registration_launch_link(registration_id, settings)

        return launch_link.launch_link

    def get_result_for_registration(self, registration_id):
        """
        Gets information about the progress of the registration.

        For the most up-to-date results, you should implement our postback
        mechanism. The basic premise is that any update to the registration
        would cause us to send the updated results to your system.

        More details can be found in the documentation:
        https://cloud.scorm.com/docs/v2/guides/postback/

        :param registration_id: Id of the registration to get results for.
        :type registration_id: str
        :returns: Detailed information about the registration's progress.
        :rtype: RegistrationSchema
        """

        # (Optional) Further authenticate via OAuth token access
        # self.__configure_oauth([ "read:registration" ])

        registration_api = scorm_cloud.RegistrationApi()
        progress = registration_api.get_registration_progress(registration_id)

        return progress

    def get_all_courses(self):
        """
        Gets information about all courses. The result received from the API
        call is a paginated list, meaning that additional calls are required
        to retrieve all the information from the API. This has already been
        accounted for in the sample.

        :returns: List of detailed information about all of the courses.
        :rtype: list[CourseSchema]
        """

        # (Optional) Further authenticate via OAuth token access
        # self.__configure_oauth([ "read:course" ])

        # Additional filters can be provided to this call to get a subset
        # of all courses.
        course_api = scorm_cloud.CourseApi()
        response = course_api.get_courses()

        # This call is paginated, with a token provided if more results exist
        course_list = response.courses
        while response.more is not None:
            response = course_api.get_courses(more=response.more)
            course_list += response.courses

        return course_list

    def get_all_registrations(self):
        """
        Gets information about the registration progress for all
        registrations. The result received from the API call is a paginated
        list, meaning that additional calls are required to retrieve all the
        information from the API. This has already been accounted for in the
        sample.

        This call can be quite time-consuming and tedious with lots of
        registrations. If you find yourself making lots of calls to this
        endpoint, it might be worthwhile to look into registration postbacks.

        More details can be found in the documentation:
        https://cloud.scorm.com/docs/v2/guides/postback/

        :returns: List of detailed information about all of the registrations.
        :rtype: list[RegistrationSchema]
        """

        # (Optional) Further authenticate via OAuth token access
        # self.__configure_oauth([ "read:registration" ])

        # Additional filters can be provided to this call to get a subset
        # of all registrations.
        registration_api = scorm_cloud.RegistrationApi()
        response = registration_api.get_registrations()

        # This call is paginated, with a token provided if more results exist
        registration_list = response.registrations
        while response.more is not None:
            response = registration_api.get_registrations(more=response.more)
            registration_list += response.registrations

        return registration_list

    def clean_up(self, course_id, registration_id):
        """
        Deletes all of the data generated by this sample.
        This code is run even if the program has errored out, providing a
        "clean slate" for every run of this sample.

        It is not necessary to delete registrations if the course
        they belong to has been deleted. Deleting the course will
        automatically queue deletion of all registrations associated with
        the course. There will be a delay between when the course is deleted
        and when the registrations for the course have been removed. The
        registration deletion has been handled here to prevent scenarios
        where the registration hasn't been deleted yet by the time the
        sample has been rerun.

        :param course_id: Id of the course to delete.
        :type course_id: str
        :param registration_id: Id of the registration to delete.
        :type registration_id: str
        """

        # (Optional) Further authenticate via OAuth token access
        # self.__configure_oauth([ "delete:course", "delete:registration" ])

        # This call will use OAuth with the "delete:course" scope
        # if configured.  Otherwise the basic auth credentials will be used
        course_api = scorm_cloud.CourseApi()
        course_api.delete_course(course_id)

        # The code below is to prevent race conditions if the
        # sample is run in quick successions.

        # This call will use OAuth with the "delete:registration" scope
        # if configured.  Otherwise the basic auth credentials will be used
        registration_api = scorm_cloud.RegistrationApi()
        registration_api.delete_registration(registration_id)


if __name__ == "__main__":
    main()

```
