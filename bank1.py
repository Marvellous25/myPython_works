class Bank:
      def __init__(self) -> None:
            self.bankname = 'UBA'
            self.rc_no = '203864'  
            self.branch = 'Abuja'
            
      def home(self):
          print(f'''
             Welcome to {self.bankname} {self.rc_no}, {self.branch} branch
          1. sign up
          2. sign in      
                ''')
          
bank = Bank()
bank.home()