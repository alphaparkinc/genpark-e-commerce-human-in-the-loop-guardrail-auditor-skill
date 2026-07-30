from client import ECommerceHumanInTheLoopGuardrailAuditorClient

def main():
    client = ECommerceHumanInTheLoopGuardrailAuditorClient()
    res = client.audit_proposed_action({"type": "DELETE_KEYWORD_CAMPAIGN", "keyword": "top_performer"}, 1200.0)
    print(f"Safety Status: {res['safety_status']}")
    print(f"Requires Human Approval: {res['requires_human_approval']}")
    print(f"Risk Assessment: {res['risk_assessment']}")

if __name__ == "__main__":
    main()
