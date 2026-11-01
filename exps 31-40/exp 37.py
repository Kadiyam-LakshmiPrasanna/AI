facts = {"computer_not_starting","power_light_off"}
rules = [
    ({"computer_not_starting","power_light_off"},"check_power_supply"),
    ({"check_power_supply"},"inspect_power_cable"),
    ({"computer_overheating"},"clean_cooling_fan")
    ]
print("Initial Facts: ",facts)

while True:
    new_facts = set()
    for conditions,conclusion in rules:
        if conditions.issubset(facts) and conclusion not in facts:
            new_facts.add(conclusion)
            print("Derived: ",conclusion)

    if not new_facts:
        break
    facts.update(new_facts)
print("Final facts: ",facts)
