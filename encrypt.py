import sys
shift = int(sys.argv[1])
msg_list = sys.stdin.readlines()
message = "".join(el for el in msg_list)

def encrypt(msg,num):
    
    output = ""
    msg = msg.upper()

    for i in range(len(msg)):
        char = msg[i]

        if (char.isalpha()):
            output += chr((ord(char) + num-65) % 26 + 65)

    final_out = ""

    for i in range(0, len(output), 5):

        final_out += output[i:i+5] + " "
        
    for i in range(0, len(final_out), 60):
      
      print(final_out[i:i+60])

    return final_out
  
  
encrypt(message,shift)