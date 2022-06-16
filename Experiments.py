def LFSR():
      # Two states
      #state1 = 0b01000100001100010110011110011000
      #state2 = 0b01110001111011100010011100000000
      #state1 = 0b11001100001001011110001000110000
      #state2 = 0b01110100100000110000000101001011
      #state1 = 0b01101101001101110001101000101011
      #state2 = 0b00111001111100101000111100001110
      #state1 = 0b11111100011111101001010001101011
      #state2 = 0b00000111100000011110001101111010
      #state1 = 0b11000000111111011000010001110111
      #state2 = 0b10001101100111000101100011011010
      newState = ""

      for i in range(10000):
        # XOR gate to get last bit
        newState += str((state1 & 1)^(state2 & 1))
        
        # Shift to the right
        newbit1 = (state1 ^ (state1 >> 1) ^ (state1 >> 7)) & 1
        newbit2 = (state2 ^ (state2 >> 1) ^ (state2 >> 7)) & 1
        
        # Add new bit
        state1 = (state1 >> 1) | (newbit1 << 31)
        state2 = (state2 >> 1) | (newbit2 << 31)
      
      return newState

def binaryDist(newState):
      i = 0
      distDict = {}
      
      # Go through newState, incrementing the respective map key value
      # for every 1 and 0
      for i in range(0, len(newState)):
        # Add new pair or increment existing pair
        if newState[i] in distDict:
          distDict[newState[i]] += 1
        else:
          distDict[newState[i]] = 1
        
        i += 1
        
      return distDict
    
def longestRun(newState):
      # Seperate loops for easier understanding
      # variables to look for
      one = '1'
      zero = '0'
  
      # Longest Run of Character in String using loop
      # First start with 1's
      res1 = 0
      cnt1 = 0

      # Map for tracking the number of zero's within the range 3 < 0 < 7
      runCount0 = {
          4: 0,
          5: 0,
          6: 0,
      }

      for chr1 in newState:
          if chr1 == one:
              cnt1 += 1
          else:
              if (cnt1 > 3 ) and (cnt1 < 7):
                    runCount0[cnt1] += 1
              res1 = max(res1, cnt1)
              cnt1 = 0
      res1 = max(res1, cnt1)
      
      # Now with 0's
      res2 = 0
      cnt2 = 0

      # Map for tracking the number of one's within the range 3 < 1 < 7
      runCount1 = {
          4: 0,
          5: 0,
          6: 0,
      }

      for chr2 in newState:
          if chr2 == zero:
              cnt2 += 1
          else:
              if (cnt2 > 3 ) and (cnt2 < 7):
                    runCount1[cnt2] += 1
              res2 = max(res2, cnt2)
              cnt2 = 0
      res2 = max(res2, cnt2)
      
      # Add counters to dictionary to use in next part
      runDict = {}
      runDict[1] = res1
      runDict[0] = res2

      return runDict, runCount0, runCount1
    
def numberOfLongestRun(runCount0, runCount1):
      print("Part 3 for 0's",runCount0)

      print("Part 3 for 1's", runCount1)
                
def main():
  newState = LFSR()
  #print("NewState: ", newState)
  
  distDict = binaryDist(newState)
  print("Number of 0's: ", distDict["0"])
  print("Number of 1's: ", distDict["1"])
  
  runDict, runCount0, runCount1 = longestRun(newState)
  print("Longest run of 0: ", runDict[0])
  print("Longest run of 1: ", runDict[1])
  
  numberOfLongestRun(runCount0, runCount1)
  
if __name__ == "__main__":
    main()