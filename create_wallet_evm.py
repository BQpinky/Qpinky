from eth_account import Account

def create_wallets_evm(count: int):
    wallets = {}
    for i in range(count):
        # Генерация нового аккаунта
        account = Account.create()
        address = account.address  # Получаем адрес аккаунта
        private_key = account.key.hex()  # Приватный ключ в формате hex
        wallets[address] = private_key

    # Сохранение адресов и приватных ключей в файл
    with open("private_keys.txt", "w") as file:
        for address, private_key in wallets.items():
            file.write(f"{address}: {private_key}\n")

# Создаем 5 кошельков
create_wallets_evm(5)
