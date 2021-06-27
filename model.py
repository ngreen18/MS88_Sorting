
quiz_sista = [['A'], ['D'], ['B'], ['A'], ['C'], ['A'], ['B']]
quiz_medical = [['C'], ['B'], ['A'], ['D'], ['B'], ['D'], ['A']]
quiz_smart = [['D'], ['C'], ['D'], ['B'], ['A'], ['B'], ['C']]


def compare(answers):
    global sista_count, smart_count, medical_count
    sista_count = 0
    smart_count = 0
    medical_count = 0
    for response in range(len(answers)):
        if answers[response] == quiz_sista[response]:
            sista_count+=1
        elif answers[response] == quiz_medical[response]:
            medical_count+=1
        elif answers[response] == quiz_smart[response]:
            smart_count+=1
    return sista_count, smart_count, medical_count


def house_selector():
    if sista_count > smart_count and sista_count > medical_count:
        return "You are in SISTA house! You are into art, music and love forming friendships that will stand the test of time!"
    elif smart_count > sista_count and smart_count> medical_count:
        return "You are in SMART house! You are responsible, love math and never shy away from asking for help when needed"
    elif medical_count> sista_count and medical_count> smart_count:
        return "You are in MEDICAL house! You are empathetic, love the sciences, and desire to help your community when you grow up!"
    else:
        return "Results were inconclusive. Please take quiz again"









    



    
