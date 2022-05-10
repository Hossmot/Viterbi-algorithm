"""
Point : Hidden cause
Chapter is Chapter 
FirstPb : Start Probability
TsPb : Transfer Probability
Emission : Outcome
EmPb : Emission Probability
VTB_FS : Viterbi First Step
VIB_LS : Viterbi Last Step
VTB_Finale : Literally.

You can empty the particular list component to adjust the number of component.

Made by Youngbo Sim
"""
def InputPoint():
    global Point
    global Chapter 
    Point = int(input('Input Point '))
    Chapter = int(input('Input Chapter '))


def InputFirstPb():
    global FirstPb
    FirstPb = []
    for i in range(Point):
        print('FirstPb :'+str(i))
        FirstPb.append(float(input('Input FirstPb ')))


def InputTsPb():
    global TsPb 
    TsPb = []
    for i in range(Point):
        print('TsPb : '+str(i))
        TsPb.append([float(input('Input TsPb ')) for j in range(Point)])


def InputEmPb():
    global EmPb 
    EmPb = []
    for i in range(Point):
        print('EmPb : '+str(i))
        EmPb.append([float(input('Input EmPb ')) for j in range(Point)])


def InputPb():
    InputFirstPb()
    InputTsPb()
    InputEmPb()
    global TotalPb
    TotalPb = FirstPb + TsPb + EmPb


def InputEm():
    global Emission
    Emission = []
    for i in range(Chapter):
        Emission.append(float(input('Input Emission' + str(i) + ' ')))


def VTB():
    global EachPointPb
    EachPointPb = []
    VTB_FS()
    VTB_LS()


def VTB_FS():
    EachPointPb.append([FirstPb[i]*EmPb[i][int(Emission[0])] for i in range(Point)])

def VTB_LS():
    for i in range(Chapter):
        if(i==0):
            pass
        else:
            EachPointPb.append([ EmPb[j][int(Emission[i])] * max([EachPointPb[i-1][k] * TsPb[k][j]for k in range(Point)])for j in range(Point)])    
        print(i)      


def VTB_Finale():
    global OutcomePoint
    global OutcomePb
    OutcomePoint = []
    OutcomePb = []
    for i in range(Chapter):
        H = max(EachPointPb[i])
        OutcomePb.append(H)
        OutcomePb
        OutcomePoint.append(EachPointPb[i].index(H))
        OutcomePoint


InputPoint()
InputPb()
InputEm()
VTB()
VTB_Finale()
print(OutcomePb)
print(OutcomePoint)
