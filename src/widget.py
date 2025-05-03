from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_number: str) -> str:
    """
    Функция обработки информацию
    о картах и счетах
    """
    if "Счет" in card_or_account_number:
        number = card_or_account_number.replace("Счет", "").strip()
        return "Счет " + get_mask_account(number)
    else:
        number = get_mask_card_number(card_or_account_number[-16:])
        updated_card_number = " ".join(card_or_account_number.split()[:-1]) + " " + number
        return updated_card_number


def get_date(date_str: str) -> str:
    """
    Функция обработки информаци
    о дате
    """
    date_with_dash = date_str.split("T")[0]
    date = date_with_dash.split("-")
    date[0], date[2] = date[2], date[0]
    new_date = ".".join(date)
    return new_date
