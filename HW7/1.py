class NoMoneyToWithdrawError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PaymentError(Exception):
    def __init__(self, message):
        super().__init__(message)


def print_accounts(accounts):
    print("Список клиентов ({}): ".format(len(accounts)))
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print("{}. {} {}".format(i, name, value))


def transfer_money(accounts_transfer, account_from, account_to, value):
    try:
        if accounts_transfer[account_from] - value < 0:
            raise NoMoneyToWithdrawError("На счете перевода недостаточно средств")
        else:
            accounts_transfer[account_from] -= value
            accounts_transfer[account_to] += value

    except PaymentError and ValueError:
        print("При переводе произошла ошибка")


if __name__ == "__main__":
    accounts_dict = {
        "Василий Иванов": 100,
        "Екатерина Белых": 1500,
        "Михаил Лермонтов": 400
    }
    print_accounts(accounts_dict)

    payment_info = {
        "account_from": "Екатерина Белых",
        "account_to": "Василий Иванов"
    }

    print("Перевод от {account_from} для {account_to}...".
          format(**payment_info))
    try:
        payment_info["value"] = int(input("Сумма = "))
    except ValueError:
        raise ValueError("Введенное значение не является целым или цифрой")

    transfer_money(accounts_dict, **payment_info)

    print("OK!")

    print_accounts(accounts_dict)
