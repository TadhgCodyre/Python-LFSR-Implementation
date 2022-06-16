def LFSR():
      # Two states
      state1 = 0b11001010110011001010011010110010
      state2 = 0b00110110111100101001010010011010
      newState = ""

      for i in range(20):
        # XOR gate to get last bit
        newState += str((state1 & 1)^(state2 & 1))
        
        # Shift to the right
        newbit1 = (state1 ^ (state1 >> 1) ^ (state1 >> 7)) & 1
        newbit2 = (state2 ^ (state2 >> 1) ^ (state2 >> 7)) & 1
        
        # Add new bit
        state1 = (state1 >> 1) | (newbit1 << 31)
        state2 = (state2 >> 1) | (newbit2 << 31)
      
      return newState 
                
def main():
  newState = LFSR()
  print("NewState: ", newState)
  
if __name__ == "__main__":
    main()