class User:
    def __init__(self,id,name,email,password):
        self.id=id
        self.name=name
        self.email=email
        self.password=password
        self.accounts={}

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def add_account(self,account):
        self.accounts[account.acc_number]=account
