message = ['spam','ham','spam','ham','spam']

#B형
lst = [msg  for msg in message  if msg == 'spam']
print(lst)

#A형
dummy = [1 if msg == 'spam'  else 0  for msg in message]
print(dummy)