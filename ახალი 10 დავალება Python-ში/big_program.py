import math

def fac(n):
  """
  ფაქტორილაი
  """
  if n == 0:
    return 1
  else:
    return n * fac(n - 1)
  
"""
  სამ რიცხვში უმცირესის პოვნა

  """

def find_smallest(x, y, z):
  
  return min(x, y, z)



def cel_to_fahr(celsius):
  """
  ცელსიუსი ფარენჰეიტში
  """
  return (celsius * 9/5) + 30

def fahr_to_cel(fahrenheit):
  """
  ფარენჰეიტი ცელსიუსში
  """
  return (fahrenheit - 30) * 5/9


def find_easy(n):
  """
  ყველა მარტივი რიცხვის პოვნა კონკრეტულ დიაპაზონში
  """
  primes = []
  for num in range(2, n+1):
    if num > 1:
      for i in range(2, num):
        if (num % i) == 0:
          break
      else:
        primes.append(num)
    
    
  return primes


def sum_num(n):
  """
  1-დან n-მდე ყველა რიცხვის ჯამი
  """
  sum = 0
  for i in range(1, n+1):
    sum += i
    
  return sum

def Arithmetic_num(n):
  """
  1-დან n-მდე ყველა რიცხვის საშუალო არითმეტიკული
  """
  sum = Arithmetic_num(n)
  Arithmetic = sum / n
  return Arithmetic

def sum_sq(n):
  """
  1-დან n-მდე ყველა რიცივის კვადრატების ჯამი
  """
  sum = 0
  for i in range(1, n+1):
    sum += i**2
    
  return sum

def sum_even_num(n):
  """
  1-დან n-მდე ყველა ლუწი რიცხვის ჯამი
  """
  sum = 0
  for i in range(2, n+1, 2):
    sum += i
    
  return sum

def gcd(x, y):
  """
  ორი რიცხვის უმცირესი საერთო ჯერადი
  """
  return x * y // math.gcd(x, y)


def spliter(n):
  """
  მოცემული რიცხვის ყველა გამყოფის პოვნა
  """
  spliter = []
  for i in range(1, n+1):
    if n % i == 0:
      spliter.append(i)
    
  return spliter
def main():
  print("რომელი გსურთ?:")
  print("1. ფაქტორული გამოთვლა")
  print("2. სამი რიცხვიდან უმცირესის პოვნა")
  print("3. ტემპერატურს შკალის კონვერტორი ცელსიუსიდან ფარენგეიტში და პირიქით")
  print("4. ყველა მარტივი რიცხვის პოვნა მოცემულ დიაპაზონში (1..n).")
  print("5. ყველა რიცხვის ჯამის პოვნა 1-დან n-მდე.")
  print("6. ყველა რიცხვის საშუალო არითმეტიკული 1-დან n-მდე")
  print("7. ყველა რიცხვის კვადრატების ჯამი 1-დან n-მდე")
  print("8. ყველა ლუწი რიცხვის ჯამი 1-დან n-მდე")
  print("9. ორი რიცხვის უმცირესი საერთო ჯერადი")
  print("10. მოცემული რიცხვის ყველა გამყოფის პოვნა.")

  choice = int(input("დააფიქსირეთ არჩევანი, ირჩიედ რიცხვი (1-10): "))

  if choice == 1:
    num = int(input("შეიყვანეთ რიცხხვი: "))
    print("ფაქტორიალი", num, "არის", fac(num))
  elif choice == 2:
    x = int(input("შეიყვანეთ პირვეი რიცხვი: "))
    y = int(input("შიყვანეთ მეორე რიცხვი: "))
    z = int(input("შეიყვანეთ მესამე რიცხვი: "))
    print("ყველაზე პატარა არის:", find_smallest(x, y, z))
  elif choice == 3:
    temp = float(input("შეიყვანეთ ტემპერატურა: "))
    scale = input("შეიყვანეთ მონაცემები(C , F ): ")
    if scale == 'C':
      converted_temp = cel_to_fahr(temp)
      print(temp, "°C უდრის", converted_temp, "°F")
    elif scale == 'F':
      converted_temp = fahr_to_cel(temp)
      print(temp, "°F უდრის", converted_temp, "°C")
  elif choice == 4:
    n = int(input("შეიყვანეთ დიაპაზონის ზედა ზღვარი: "))
    easy = find_easy(n)
    print("დიაპაზონის მარტივი რიცხვები [2,", n, "] არის:", easy)
  elif choice == 5:
    n = int(input("შეიყვანეთ დიაპაზონის ზედა ზღვარი: "))
    sum = sum_num(n)
    print("ყველა რიცხვის ჯამი 1-დან", n, "არის", sum)
  elif choice == 6:
    n = int(input("შეიყვანეთ დიაპაზონის ზედა ზღვარი: "))
    Arithmetical = Arithmetic_num(n)
    print("ყველა რიცხვის საშუალო არითმეტიკული რიცხვი 1-დან", n, "არის", Arithmetical)
  elif choice == 7:
    n = int(input("შეიყვანეთ დიაპაზონის ზედა ზღვარი: "))
    sq = sum_sq(n)
    print("ყველა რიცხვის კვადრატების ჯამი 1-დან", n, "არის", sq)
  elif choice == 8:
    n = int(input("შეიყვანეთ დიაპაზონის ზედა ზღვარი: "))
    sum_even_nume = sum_even_num(n)
    print("ყველა ლუწი რიცხვის ჯამი 1-დან", n, "არის", sum_even_nume)
  elif choice == 9:
    x = int(input("შეიყვანეთ პირველი რიცხვი: "))
    y = int(input("შეიყვანეთ მეორე რიცხვი: "))
    gcde = gcd(x, y)
    print("უსჯ", x, "-სა და", y, "ს არის", gcde)
  elif choice == 10:
    x = int(input("შეიყვანეთ რიცხვი: "))
    splite = spliter(x)
    print("-ის გამყოფები", x, "არის:", splite)


if __name__ == "__main__":
  main()
