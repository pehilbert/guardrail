import dspy
import debugger as debug
from dotenv import load_dotenv

load_dotenv()

gpt = dspy.LM("openai/gpt-4o-mini")
dspy.settings.configure(lm=gpt)

class GenerateFunctionTest(dspy.Signature):
    """
    Given the source code for a function, generate a full, working test script for that
    function using the given framework. The user will be responsible for importing their
    function, so do not try to do so.

    The generated output must follow the following format:

    # ============================= IMPORTS ==============================
    <import the test framework>
    # TODO: import function to test

    # ============================ TEST CASES ============================
    # Function tested: <function_name>
    # File tested: <file_name>

    <test cases>
    """
    function_src = dspy.InputField(desc="The source code of the function to test")
    framework = dspy.InputField(desc="The testing framework in which to write the tests")

    reasoning = dspy.OutputField(desc="Reason about the intent of the function, possible paths through the code, common test cases, and edge cases")
    test_src = dspy.OutputField(desc="Based on the reasoning, create a test script in the specified format. Comment test cases using information from your reasoning")

def generate_test_src(function_src, framework):
    print()
    debug.log("Generating test:")
    debug.check_value("Function source", '\n' + function_src)
    debug.check_value("Framework", framework)
    print()

    result = dspy.Predict(GenerateFunctionTest)(function_src=function_src, framework=framework)

    debug.check_value("Reasoning", result.reasoning)
    debug.check_value("Test source", '\n' + result.test_src)
    print()

    return result.test_src