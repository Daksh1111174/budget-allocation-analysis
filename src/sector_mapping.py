def map_sector(ministry: str) -> str:
    social = ["Education", "Health", "Women", "Tribal", "Minority", "Labour"]
    infra = ["Railways", "Road", "Power", "Housing", "Ports", "Telecommunications"]
    defence = ["Defence", "Atomic", "Home Affairs"]

    if any(x in ministry for x in social):
        return "Social Sector"
    if any(x in ministry for x in infra):
        return "Infrastructure"
    if any(x in ministry for x in defence):
        return "Defence & Security"

    return "Economic / Other"
