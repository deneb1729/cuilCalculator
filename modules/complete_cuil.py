def completeCuil(previusCuil, rest):

    if rest == 0:
        return previusCuil[0:2] + previusCuil[2:] + '0'
    elif rest == 1:
        if previusCuil[0:2] == '20':
            return '23' + previusCuil[2:] + '9'
        if previusCuil[0:2] == '27':
            return '23' + previusCuil[2:] + '4'
        
    return str(previusCuil[0:2]) + str(previusCuil[2:]) + str(11 - rest)