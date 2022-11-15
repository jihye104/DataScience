#A형
message = ['spam','ham','spam','ham','spam']

lst = [msg  for msg in message  if msg == 'spam']
print(lst)

#B형
dummy = [1 if msg == 'spam'  else 0  for msg in message]
print(dummy)