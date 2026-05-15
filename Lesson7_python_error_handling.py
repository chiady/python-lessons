# Lesson 7: Error Handling in Python
#
# Topics covered:
#   - simple print-based error reporting
#   - using the logging package
#   - try / except
#   - catching specific exceptions
#   - catching multiple exceptions
#   - else clause
#   - finally clause
#   - raising exceptions
#   - re-raising exceptions
#   - custom exception classes
#   - assertions
#   - exception chaining (raise ... from ...)


##################### Part One: Simple print() Error Reporting #######################

# The simplest way to report an error is to just print a message.
# This is fine for small scripts, learning exercises, or quick debugging.
# For real applications, prefer the 'logging' module (see Part Two) because:
#   - print() always goes to stdout - logging can go to files, the console, etc.
#   - print() has no severity levels - logging has DEBUG / INFO / WARNING / ERROR / CRITICAL
#   - print() can't easily be turned off - logging has configurable levels
#   - print() doesn't include timestamps or context - logging does

try:
    x = 10 / 0
except ZeroDivisionError as err:
    print(f"ERROR: division failed - {err}")

# You can also send errors to stderr (the standard error stream)
# instead of stdout. This is slightly more "correct" for error messages.
import sys
try:
    x = int("not a number")
except ValueError as err:
    print(f"ERROR: bad input - {err}", file=sys.stderr)


##################### Part Two: The 'logging' Package ################################

# Python's built-in 'logging' module is the standard way to report errors and
# diagnostic information in real applications. It's much more flexible than print().
#
# Severity levels (from least to most severe):
#   - DEBUG    --> detailed info, useful only when diagnosing problems
#   - INFO     --> confirmation that things are working as expected
#   - WARNING  --> something unexpected happened, but the program still works
#   - ERROR    --> a serious problem - some functionality failed
#   - CRITICAL --> a very serious error - the program may not be able to continue

import logging

# Basic configuration: set the minimum level and the message format.
# Anything below the configured level will be ignored.
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# The five severity levels in action
logging.debug("This is a debug message - very detailed.")
logging.info("This is informational - things are fine.")
logging.warning("This is a warning - something unusual happened.")
logging.error("This is an error - something failed.")
logging.critical("This is critical - the program may stop.")

# Logging an exception inside an except block
try:
    x = 10 / 0
except ZeroDivisionError as err:
    # logging.error() just logs the message
    logging.error(f"Division failed: {err}")

    # logging.exception() logs the message AND includes the full traceback.
    # Use this when you want to know exactly where the error came from.
    logging.exception("Full traceback for the division error:")

# Best practice: create a named logger per module instead of using the root logger.
# This makes it easy to control log output for different parts of your program.
logger = logging.getLogger("Lesson7")
logger.info("This message comes from the 'Lesson7' logger.")

try:
    arr = [1, 2, 3]
    print(arr[99])
except IndexError as err:
    logger.error(f"Bad index access: {err}")


##################### Part Three: Basic try / except #################################

# A try/except block lets you "try" some code, and "catch" the error if it fails
# instead of crashing the whole program.

try:
    x = 10 / 0
except:
    print("Something went wrong (bare except - not recommended)")

# Bare 'except:' catches EVERYTHING, even things you didn't expect.
# It's almost always better to catch a specific exception type.


##################### Part Four: Catching Specific Exceptions ########################

# Catching a specific exception is safer because you only handle the case you expect.

try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

try:
    num = int("not a number")
except ValueError:
    print("That string can't be converted to an integer.")

try:
    arr = [1, 2, 3]
    print(arr[10])
except IndexError:
    print("That index doesn't exist in the array.")

try:
    print(undefined_variable)
except NameError:
    print("That variable hasn't been defined.")


##################### Part Five: Accessing the Exception Object ######################

# Use 'as' to get a reference to the exception itself.
# The exception object usually has a useful message you can print.

try:
    x = int("hello")
except ValueError as err:
    print(f"Caught a ValueError. Message: {err}")


##################### Part Six: Catching Multiple Exceptions #########################

# Option A: separate except blocks (different handling for each error type)
try:
    value = int(input_str := "42")
    result = value / 0
except ValueError:
    print("Bad input - couldn't convert.")
except ZeroDivisionError:
    print("Math error - division by zero.")

# Option B: one except block for several types (same handling for all)
try:
    x = int("not a number")
except (ValueError, TypeError, ZeroDivisionError) as err:
    print(f"Some kind of input/math error happened: {err}")


