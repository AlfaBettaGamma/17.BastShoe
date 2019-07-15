def is_digit(l):
    if l.isdigit():
       return True
    else:
        try:
            float(l)
            return True
        except ValueError:
            return False

def Adding(l,stresult):
  listres = stresult
  ls = []
  listres.split(stresult)
  ls.append(listres)
  ls.append(l)
  result = ''.join(ls)
  return result

def AddingFirst(l):
  result = ''.join(str(l))
  return result

def Delete(l,stresult):
  n = int(l)
  st = list(stresult)
  st.reverse()
  result = []
  for i in range(len(st)):
    if i >= n:
      result.append(st[i])
  result.reverse()
  result = ''.join(result)
  return result

def Index(l,stresult):
  n = int(l)
  st = list(stresult)
  result = ''.join(st[n - 1])
  return result


def Undo(stresult, resultList):
    resultList.reverse()
    result = []
    vl = stresult
    p = 0
    p3 = 0
    p5 = 0
    p4 = 0
    n = 0
    for i in range(len(resultList)):
      if resultList[i] == '1':
        for j in range(i,len(resultList)):
          if resultList[j] == '1':
            p += 1
          elif resultList[j] == '2':
            p += 1
          elif resultList[j] == '4':
            break
        break
      elif resultList[i] == '2' :
        for j in range(i,len(resultList)): 
          if resultList[j] == '1':
            p += 1
          elif resultList[j] == '2':
            p += 1
          elif resultList[j] == '4':
            break
        break
      elif resultList[i] == '4' :
        p4 += 1
      elif resultList[i] == '3' :
        p3 += 1
      elif resultList[i] == '5':
        p5 += 1
    if (p5+p4+p3+p)*2-1 == len(resultList):
      if p4 >= p+p5:
        resultList.reverse()
        return ''
      else:
        for j in range(len(resultList)):
          if resultList[j] == '1' or resultList[j] == '2' or resultList[j] == '5':
            n += 1
          if p4 == n :
            result = resultList[j + 1]
            break
    else:
      for i in range(len(resultList)):
        if stresult == resultList[i-1] and resultList[i] == '1' or resultList[i] == '2':
          result = resultList[i + 1]
          break
    resultList.reverse()
    return result

def Redo(stresult, resultList):
  resultList.reverse()
  result = []
  p = 0
  p4 = 0
  p5 = 0
  n = 0
  for i in range(len(resultList)):
    if resultList[i] == '1' or resultList[i] == '2':
      p += 1
      break
    elif resultList[i] == '4' :
      p4 += 1
    elif resultList[i] == '5' :
      p5 += 1
  if p5 < p4:
    for i in range(len(resultList)):
      if resultList[i] == '1' or resultList[i] == '2':
        result = stresult
      elif resultList[i] == '4':
        n += 1
      if n == p5:
        result = resultList[i + 1]
        break
  else:
    for i in range(len(resultList)):
      if resultList[i] == '1' or resultList[i] == '2':
        result = resultList[i - 1]
        break
  resultList.reverse()
  return result
              
def BastShoe(command):
  truth = False
  l = []
  l = command.split()
  if l[0] == '4' or l[0] == '5':
    if len(l) > 1:
      return 'невенрные данные!'
  result = ''
  vl = []
  global stresult
  global resultList
  if len(l) > 2:
    l.clear()
    for i in range(len(command)):
      if command[i] == ' ':
        l.append(''.join(command[i+1:len(command)]))
        break
      else:
        l.append(command[i])
  if l[0] == '1':
    if 'stresult' in globals():
      if len(stresult) == 0:
        result = AddingFirst(l[1])
        stresult = result
      else:  
        result = Adding(l[1],stresult)
        stresult = result
    else:
      result = AddingFirst(l[1])
      stresult = result
    if 'resultList' in globals():
      resultList.append(l[0])
    else:
      vl = []
      vl.append(l[0])
      resultList = vl
    if 'resultList' in globals():
      resultList.append(result)
    else:
      vl = []
      resultList = vl
      resultList.append(result)
  elif l[0] == '2':
    if 'stresult' in globals():
      truth = is_digit(l[1])
      if truth is True:
        if 'stresult' in globals():
          result = Delete(l[1],stresult)
          stresult = result
        else:
          result = ''
        if 'resultList' in globals():
          resultList.append(l[0])
        else:
          vl = []
          vl.append(l[0])
          resultList = vl
        if 'resultList' in globals():
          resultList.append(result)
        else:
          vl = []
          resultList = vl
          resultList.append(result)
      else:
        return 'Для удаления нужно указать число! Неверные данные!'
    else:
      return 'Неверные данные!'
  elif l[0] == '3':
    if 'stresult' in globals():
      truth = is_digit(l[1])
      if truth is True:
        if 'stresult' in globals():
          if len(stresult) > 0:
            result = Index(l[1],stresult)
            stresult = result
          else:
            return ''
        else:
          result = ''
        if 'resultList' in globals():
          resultList.append(l[0])
        else:
          vl = []
          vl.append(l[0])
          resultList = vl
        resultList.append(result)
      else:
        return 'Нужно указать число! Неверные данные!'
    else:
        return 'Неверные данные!'
  elif l[0] == '4':
    if 'stresult' in globals():
      if len(resultList) == 3:
        result = ''
        stresult = result
      else:      
        if 'resultList' in globals():
          resultList.append(l[0])
        else:
          vl = []
          vl.append(l[0])
          resultList = vl
        result = Undo(stresult, resultList)
        resultList.append(result)
        stresult = result
    else:
      result = 'Неверные данные!'
  elif l[0] == '5':
    if 'stresult' in globals():
      if len(resultList) == 3:
        result = ''
        stresult = result
      else:
        if 'resultList' in globals():
          resultList.append(l[0])
        else:
          vl = []
          vl.append(l[0])
          resultList = vl
        result = Redo(stresult, resultList)
        resultList.append(result)
        stresult = result
    else:
      return 'Неверные данные!'
  else:
    return 'Неверно введенны данные!'
  return result