import re

def extract_requirements(prd_text):
    sentences = re.split(r'\.|\n', prd_text)

    requirements = []

    for sentence in sentences:
        sentence = sentence.strip()

        if len(sentence) > 10:
            requirements.append(sentence)

    return requirements


def generate_test_cases(prd_text):

    requirements = extract_requirements(prd_text)

    output = ""

    for idx, req in enumerate(requirements, start=1):

        output += f"""
========================================
Test Case ID: TC_{idx:03}

Scenario:
Validate that {req}

Preconditions:
- User is logged into the system
- Application is running

Steps:
1. Open the application
2. Perform the required action
3. Observe system behavior

Expected Result:
System should correctly handle: {req}

Priority:
P1

Test Type:
Functional
========================================
"""

        # Edge Case
        output += f"""
Test Case ID: TC_{idx:03}_EDGE

Scenario:
Validate edge case for {req}

Preconditions:
- Application is available

Steps:
1. Perform action with boundary/empty values
2. Observe behavior

Expected Result:
Application should gracefully handle edge conditions.

Priority:
P2

Test Type:
Edge
========================================
"""

        # Negative Case
        output += f"""
Test Case ID: TC_{idx:03}_NEG

Scenario:
Validate invalid behavior for {req}

Preconditions:
- User provides invalid input

Steps:
1. Perform invalid operation
2. Observe error handling

Expected Result:
System should show proper validation/error message.

Priority:
P0

Test Type:
Negative
========================================
"""

    return output