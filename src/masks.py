def get_mask_card_number(card_number: str) -> str:
    """
    :card_number номер в виде 7000792289606361
    :return номер в виде 7000 79** **** 6361
    """

    if len(card_number) != 16:
        return "Карта должна быть из 16 цифр"

    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(mask_account: str) -> str:
    """
    :mask_account номер счета в виде 73654108430135874305
    :return номер счета в виде **4305
    """
    if len(mask_account) != 20:
        return "Номер счета должен быть из 20 цифр"

    return f"**{mask_account[-4:]}"


