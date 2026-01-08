# Manual Test Plan

## Project Information
- **Project Name**:
- **Module / Feature**:
- **Test Type**: Manual (Playwright Python–aligned)
- **Prepared By**:
- **Date**:

---

## 1. Requirement Summary
Brief summary of the user story or requirements being tested.
- Business objective
- In-scope functionality
- Out-of-scope functionality

---

## 2. Assumptions & Dependencies
- Application state assumptions
- Test environment assumptions
- External system dependencies
- User roles involved

---

## 3. Risk Analysis
Identify high-risk areas such as:
- Data loss
- Security misuse
- Workflow breakage
- Performance-sensitive paths
- Integration failures

---

## 4. User Flows
Describe expected user journeys.
Each flow must include:
- Entry point
- Key actions
- System validations
- Exit condition

---

## 5. Test Scenarios & Test Cases

> All test cases must be:
> - Independent
> - Executable in any order
> - Non-duplicative
> - Clearly traceable to requirements

---

### Test Case Format (MANDATORY)

---

### **TC_01**
- **Test Scenario**:
- **Test Case Description**:
- **Test Design Technique Used**:
  1. Positive Testing: Validating the Expected Behavior

      Description: Positive testing is aimed at verifying that the system behaves as expected when given valid input. It confirms that the core functionality of the system works under normal, expected conditions.

      Test Case Generation Approach:

      Test with valid inputs that reflect real-world usage.
  
  2. Boundary Testing: Focusing on the Limits of Inputs

  Description: Boundary testing focuses on testing the limits or edges of input ranges. These are typically values at or near the boundary of what is allowed, as well as values just outside of the valid range.

  Test Case Generation Approach:

  Test values that are on the boundary (e.g., minimum, maximum values).

  Test values just below or just above the boundary.

  Useful for validating input field constraints like minimum and maximum length.
  3. Equivalence Partitioning: Grouping Inputs Into Similar Behaviors
      Description: Equivalence partitioning divides the input domain into equivalence classes. Inputs that belong to the same class are expected to produce similar results, so testing one input from each class is typically enough to verify correctness.

      Test Case Generation Approach:

      Identify valid and invalid partitions for inputs.

      Choose representative values from each partition for testing.
  4. State Transition Testing: Testing States and Transitions

  Description: State transition testing is useful for systems that have distinct states and can transition between them based on specific actions or events. It tests whether the system behaves correctly when moving from one state to another.

  Test Case Generation Approach:

  Identify all possible states of the system.

  Test all transitions between states, including valid and invalid transitions.
  5. Error Guessing: Using Experience to Guess Potential Failures

  Description: Error guessing involves using prior experience, intuition, and knowledge of common mistakes to guess where errors might occur. The goal is to test "edge cases" that might not be directly captured by the other testing techniques.

  Test Case Generation Approach:

  Test common mistakes or likely failure points based on prior experience.

  Include cases for handling unusual or unexpected input.

- **Preconditions**:
- **Steps**:
  1.
  2.
  3.
- **Test Data**:
- **Expected Result**:
- **Success Criteria**:
- **Failure Criteria**:

---

### **TC_02**
- **Test Scenario**:
- **Test Case Description**:
- **Test Design Technique Used**:
- **Preconditions**:
- **Steps**:
- **Test Data**:
- **Expected Result**:
- **Success Criteria**:
- **Failure Criteria**:

---

> Continue sequentially:
> TC_03, TC_04, TC_05 …  
> No gaps. No reuse. No trivial variations.

---

## 6. Coverage Validation Checklist

For EACH identified feature or user flow, the Planner Agent MUST generate test cases using ALL of the following lenses independently:

1. Positive / Happy Path  
2. Negative / Invalid Input  
3. Boundary Value Analysis  
4. State Transition / Workflow Order  
5. Error Guessing / Failure Conditions  

### Coverage Enforcement Rules (MANDATORY)

- Each lens MUST result in **at least one unique test case per feature**
- Where a lens naturally allows variation (e.g. boundaries, invalid inputs, state transitions),  
  the Planner Agent MUST generate **multiple test cases** to cover:
  - Different input values
  - Different failure modes
- A single test case MUST NOT combine multiple lenses

Skipping a lens is **NOT allowed**.


## 7. Notes
- Any special execution notes
- Known limitations
- Future test considerations

---

## File Persistence

After generating the complete manual test plan:

- Call the MCP tool **save_plan**
- Use:
  - `plan_name`: a short, meaningful name derived from the feature or story
  - `content`: the FULL Markdown test plan
- Do NOT display the test plan in chat after saving
- The tool call is REQUIRED for successful completion
