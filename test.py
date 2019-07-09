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
    for i in range(len(resultList)):
      if resultList[i] == '1' and resultList[i+2] == '1' and resultList[i+1] == vl:
        result.append(resultList[i+3])
        result = ''.join(result)
        break
      elif resultList[i] == '1' and resultList[i+2] != '4':
        result.append(resultList[i+1])
        result = ''.join(result)
        break
      elif resultList[i] == '1' and resultList[i+2] == '4':
        result.append(resultList[i+1])
        result = ''.join(result)
        break
      if resultList[i] == '1' and resultList[i+2] == '1' and resultList[i+1] == vl:
        result.append(resultList[i+3])
        result = ''.join(result)
        break
      elif resultList[i] == '2' and resultList[0] == resultList[i+1]:
        continue
      elif resultList[i] == '2' and resultList[0] != resultList[i+1]:
        result.append(resultList[i+1])
        result = ''.join(result)
        break
    resultList.reverse()
    return result

def Redo(stresult, resultList):
    resultList.reverse()
    result = []
    p = 0
    p4 = 0
    p5 = 0
    for i in range(len(resultList)):
      if resultList[i] == '1' or resultList[i] == '2':
        p += 1
        break
      elif resultList[i] == '4' :
        p4 += 1
      elif resultList[i] == '5' :
        p5 += 1
    for i in range(len(resultList)):
      if p5 >= p4:
        for j in range(len(resultList)):
          if resultList[j] == '1' or resultList[j] == '2':
            result = resultList[j-1]
            resultList.reverse()
            return result
      if resultList[i] == '4':
        result = resultList[i + 1]
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
        result = Undo(stresult, resultList)
        if 'resultList' in globals():
          resultList.append(l[0])
        else:
          vl = []
          vl.append(l[0])
          resultList = vl
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
        result = Redo(stresult, resultList)
        if 'resultList' in globals():
          resultList.append(l[0])
        else:
          vl = []
          vl.append(l[0])
          resultList = vl
        resultList.append(result)
        stresult = result
    else:
      return 'Неверные данные!'
  else:
    return 'Неверно введенны данные!'
  return result


print(BastShoe('1 Привет'))
print(BastShoe('1 , мир!'))
print(BastShoe('1 ++'))
print(BastShoe('2 2'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('1 *'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('3 7'))
print(BastShoe('2 100'))
print(BastShoe('1 Привет'))
print(BastShoe('1 , мир!'))
print(BastShoe('1 ++'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('5'))
print(BastShoe('4'))
print(BastShoe('5'))
print(BastShoe('5'))
print(BastShoe('5'))
print(BastShoe('5'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('2 2'))
print(BastShoe('4'))
print(BastShoe('5'))
print(BastShoe('5'))
print(BastShoe('5'))
