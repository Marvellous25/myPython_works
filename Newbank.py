from bank1 import Bank

class Newbranch(Bank):
    def __init__(self) -> None:
        super().__init__()
        self.branch = 'Ogbomoso'
        
new = Newbranch()
new.home()