##################### Part Seven: try / except / else ################################

# The 'else' block runs ONLY if the try block did NOT raise an exception.
# Useful when you want code to run on success but not be wrapped in the try.

try:
    number = int("100")
except ValueError:
    print("Conversion failed.")
else:
    print(f"Conversion worked! Got: {number}")


##################### Part Eight: try / except / finally #############################

# The 'finally' block ALWAYS runs - whether or not an exception happened.
# Typically used for cleanup: closing files, releasing resources, etc.

try:
    f = open("nonexistent_file.txt", "r")
    contents = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("This 'finally' block always runs (cleanup goes here).")


##################### Part Nine: Full try / except / else / finally ##################

try:
    value = int("25")
except ValueError as err:
    print(f"Failed: {err}")
else:
    print(f"Success: {value}")
finally:
    print("Cleanup is done.")


##################### Part Ten: Raising Exceptions Yourself ##########################

# You can trigger an exception on purpose using 'raise'.
# This is useful when invalid input or invalid state is detected.

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age is unrealistically large")
    print(f"Age set to {age}")

try:
    set_age(-5)
except ValueError as err:
    print(f"Bad age: {err}")


##################### Part Eleven: Re-raising Exceptions #############################

# Sometimes you want to log/print info about an error, then let it keep propagating.
# Use a bare 'raise' inside an except block to re-raise the same exception.

def risky_operation():
    try:
        return 10 / 0
    except ZeroDivisionError:
        print("Logging: a division by zero happened in risky_operation")
        raise  # re-raise so the caller knows about it

try:
    risky_operation()
except ZeroDivisionError:
    print("Caller saw the re-raised ZeroDivisionError.")


##################### Part Twelve: Custom Exception Classes ##########################

# You can define your own exception types by inheriting from Exception.
# This makes your code's errors more descriptive and easier to catch selectively.

class NegativeNumberError(Exception):
    """Raised when a negative number is passed where it isn't allowed."""
    pass

class TooLargeError(Exception):
    """Raised when a number exceeds the allowed maximum."""
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError(f"Cannot take square root of negative number: {x}")
    if x > 1_000_000:
        raise TooLargeError(f"Number too large: {x}")
    return x ** 0.5

try:
    square_root(-9)
except NegativeNumberError as err:
    print(f"Custom error caught: {err}")
except TooLargeError as err:
    print(f"Custom error caught: {err}")


##################### Part Thirteen: Exception Chaining (raise ... from ...) #########

# When one exception causes another, you can chain them with 'raise X from Y'.
# This preserves the original cause for debugging.

def load_config():
    try:
        return int("not a valid config value")
    except ValueError as original_err:
        raise RuntimeError("Failed to load configuration") from original_err

try:
    load_config()
except RuntimeError as err:
    print(f"Top-level error: {err}")
    print(f"Caused by: {err.__cause__}")


##################### Part Fourteen: assert ##########################################

# 'assert' is a quick way to verify that a condition is true.
# If the condition is false, Python raises an AssertionError.
# Useful for sanity checks during development.
# WARNING: assertions can be disabled with the -O flag, so don't use them
# for input validation in production code - use raise instead.

def divide(a, b):
    assert b != 0, "Divisor must not be zero"
    return a / b

try:
    divide(10, 0)
except AssertionError as err:
    print(f"Assertion failed: {err}")


##################### Part Fifteen: The 'with' Statement (Context Managers) ##########

# The 'with' statement automatically handles cleanup, even if an exception occurs.
# It's the recommended way to work with files, locks, network connections, etc.
# You don't need a finally block - 'with' takes care of it.

try:
    with open("nonexistent_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File didn't exist - but no manual cleanup was needed thanks to 'with'.")


##################### Summary ########################################################

# - print(...)             --> simple error reporting (small scripts only)
# - logging                --> proper error reporting with levels and formatting
# - try / except           --> catch and handle errors
# - except SpecificError   --> only catch what you expect
# - except (A, B) as err   --> catch multiple types in one block
# - else                   --> runs only if try succeeded
# - finally                --> always runs (cleanup)
# - raise                  --> trigger an exception yourself
# - raise (bare)           --> re-raise inside an except block
# - class MyError(Exception) --> define custom exception types
# - raise X from Y         --> chain exceptions to preserve cause
# - assert                 --> quick sanity check (development only)
# - with ... as ...        --> automatic cleanup via context managers
