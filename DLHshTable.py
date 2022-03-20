

class Dict:
  def __init__(self, table_size = 10):
    self.table = [None] * table_size
    self.len = 0
    self.top = [None, None, None, None]

  def __getitem__(self, key):
    index = hash(key) % len(self.table)
    #print(index)
    #print(self.table)
    #print(self.top)

    current_value = self.table[index]
    #print(current_value)
    
    if current_value != None:
      while current_value != None:
        if current_value[2] == key: return current_value[3]
        current_value = current_value[1]
    else:
      raise KeyError()
      #print(1)

  def __setitem__(self, key, value):
    index = hash(key) % len(self.table)

    current_value = self.table[index]

    if current_value == None:
      current_value = [self.top, None, key, value]
      self.top[1] = current_value
      current_value[0] = self.top
      self.table[index] = current_value
      top_index = hash(self.top[2]) % len(self.table)
      self.table[top_index] = self.top
      self.top = current_value
      self.len += 1

    else:
      current_value[3] = value
      self.top = current_value[0]
      if self.top != None:
        self.top[1] = current_value
        top_index = hash(self.top[2]) % len(self.table)
        self.table[top_index] = self.top
      current_value[0] = self.top
      #top_index = hash(self.top[2]) % len(self.table)
      self.table[index] = current_value
      #self.table[top_index] = self.top
      self.top = current_value

    if self.len * 2 > len(self.table): self.resize()

  def __delitem__(self, key):
    index = hash(key) % len(self.table)
    
    current_value = self.table[index]

    if current_value != None:
      while current_value != None:
        if current_value[2] == key:
          self.top = current_value[0]
          current_value = current_value[1]
          current_value[0] = self.top
          self.top[1] = current_value
          self.table[index] = [None]
          current_index = hash(current_value) % len(self.table)
          top_index = hash(self.top) % len(self.table)
          self.table[current_index] = current_value
          self.table[top_index] = self.top
        current_value = current_value[1]
      self.top = current_value[0]
      self.len -= 1
    else:
      raise KeyError()

  def __contains__(self, key):
    index = hash(key) % len(self.table)

    current_value = self.table[index]
    if current_value != None:
      while current_value != None:
        if current_value[2] == key: return current_value[3]
        current_value = current_value[1]
    else:
      raise KeyError()

  def __len__(self):
    return self.len

  def resize(self):
    raise RunTimeError('Not Implemented')

    
    
      
    
        

