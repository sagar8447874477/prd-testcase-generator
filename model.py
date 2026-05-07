import re

# ==================================================
# REQUIREMENT EXTRACTION
# ==================================================

def extract_requirements(prd_text):

    # Split PRD into sentences/lines
    raw_lines = re.split(r'\n|\. ', prd_text)

    requirements = []

    for line in raw_lines:

        line = line.strip()

        # Ignore small/noisy lines
        if len(line) < 15:
            continue

        # Remove bullets
        line = re.sub(r'^[-•\d.]+\s*', '', line)

        requirements.append(line)

    # Remove duplicates
    unique_requirements = []

    seen = set()

    for req in requirements:

        req_lower = req.lower()

        if req_lower not in seen:
            unique_requirements.append(req)
            seen.add(req_lower)

    return unique_requirements


# ==================================================
# TEST CASE GENERATOR
# ==================================================

def generate_test_cases(prd_text):

    requirements = extract_requirements(prd_text)

    if not requirements:
        return "No valid requirements found in PRD."

    output = ""

    test_case_counter = 1

    for req in requirements:

        req = req.strip()

        # ------------------------------------------------
        # FUNCTIONAL TEST
        # ------------------------------------------------

        output += f"""
==================================================
Test Case ID: TC_{test_case_counter:03}

Scenario:
Verify normal functionality for:
{req}

Preconditions:
- Application is running
- User has valid access

Steps:
1. Open the application
2. Navigate to the required module
3. Perform the intended action
4. Observe the system response

Expected Result:
The system should correctly execute:
{req}

Priority:
P1

Test Type:
Functional
==================================================

"""

        test_case_counter += 1

        # ------------------------------------------------
        # EDGE TEST
        # ------------------------------------------------

        output += f"""
==================================================
Test Case ID: TC_{test_case_counter:03}

Scenario:
Verify edge case handling for:
{req}

Preconditions:
- Application is operational

Steps:
1. Perform the action using boundary or empty values
2. Observe system behavior

Expected Result:
The system should handle edge cases gracefully without crashing.

Priority:
P2

Test Type:
Edge
==================================================

"""

        test_case_counter += 1

        # ------------------------------------------------
        # NEGATIVE TEST
        # ------------------------------------------------

        output += f"""
==================================================
Test Case ID: TC_{test_case_counter:03}

Scenario:
Verify invalid input handling for:
{req}

Preconditions:
- Invalid input/data is available

Steps:
1. Enter invalid data
2. Attempt the operation
3. Observe validation/error behavior

Expected Result:
The system should show proper validation or error messages.

Priority:
P0

Test Type:
Negative
==================================================

"""

        test_case_counter += 1

        # ------------------------------------------------
        # SECURITY TEST
        # ------------------------------------------------

        output += f"""
==================================================
Test Case ID: TC_{test_case_counter:03}

Scenario:
Verify unauthorized access restrictions for:
{req}

Preconditions:
- Unauthorized user/session

Steps:
1. Attempt to access restricted functionality
2. Observe system response

Expected Result:
The system should prevent unauthorized access securely.

Priority:
P0

Test Type:
Security
==================================================

"""

        test_case_counter += 1

        # ------------------------------------------------
        # VALIDATION TEST
        # ------------------------------------------------

        output += f"""
==================================================
Test Case ID: TC_{test_case_counter:03}

Scenario:
Verify validation rules for:
{req}

Preconditions:
- User is on the relevant screen

Steps:
1. Provide incomplete or malformed input
2. Submit the action
3. Observe validation response

Expected Result:
Appropriate validation rules/messages should be triggered.

Priority:
P1

Test Type:
Validation
==================================================

"""

        test_case_counter += 1

    return output