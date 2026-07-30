class ECommerceHumanInTheLoopGuardrailAuditorClient:
    def audit_proposed_action(self, proposed_agent_action: dict, financial_impact_usd: float = 0.0) -> dict:
        action_type = proposed_agent_action.get("type", "").upper()
        if "DELETE" in action_type or financial_impact_usd > 500.0:
            requires = True
            risk = "HIGH_RISK: Action modifies critical keywords or exceeds financial threshold."
            status = "BLOCKED_PENDING_HUMAN_APPROVAL"
        else:
            requires = False
            risk = "LOW_RISK"
            status = "AUTO_APPROVED"
        return {
            "requires_human_approval": requires,
            "risk_assessment": risk,
            "safety_status": status
        }
