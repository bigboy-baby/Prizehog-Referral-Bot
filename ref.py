import requests, random, string, threading

code = input("Referal Code: ")
am = int(input("Thread Amount: "))

def gen(code):
  while True:
    rnd = ('').join(random.choices(string.ascii_letters + string.digits, k=15))

    s = requests.Session()

    r = s.post("https://prizehog.net/api/login", data={'email': f"{rnd}@bigboyxd.tk"})
    r2 = s.post("https://prizehog.net/api/refer-user", data={'referral_code': code})

    empty = r.json()
    j = r2.json()

    if empty['success'] == True:
      if j['success'] != True:
        print(f"[{rnd}@bigboyxd.tk] Fail")
      elif j['success'] == True:
        print(f"[{rnd}@bigboyxd.tk] Success")
      else:
        print(f"[{rnd}@bigboyxd.tk] Referal Error")
    else:
      print(f"[{rnd}@bigboyxd.tk] Signup Error")   

threads = list()
for index in range(am):
  x = threading.Thread(target=gen, args=(code,))
  threads.append(x)
  x.start()
for index, thread in enumerate(threads):
  thread.join()