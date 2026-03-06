Academic project developed during the M.S. in Health Informatics program at Indiana University.

# SU25_Week_4: Proteinuria Management in CKD

## Purpose
The purpose of this script is to extract condition-action rules from the NICE guideline and represent them in a structured, logical format. It translates the narrative recommendations into executable decision logic using Python, such as if-then rules, allowing the guideline’s clinical decisions to be applied and tested in a programmatic way.

## Guideline Description
This guideline focuses on the management of proteinuria in patients with chronic kidney disease (CKD) [^1]. It outlines specific recommendations based on whether the patient has diabetes or not. For patients with diabetes, decisions are made based on whether the albumin-to-creatinine ratio (ACR) is below or above 3 mg/mmol. For patients without diabetes, recommendations vary depending on ACR levels: less than 30 mg/mmol, between 30 and 70 mg/mmol, or above 70 mg/mmol.

The guideline includes actions such as monitoring ACR, creatinine, and blood pressure; prescribing medications like ACE inhibitors or ARBs; and considering SGLT2 inhibitors for managing diabetes. It also emphasizes assessing whether the patient is hypertensive and managing blood pressure accordingly. In some cases, the guideline recommends monitoring eGFR and determining whether referral to a nephrologist is needed.

## How to Run It 

1. Open the project folder in PyCharm.
2. Inside the **src** package, double-click to open the file named **main.py**.
3. Right-click anywhere in the code area of that file.
4. Choose the option Run from the list that appears.
5. The program will start running in the terminal window at the bottom.
6. Answer the questions by typing the responses such as the **ACR value** or **yes/no**.
7. Based on the answers, the program will display the recommended actions.


## Example Input/Output

### Example 1: ACR < 3 mg/mmol, no diabetes or hypertension
```text
Enter ACR (mg/mmol): 2.4
Does the patient have diabetes? (yes/no): no
ACR classification: ACR < 3 mg/mmol
Does the patient have hypertension? (yes/no): no

Output:
Monitor in line with eGFR category
```
### Example 2: ACR 3–29 mg/mmol, type 2 diabetes, eligible for SGLT2
```text
Enter ACR (mg/mmol): 4
Does the patient have diabetes? (yes/no): y'
Invalid input
Does the patient have diabetes? (yes/no): yes
ACR classification: ACR 3–29 mg/mmol

Output:
Offer an ACE inhibitor or ARB (titrated to the highest licensed dose they can tolerate)

Input:
Does the patient have type 2 diabetes? (yes/no): yes
Does the patient meet criteria for SGLT2 inhibitor? (yes/no): yes

Output:
Consider an SGLT2 inhibitor
```

### Example 3: ACR 30–69 mg/mmol, no diabetes, with hypertension
```text
Enter ACR (mg/mmol): 48
Does the patient have diabetes? (yes/no): no
ACR classification: ACR 30–69 mg/mmol
Does the patient have hypertension? (yes/no): yes

Output:
Offer ACE inhibitor or ARB (titrated to the highest licensed dose that they can tolerate)
```

### Example 4: ACR ≥ 70 mg/mmol, no diabetes, no hypertension
```text
Enter ACR (mg/mmol): 75
Does the patient have diabetes? (yes/no): no
ACR classification: ACR ≥ 70 mg/mmol

Output:
Offer ACE inhibitor or ARB (titrated to the highest licensed dose that they can tolerate) and refer for specialist assessment
```
### Example 5: ACR 30–69 mg/mmol, no diabetes, no hypertension, with invalid ACR input
```text
Enter ACR (mg/mmol): 46/
Invalid input
Enter ACR (mg/mmol): 46
Does the patient have diabetes? (yes/no): no
ACR classification: ACR 30–69 mg/mmol
Does the patient have hypertension? (yes/no): no

Output:
Monitor eGFR and consider nephrologist if eGFR declines or ACR increases
```
## Extracted Rules

### Adults with Diabetes

- IF ACR < 3 mg/mmol THEN monitor ACR, creatinine, and blood pressure annually.
- IF ACR ≥ 3 mg/mmol THEN offer an ACE inhibitor or ARB (titrated to the highest licensed dose they can tolerate).
- IF ACR ≥ 30 mg/mmol AND has type 2 diabetes AND criteria in licence are met THEN offer an SGLT2 inhibitor.
- IF ACR between 3 mg/mmol and 30 mg/mmol AND has type 2 diabetes AND criteria in licence are met THEN consider an SGLT2 inhibitor.

### Adults without Diabetes

- IF ACR < 30 mg/mmol AND no hypertension THEN monitor in line with eGFR category.
- IF ACR < 30 mg/mmol AND has hypertension THEN follow the NICE guideline on hypertension in adults.
- IF ACR between 30 and 70 mg/mmol AND no hypertension THEN monitor in line with eGFR and consider discussing with a nephrologist if eGFR declines or ACR increases.
- IF ACR between 30 and 70 mg/mmol AND has hypertension THEN offer an ACE inhibitor or ARB (titrated to the highest licensed dose that they can tolerate).
- IF ACR ≥ 70 mg/mmol THEN offer an ACE inhibitor or ARB (titrated to the highest licensed dose that they can tolerate), and refer for specialist assessment.


## Reference

[^1]: National Institute for Health and Care Excellence (NICE). (2021). *Chronic kidney disease (G1‑5, A1‑3): managing proteinuria* [Visual summary]. Available at: https://www.nice.org.uk/guidance/ng203/resources/visual-summary-chronic-kidney-disease-g15-a13-managing-proteinuria-pdf-9206256495
