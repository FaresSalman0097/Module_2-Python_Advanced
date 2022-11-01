class Car():
    #def __init__(self,kms,lit):
    def __int__(self):
        self.kms=kms
        self.lit=lit
    def mileageOfCar(self,kms,lit):
        mileageOFTheCar = kms/lit
        print(mileageOFTheCar)
obj=Car()
obj.mileageOfCar(100,5)