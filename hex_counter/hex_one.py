import time

def hex_loop(start, end):
  for i in range(start, end):
    print(hex(i))
    time.sleep(0.01)
    
hex_loop(0,891)
