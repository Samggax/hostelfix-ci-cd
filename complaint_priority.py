# complaint_priority.py
 
URGENT_CATEGORIES = {"electrical", "gas_leak", "water_leak"}
 
def priority_score(category: str, days_open: int) -> int:
    """Return a priority score from 1 (low) to 5 (critical)."""
    if days_open < 0:
        raise ValueError("days_open cannot be negative")
 
    base = 3 if category in URGENT_CATEGORIES else 1
    escalation = min(days_open, 3)   # every day open adds urgency, capped
    return min(base + escalation, 5)

def priority_label(score: int) -> str:

    elif score >= 3:
        return "MEDIUM"
    else:
        return "LOW"
