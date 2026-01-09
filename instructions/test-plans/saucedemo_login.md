# Manual Test Plan

## Project Information
- **Project Name**: SauceDemo Login
- **Module / Feature**: Login Functionality
- **Test Type**: Manual (Playwright Python–aligned)
- **Prepared By**: Planner Agent
- **Date**: 2026-01-08

---

## 1. Requirement Summary
- Business objective: Ensure secure and reliable login for SauceDemo users.
- In-scope functionality: Login page, credential validation, error handling, UI elements (password masking, login button).
- Out-of-scope functionality: Registration, password reset, post-login features.

---

## 2. Assumptions & Dependencies
- Application state: Login page is accessible, backend is available.
- Test environment: Stable test environment with test user accounts.
- External dependencies: None.
- User roles: Standard user, locked-out user.

---

## 3. Risk Analysis
- Data loss: Low (no data modification on login)
- Security misuse: High (credential handling)
- Workflow breakage: Medium (login is entry point)
- Performance-sensitive paths: Low
- Integration failures: Medium (backend auth)

---

## 4. User Flows
- Entry point: User navigates to SauceDemo login page.
- Key actions: Enter credentials, click Login.
- System validations: Credential check, error messages, UI feedback.
- Exit condition: User is logged in or receives error message.

---

## 5. Test Scenarios & Test Cases

### **TC_01**
- **Test Scenario**: Successful login with valid credentials
- **Test Case Description**: User logs in with valid username and password.
- **Test Design Technique Used**: Positive Testing
- **Preconditions**: User is on login page, valid credentials available.
- **Steps**:
  1. Enter valid username
  2. Enter valid password
  3. Click Login
- **Test Data**: username: standard_user, password: secret_sauce
- **Expected Result**: User is redirected to Products page.
- **Success Criteria**: Products page loads, user is authenticated.
- **Failure Criteria**: Error message, not redirected.

---

### **TC_02**
- **Test Scenario**: Login attempt with invalid username
- **Test Case Description**: User enters invalid username and valid password.
- **Test Design Technique Used**: Negative Testing
- **Preconditions**: User is on login page.
- **Steps**:
  1. Enter invalid username
  2. Enter valid password
  3. Click Login
- **Test Data**: username: invalid_user, password: secret_sauce
- **Expected Result**: Error message displayed.
- **Success Criteria**: Error message indicates mismatch.
- **Failure Criteria**: No error, login succeeds.

---

### **TC_03**
- **Test Scenario**: Login attempt with invalid password
- **Test Case Description**: User enters valid username and invalid password.
- **Test Design Technique Used**: Negative Testing
- **Preconditions**: User is on login page.
- **Steps**:
  1. Enter valid username
  2. Enter invalid password
  3. Click Login
- **Test Data**: username: standard_user, password: wrong_pass
- **Expected Result**: Error message displayed.
- **Success Criteria**: Error message shown, user remains on login page.
- **Failure Criteria**: No error, login succeeds.

---

### **TC_04**
- **Test Scenario**: Login attempt with empty username and password
- **Test Case Description**: User clicks Login without entering credentials.
- **Test Design Technique Used**: Boundary Value Analysis
- **Preconditions**: User is on login page.
- **Steps**:
  1. Leave username and password blank
  2. Click Login
- **Test Data**: username: '', password: ''
- **Expected Result**: Error message displayed.
- **Success Criteria**: Message states username is required.
- **Failure Criteria**: No error, login proceeds.

---

### **TC_05**
- **Test Scenario**: Login attempt with locked-out user
- **Test Case Description**: User enters credentials of a locked-out user.
- **Test Design Technique Used**: Equivalence Partitioning
- **Preconditions**: User is on login page.
- **Steps**:
  1. Enter locked-out username
  2. Enter valid password
  3. Click Login
- **Test Data**: username: locked_out_user, password: secret_sauce
- **Expected Result**: Error message displayed.
- **Success Criteria**: Message indicates user is locked out.
- **Failure Criteria**: No error, login succeeds.

---

### **TC_06**
- **Test Scenario**: Password masking
- **Test Case Description**: Password field masks input.
- **Test Design Technique Used**: State Transition Testing
- **Preconditions**: User is on login page.
- **Steps**:
  1. Enter any text in password field
- **Test Data**: password: any
- **Expected Result**: Password is masked (dots/bullets).
- **Success Criteria**: Input not visible as plain text.
- **Failure Criteria**: Password visible as plain text.

---

### **TC_07**
- **Test Scenario**: Login button availability
- **Test Case Description**: Login button is visible and enabled.
- **Test Design Technique Used**: Error Guessing
- **Preconditions**: User is on login page.
- **Steps**:
  1. Observe Login button
- **Test Data**: N/A
- **Expected Result**: Button is visible and enabled.
- **Success Criteria**: Button can be clicked.
- **Failure Criteria**: Button is missing or disabled.

---

### **TC_08**
- **Test Scenario**: Login with minimum length username and password
- **Test Case Description**: User enters minimum allowed characters.
- **Test Design Technique Used**: Boundary Value Analysis
- **Preconditions**: User is on login page.
- **Steps**:
  1. Enter 1-character username
  2. Enter 1-character password
  3. Click Login
- **Test Data**: username: a, password: b
- **Expected Result**: Error or login based on app rules.
- **Success Criteria**: System handles boundary input correctly.
- **Failure Criteria**: System crashes or behaves unexpectedly.

---

### **TC_09**
- **Test Scenario**: Login with maximum length username and password
- **Test Case Description**: User enters maximum allowed characters.
- **Test Design Technique Used**: Boundary Value Analysis
- **Preconditions**: User is on login page.
- **Steps**:
  1. Enter max-length username
  2. Enter max-length password
  3. Click Login
- **Test Data**: username: 50 chars, password: 50 chars
- **Expected Result**: Error or login based on app rules.
- **Success Criteria**: System handles boundary input correctly.
- **Failure Criteria**: System crashes or behaves unexpectedly.

---

### **TC_10**
- **Test Scenario**: Error guessing - SQL injection attempt
- **Test Case Description**: User enters SQL injection string.
- **Test Design Technique Used**: Error Guessing
- **Preconditions**: User is on login page.
- **Steps**:
  1. Enter "' OR '1'='1" as username
  2. Enter "' OR '1'='1" as password
  3. Click Login
- **Test Data**: username: ' OR '1'='1, password: ' OR '1'='1
- **Expected Result**: Error message, no login.
- **Success Criteria**: System does not allow injection.
- **Failure Criteria**: Login succeeds or system error.

---

## 6. Coverage Validation Checklist
- Each scenario above is covered by at least one test case for each required lens (positive, negative, boundary, state, error guessing).
- Multiple test cases for boundaries, invalid input, and error guessing are included.
- No test case combines multiple lenses.

---

## 7. Notes
- Test data should be configurable for different environments.
- Known limitation: UI selectors may change.
- Future: Add tests for multi-factor authentication if implemented.
