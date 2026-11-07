
def parse_plan(text):
    if not isinstance(text, str):
        return "Invalid", 0.0

    if ":" not in text:
        return "Invalid", 0.0

    parts = text.split(":")

    if len(parts) != 2:
        return "Invalid", 0.0

    plan, gb = parts

    if not plan.strip() or not gb.strip():
        return "Invalid", 0.0

    try:
        gb = float(gb)
    except ValueError:
        return "Invalid", 0.0

    if gb < 0:
        return "Invalid", 0.0

    return plan.strip().title(), gb


def usage_average(usage_csv):
    if not isinstance(usage_csv, str) or not usage_csv.strip():
        return 0

    try:
        values = [int(r.strip()) for r in usage_csv.split(",")]
    except ValueError:
        return 0

    if not values:
        return 0

    if any(value < 0 for value in values):
        return 0

    return sum(values) // len(values)


def payable_bill(text):
    if not isinstance(text, str):
        return 0.0

    if "|" not in text:
        return 0.0

    parts = text.split("|")

    if len(parts) != 2:
        return 0.0

    bill, discount = parts

    if not bill.strip() or not discount.strip():
        return 0.0

    try:
        bill = float(bill)
        discount = float(discount)
    except ValueError:
        return 0.0

    if bill < 0 or discount < 0:
        return 0.0

    total = bill * 1.18 - discount

    return max(total, 0)


def main():
    print("==== Running parse_plan ====")
    user_input = input(
        "Enter plan:data in GB (e.g. standard:5): "
    )
    result = parse_plan(user_input)
    print("Plan and Data:", result)

    print("\n==== Running usage_average ====")
    user_input = input(
        "Enter daily usage in MB as CSV (e.g. 300,450,800): "
    )
    result = usage_average(user_input)
    print("Average Usage:", result)

    print("\n==== Running payable_bill ====")
    user_input = input(
        "Enter bill|discount (e.g. 399|50): "
    )
    result = payable_bill(user_input)
    print("Payable Bill:", result)


if __name__ == "__main__":
    main()
