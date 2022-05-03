class asper():
    def hpcal(Bas,Iv,Ev,Level):
        return ((2*Bas+Iv+(Ev/4)*Level)/100)+Level+10
    
    def otherstat(Bas,Iv,Ev,Level):
        return ((((2*Bas+Iv+(Ev/4))*Level)/100)+5)*1.0