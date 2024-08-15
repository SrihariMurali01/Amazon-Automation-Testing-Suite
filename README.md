# **AutoPilot: Amazon Automation & Testing Suite**

## Project Overview

AutoPilot is a powerful and scalable testing suite designed to automate and validate key functionalities on Amazon's website. Utilizing the robust Page Object Model (POM) architecture, AutoPilot leverages Python and Selenium to ensure your test cases are maintainable, efficient, and easy to extend as your project evolves.

## Installation Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- ChromeDriver or the appropriate web driver for your browser

### Setup

1. Clone the repository to your local machine.

2. Navigate to the project directory.

3. Install the required Python packages using the provided `requirements.txt` file.

4. Ensure you have the correct web driver installed and configured for your browser. The `driver_config.py` file in the `config` directory may need to be adjusted according to your specific setup.

## Directory Structure

- **amazon_test_log_20240802_110936.log**: Log file containing the execution logs for the tests.
- **config**: Contains configuration files necessary for setting up the web driver.
- **main_test.py**: The main test script that executes the test cases.
- **page_objects**: Contains the Page Object Model classes used in the tests.
- **tests**: Contains the test cases.

## Configuration

### Web Driver Configuration

The `config/driver_config.py` file contains the configuration settings for the Selenium WebDriver. You may need to update the path to the driver executable and the desired browser settings according to your environment.

## Running the Tests

To run the tests, execute the `main_test.py` script. This will initialize the WebDriver and log the results to a log file.

## Page Objects

The Page Object Model is implemented in the `page_objects` directory. This directory contains classes that represent different pages or components of Amazon's website. For example, one of the classes might represent the search functionality on Amazon and would include methods to interact with the search bar.

## Logging

The test execution logs are saved in the `amazon_test_log_20240802_110936.log` file. This file contains detailed information about each test run, including any errors or exceptions that occurred.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to follow the existing coding style and include appropriate tests for any new features.
