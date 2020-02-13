import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
semaphore = threading.Semaphore(1)
semaphoreCo =threading.Semaphore(0)
class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'
  
  def run(self):
    global platosDisponibles
    
    while (True):
      semaphoreCo.acquire()
      try:
        logging.info('Reponiendo platos')
        platosDisponibles=3
      finally:
        semaphore.release()

class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    
    semaphore.acquire()
    try:
      if platosDisponibles==0:
        semaphoreCo.release()
        semaphore.acquire()
      self.comer()
    finally:
      semaphore.release()
  def comer(self):
    global platosDisponibles  
    platosDisponibles -= 1
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
  
platosDisponibles = 3

Cocinero().start()

for i in range(55):
  Comensal(i).start()
  
  
  
