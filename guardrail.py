from sys import argv
import debugger as debug

EXPECTED_USAGE = """
Usage: guardrail <file> <function> [options]

Generate unit tests for a specific Python function.

Arguments:
  file            Path to the Python file containing the function (e.g., foo.py)
  function        The name of the function to generate tests for

Options:
  -o, --output <path>   Specify output file name (default: test_<file>.py)
  -d, --dir <path>      Specify output directory (default: test/)
  -f, --framework <name>  Choose a testing framework (unittest, pytest) (default: pytest)
  -h, --help           Show this help message and exit

Examples:
  guardrail foo.py bar
  guardrail foo.py bar --framework unittest
  guardrail foo.py bar -o tests/test_bar.py -f pytest
"""

ACCEPTED_FILE_EXTENSIONS = ["py"]
ACCEPTED_FRAMEWORKS = ["pytest", "unittest"]

DEFAULT_OUTPUT_DIR = "test"
DEFAULT_OUTPUT_FILE_PREFIX = "test_"
DEFAULT_FRAMEWORK = "pytest"

def main():
    pass

    # Parse command line arguments
    argc = len(argv)

    if argc < 3 or (argc == 2 and (argv[1] == "-h" or argv[1] == "--help")):
        print(EXPECTED_USAGE)
        return
    
    file_name = argv[1]

    # Verify file extension
    file_extension = file_name.split(".")[-1]

    if not file_extension in ACCEPTED_FILE_EXTENSIONS:
        print("File must have one of the following file extensions:", ", ".join(["." + e for e in ACCEPTED_FILE_EXTENSIONS]))
        return

    function_name = argv[2]

    output_dir = DEFAULT_OUTPUT_DIR
    output_file = DEFAULT_OUTPUT_FILE_PREFIX + file_name
    framework = DEFAULT_FRAMEWORK

    # Parse options
    index = 3

    while index < argc:
        arg = argv[index]

        if arg == "-o" or arg == "--output":
            if index == argc - 1:
                print(EXPECTED_USAGE)
                return
            
            output_file = argv[index + 1]
            index += 2

        elif arg == "-d" or arg == "--dir":
            if index == argc - 1:
                print(EXPECTED_USAGE)
                return
            
            output_dir = argv[index + 1]
            index += 2

        elif arg == "-f" or arg == "--framework":
            if index == argc - 1:
                print(EXPECTED_USAGE)
                return
            
            framework = argv[index + 1].lower()

            if not framework in ACCEPTED_FRAMEWORKS:
                print("Framework must be one of the following:", ", ".join(ACCEPTED_FRAMEWORKS))
                return

            index += 2

        else:
            print("Unknown option:", argv[index])
            return

    debug.check_value("file_name", file_name)
    debug.check_value("function_name", function_name)
    debug.check_value("output_file", output_file)
    debug.check_value("output_dir", output_dir)
    debug.check_value("framework", framework)

    # Ensure file exists

    # Look for function in file

    # Generate test script (function: generate_tests)

    # Write returned source code to file

def generate_tests(function_src, framework):
    pass

    # Call LLM to analyze function and generate tests in framework

    # return test source code


if __name__ == "__main__":
    main()