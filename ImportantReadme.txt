Regular Selenium Code:
"Project Selenium/ProjecTest.py" is regular selenium code that performs the tasks required
to run this via pycharm install required dependencies via project Settings in pycharm namely "Selenium"

Using Behave Framework(BDD):
"feature/myfeature.feature" is a feature file
"steps/steps.py" is the implementation of the code

to run this via pycharm install required dependencies via project Settings in pycharm namely "Selenium, behave, allure-behave, Gherkin"
use the following cmd to run the code in behave:
 
"behave Project Selenium\feature\myfeature.feature"
if want to generate report use the following CMDs in order:

1. "behave -f allure_behave.formatter:AllureFormatter -o '\Project Selenium\reports' '\Project Selenium\feature\myfeature.feature'

2. "allure serve '\Project Selenium\reports\"

I have pushed a report from my side of generation in reports folder 
