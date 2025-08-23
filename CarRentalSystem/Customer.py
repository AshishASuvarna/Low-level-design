class Customer:
    def __init__(self,dl_number,name,email):
        self.dl_number=dl_number
        self.name=name
        self.email=email

    def get_dl_number(self):
        return self.dl_number

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email
