
class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    return self.queue.pop(0)

  def is_empty(self):
    return self.queue == []

  def size(self):
    return len(self.queue)


def queue(word, time):
  customer_queue = Queue()
  cashier_1_queue = Queue()
  cashier_2_queue = Queue()

  for i in word:
    customer_queue.enqueue(i)

  for i in range(1, time+1):
    if (i - 1) % 3 == 0 and not cashier_1_queue.is_empty():
      cashier_1_queue.dequeue()

    if (i - 8) % 2 == 0 and not cashier_2_queue.is_empty():
      cashier_2_queue.dequeue()

    if not customer_queue.is_empty():
      if cashier_1_queue.size() < 5:
        cashier_1_queue.enqueue(customer_queue.dequeue())
      elif cashier_2_queue.size() < 5:
        cashier_2_queue.enqueue(customer_queue.dequeue())

    print(f'{i} {customer_queue.queue} {cashier_1_queue.queue} {cashier_2_queue.queue}')


if __name__ == '__main__':
  word, time = input('Enter people and time : ').split()

  queue(word, int(time))
