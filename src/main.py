# Clinical Guideline Implementation: Proteinuria Management in CKD (NICE NG203)

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
    elif acr < 30:
        return "ACR 3–29 mg/mmol"
    elif acr < 70:
        return "ACR 30–69 mg/mmol"
    else:
        return "ACR ≥ 70 mg/mmol"

def needs_sglt2(acr, has_type2, is_eligible):
    if acr >= 30 and has_type2 and is_eligible:
        return "Offer an SGLT2 inhibitor"
    elif 3 <= acr < 30 and has_type2 and is_eligible:
        return "Consider an SGLT2 inhibitor"
    return None

def run_guideline():
    acr = get_float("Enter ACR (mg/mmol): ")
    diabetes = yes_or_no("Does the patient have diabetes?")

    print("ACR classification:", classify_acr(acr))

    if diabetes:
        if acr < 3:
            print("Monitor ACR, creatinine and blood pressure annually.")
        else:
            print("Offer an ACE inhibitor or ARB (titrated to the highest licensed dose they can tolerate)")
            type2_dm = yes_or_no("Does the patient have type 2 diabetes?")
            if type2_dm:
                meets_criteria = yes_or_no("Does the patient meet criteria for SGLT2 inhibitor?")
                sglt2_result = needs_sglt2(acr, type2_dm, meets_criteria)
                if sglt2_result:
                    print(sglt2_result)

    else:
        if acr < 30:
            has_hypertension = yes_or_no("Does the patient have hypertension?")
            if has_hypertension:
                print("Offer an ACE inhibitor or ARB (titrated to the highest licensed dose they can tolerate)")
                print("Follow the NICE guideline on hypertension in adults.")
            else:
                print("Monitor in line with eGFR category.")
        elif 30 <= acr < 70:
            has_hypertension = yes_or_no("Does the patient have hypertension?")
            if has_hypertension:
                print("Offer an ACE inhibitor or ARB (titrated to the highest licensed dose they can tolerate)")
            else:
                print("Monitor eGFR and consider discussing with a nephrologist if eGFR declines or ACR increases.")
        else:
            print("Offer an ACE inhibitor or ARB (titrated to the highest licensed dose they can tolerate) and refer for specialist assessment.")

    print("Refer to NICE NG203 guideline for full context.")

if __name__ == "__main__":
    run_guideline()
