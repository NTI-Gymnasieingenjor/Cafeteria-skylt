# Tests

## Before running tests
* Make sure that the [local setup](localSetup.md) has been followed
* Run [startServer.py](../startServer.py) and keep it running during testing

## How to run tests using Selenium
* While having the project open in VS Code open the testing tab as illustrated in the image below:

    ![Test setup](../documentation/images/testSetup.jpg)

* If you are unable to find the testing tab go to "view" at the top of VS Code and press testing as shown below

    ![Open testing](../documentation/images/openTesting.jpg)
* When the testing tab is open, press the blue "Configure Python Tests" button

* Next choose "unittest" as displayed below:

    ![Unittest](../documentation/images/unittest.jpg)

* Next choose "Root directory" as displayed below:

    ![Unittest](../documentation/images/selectDirectory.png)

* Lastly choose "test*.py" so that all files beginning their name with test will be run as demonstrated below:

    ![Test naming](../documentation/images/testNaming.jpg)
    