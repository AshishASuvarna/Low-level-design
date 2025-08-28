from User import User
from Account import Account
from Currency import Currency
from Wallet import Wallet
from PaymentMethod import BankTransfer
from TransactionStatus import TransactionStatus

def main():
    # Step 1: Create Users and Accounts
    user1 = User("u1", "Alice", "alice@email.com", "password123")
    acc1 = Account("A1", "u1", 1000, Currency.RUPEE)
    user1.add_account(acc1)

    user2 = User("u2", "Bob", "bob@email.com", "password456")
    acc2 = Account("A2", "u2", 0, Currency.DOLLAR)
    user2.add_account(acc2)

    # Step 2: Get Wallet instance and register users
    wallet = Wallet.get_instance()
    wallet.register_users(user1)
    wallet.register_users(user2)

    # Step 3: Perform successful transfer
    print("\n--- Transfer 1: SUCCESSFUL ---")
    bank_transfer = BankTransfer("pm1", Currency.RUPEE)
    txn1 = wallet.transfer_fund("A1", "A2", 100, bank_transfer)
    print(f"Transaction Status: {txn1.get_status().name}\n")

    # Step 4: Perform failed transfer (insufficient balance)
    print("\n--- Transfer 2: FAILED (Insufficient Balance) ---")
    txn2 = wallet.transfer_fund("A1", "A2", 5000, bank_transfer)
    print(f"Transaction Status: {txn2.get_status().name}\n")

    # Step 5: Print Final Balances
    print("--- Final Balances ---")
    print(f"Alice ({acc1.get_acc_number()}): {acc1.get_balance()} {acc1.get_currency().name}")
    print(f"Bob   ({acc2.get_acc_number()}): {acc2.get_balance()} {acc2.get_currency().name}")

    # Step 6: Print All Transactions
    print("\n--- All Transactions ---")
    for txn in wallet.transaction:
        print(f"{txn.get_transaction_id()} | Status: {txn.get_status().name} | From: {txn.get_sender()} → To: {txn.get_receiver()} | Amount: {txn.get_amount()} {txn.get_currency().name}")

if __name__ == "__main__":
    main()
