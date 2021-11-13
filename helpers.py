def budget_to_location(budget: str, location: str) -> str:
    if budget == "$$$":
        if location == "city":
            return "dubai"
        elif location == "wilderness":
            return "ooty"
        else:
            return "cape_town"
    elif budget == "$$":
        if location == "city":
            return "new_york"
        elif location == "wilderness":
            return "yosemite"
        else:
            return "miami"
    else:
        if location == "city":
            return "charlotte"
        elif location == "wilderness":
            return "boone"
        else:
            return "wilmington"
