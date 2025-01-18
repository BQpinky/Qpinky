from solders.keypair import Keypair


def create_wallets_sol(count: int):
    wallets = {}
    for i in range(count):
        keypair = Keypair()
        address = str(keypair.pubkey())
        private_key = str(keypair)
        wallets[address] = private_key

    with open("private_keys.txt", "w") as file:
        for key, value in wallets.items():
            file.write(f"{key}: {value}\n")


create_wallets_sol(5)

