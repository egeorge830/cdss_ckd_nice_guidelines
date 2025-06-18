# Clinical Guideline Implementation: Proteinuria Management in CKD
# With basic input validation

def yes_or_no(prompt):
    answer = input(prompt + " (yes/no): ")
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        print("Invalid input")
        return yes_or_no(prompt)

def get_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input")
        return get_float(prompt)

def classify_acr(acr):
    if acr < 3:
        return "ACR < 3 mg/mmol"
    elif acr >= 3 and acr < 30:
        return "ACR 3–29 mg/mmol"
    elif acr >= 30 and acr < 70:
        return "ACR 30–69 mg/mmol"
    else:
        return "ACR ≥ 70 mg/mmol"

def needs_sglt2(acr, has_type2, is_eligible):
    if acr >= 30 and has_type2 and is_eligible:
        return "Offer SGLT2 inhibitor"
    elif acr >= 3 and acr < 30 and has_type2 and is_eligible:
        return "Consider SGLT2 inhibitor"
    return None

def proteinuria_recommendation(acr, has_hypertension):
    if acr >= 70:
        return "Offer ACE inhibitor or ARB and refer to specialist"
    elif acr >= 30 and acr < 70:
        if has_hypertension:
            return "Offer ACE inhibitor or ARB"
        else:
            return "Monitor eGFR and consider nephrologist if eGFR declines or ACR increases"
    elif acr >= 3 and acr < 30:
        if has_hypertension:
            return "Offer ACE inhibitor or ARB"
        else:
            return "Monitor eGFR and consider discussing with nephrologist if eGFR declines or ACR increases"
    else:
        return "Monitor in line with eGFR category"

def run_guideline():
    acr = get_float("Enter ACR (mg/mmol): ")
    diabetes = yes_or_no("Does the patient have diabetes?")

    print("ACR classification:", classify_acr(acr))

    if diabetes:
        print("Monitor ACR, creatinine and blood pressure annually.")
        type2_dm = yes_or_no("Does the patient have type 2 diabetes?")
        meets_criteria = yes_or_no("Does the patient meet criteria for SGLT2 inhibitor?")
        sglt2_result = needs_sglt2(acr, type2_dm, meets_criteria)
        if sglt2_result:
            print(sglt2_result)
    else:
        has_hypertension = yes_or_no("Does the patient have hypertension?")
        print(proteinuria_recommendation(acr, has_hypertension))

    print("Follow NICE guideline on hypertension in adults.")

if __name__ == "__main__":
    run_guideline()
