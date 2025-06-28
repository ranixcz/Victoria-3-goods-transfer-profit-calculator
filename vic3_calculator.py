def optimal_export(basecost, S_o, B_o, S_t, B_t):
    k1 = 1 / S_t
    k2 = 1 / S_o
    A = S_t + B_t
    C = S_o - B_o
    D = k1 * A - k2 * C
    denom = 2 * (k1 + k2)
    if D <= 0 or denom == 0:
        return 0, 0
    x_opt = D / denom
    profit_max = basecost * (D**2) / (4 * (k1 + k2))
    return round(x_opt, 2), round(profit_max, 2)

def smart_number(value):
    value = value.strip().lower().replace(",", ".")
    num = float(value)
    if num == 0:
        raise ValueError
    if "." in value and num < 100:
        return round(num * 1000, 2)
    return num

def safe_input(prompt):
    while True:
        try:
            return smart_number(input(prompt).strip())
        except ValueError:
            print("Please enter a positive number.")


goods_prices = {
    # Standard goods
    "clothes": 30, "fabric": 20, "fish": 20, "furniture": 30, "grain": 20,
    "groceries": 30, "merchant marine": 50, "paper": 30, "wood": 20,

    # Luxury goods
    "automobiles": 100, "coffee": 50, "fine art": 200, "fruit": 30, "liquor": 30,
    "luxury clothes": 60, "luxury furniture": 60, "meat": 30, "opium": 50,
    "porcelain": 70, "radios": 80, "sugar": 30, "tea": 50,
    "telephones": 70, "tobacco": 40, "wine": 50,

    # Industrial goods
    "clippers": 60, "coal": 30, "dye": 40, "engines": 60, "explosives": 50,
    "fertilizer": 40, "glass": 40, "hardwood": 40, "iron": 40, "lead": 40,
    "oil": 40, "rubber": 40, "silk": 40, "steamers": 70,
    "steel": 50, "sulfur": 50, "tools": 40,

    # Military goods
    "aeroplanes": 80, "ammunition": 50, "artillery": 70, "ironclads": 80,
    "man-o-wars": 70, "small arms": 60, "tanks": 80
}
while True:
    goods_name = input("\nSelect goods: ").lower().strip()

    basecost = goods_prices.get(goods_name)
    if basecost is None:
        print("Invalid goods name. Stopping tool")
        break

    player_export = safe_input("Your market: Export: ")
    player_import = safe_input("Your market: Import: ")
    country_export = safe_input("Target market: Export: ")
    country_import = safe_input("Target market: Import: ")

    S_o = player_export
    B_o = player_export - player_import
    S_t = country_export
    B_t = country_import - country_export

    x_opt, profit = optimal_export(basecost, S_o, B_o, S_t, B_t)

    print(f"\nOptimal export: {x_opt} units")
    print(f"Maximum profit: {profit:.2f}")
