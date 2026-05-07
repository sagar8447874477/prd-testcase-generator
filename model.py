import re

# ---------------- REQUIREMENT EXTRACTION ---------------- #

def extract_requirements(prd_text):

    # Split text into lines/sentences
    raw_sentences = re.split(r'\n|\.', prd_text)

    requirements = []

    for sentence in raw_sentences:

        sentence = sentence.strip()

        # Ignore very short lines
        if len(sentence) < 10:
            continue

        requirements.append(sentence)

    return requirements


# ---------------- TEST CASE GENERATION ---------------- #

def generate_test_cases(prd_text):

    requirements = extract_requirements(prd_text)

    # Safety fallback
    if not requirements:
        return "No requirements found in PRD."

    output = ""

    counter = 1

    for req in requirements:

        req_clean = req.strip()

        # FUNCTIONAL
        output += f"""
==================================================
Test Case ID: TC_{counter:03}

Scenario:
Validate functionality for:
{req_clean}

Preconditions:
- User has access to application
- System is operational

Steps:
1. Open application
2. Navigate to feature
3. Perform action
4. Observe behavior

Expected Result:
System should correctly perform:
{req_clean}

Priority:
P1

Test Type:
Functional
==================================================

"""
        counter += 1

        # EDGE
        output += f"""
==================================================
Test Case ID: TC_{counter:03}

Scenario:
Validate edge case handling for:
{req_clean}

Preconditions:
- Application is running

Steps:
1. Use boundary/empty values
2. Observe behavior

Expected Result:
Application should handle edge cases gracefully.

Priority:
P2

Test Type:
Edge
==================================================

"""
        counter += 1

        # NEGATIVE
        output += f"""
==================================================
Test Case ID: TC_{counter:03}

Scenario:
Validate invalid operations for:
{req_clean}

Preconditions:
- Invalid input is available

Steps:
1. Perform invalid action
2. Observe validation

Expected Result:
Proper error/validation message should appear.

Priority:
P0

Test Type:
Negative
==================================================

"""
        counter += 1

        # SECURITY
        output += f"""
==================================================
Test Case ID: TC_{counter:03}

Scenario:
Validate unauthorized access handling for:
{req_clean}

Preconditions:
- Unauthorized user/session

Steps:
1. Attempt restricted action
2. Observe response

Expected Result:
Unauthorized access should be blocked.

Priority:
P0

Test Type:
Security
==================================================

"""
        counter += 1

    return output
