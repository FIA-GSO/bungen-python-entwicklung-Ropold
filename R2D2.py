
R2D2_Junge = 10
R2D2_Erwachsene = 10
R2D2_Alt = 10
NaechsteRunde = 0

def Zyklus (R2D2_Junge, R2D2_Erwachsene, R2D2_Alt):
    NaechsteRunde = (
                    R2D2_Junge = R2D2_Junge / 2
                    R2D2_Erwachsene = R2D2_Erwachsene / 3

                    R2D2_Junge = R2D2_Junge + (R2D2_Erwachsene * 4)
                    R2D2_Junge = R2D2_Junge + (R2D2_Alt * 2)
                     )
    R2D2_Alt = R2D2_Erwachsene
    R2D2_Erwachsene = R2D2_Junge
    R2D2_Junge = NaechsteRunde


    return R2D2_Junge, R2D2_Erwachsene, R2D2_Alt