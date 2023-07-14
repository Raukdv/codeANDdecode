temp_example_1_loop_valor = {'1': '0', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '10': '9', '11': 'a', '12': 'b', '13': 'c', '14': 'd', '15': 'e', '16': 'f', '17': 'g', '18': 'h', '19': 'i', '20': 'j', '21': 'k', '22': 'l', '23': 'm', '24': 'n', '25': 'ñ', '26': 'o', '27': 'p', '28': 'q', '29': 'r', '30': 's', '31': 't', '32': 'u', '33': 'v', '34': 'w', '35': 'x', '36': 'y', '37': 'z', '38': 'A', '39': 'B', '40': 'C', '41': 'D', '42': 'E', '43': 'F', '44': 'G', '45': 'H', '46': 'I', '47': 'J', '48': 'K', '49': 'L', '50': 'M', '51': 'N', '52': 'Ñ', '53': 'O', '54': 'P', '55': 'Q', '56': 'R', '57': 'S', '58': 'T', '59': 'U', '60': 'V', '61': 'W', '62': 'X', '63': 'Y', '64': 'Z', '65': '<', '66': '=', '67': '>', '68': '@', '69': '#', '70': '%', '71': '&', '72': '+', '73': '(', '74': ')', '75': '^'}
temp_example_2_valor_loop = {'0': '1', '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '9', '9': '10', 'a': '11', 'b': '12', 'c': '13', 'd': '14', 'e': '15', 'f': '16', 'g': '17', 'h': '18', 'i': '19', 'j': '20', 'k': '21', 'l': '22', 'm': '23', 'n': '24', 'ñ': '25', 'o': '26', 'p': '27', 'q': '28', 'r': '29', 's': '30', 't': '31', 'u': '32', 'v': '33', 'w': '34', 'x': '35', 'y': '36', 'z': '37', 'A': '38', 'B': '39', 'C': '40', 'D': '41', 'E': '42', 'F': '43', 'G': '44', 'H': '45', 'I': '46', 'J': '47', 'K': '48', 'L': '49', 'M': '50', 'N': '51', 'Ñ': '52', 'O': '53', 'P': '54', 'Q': '55', 'R': '56', 'S': '57', 'T': '58', 'U': '59', 'V': '60', 'W': '61', 'X': '62', 'Y': '63', 'Z': '64', '<': '65', '=': '66', '>': '67', '@': '68', '#': '69', '%': '70', '&': '71', '+': '72', '(': '73', ')': '74', '^': '75'}

def encode(data:str, subsequence:str, expansion:int) -> str:
    code_string = ''
    #Loop to change each value to the new encode
    for character in data:
        #loop for compare actual template dict for each value given
        for key, value in temp_example_1_loop_valor.items():
            #Check if the current character it's the same as the template value and if is, change to the key (loop int)
            if character == value:
                code_string += f'{key}$'
    
    #Formating to get a better response
    if code_string.endswith("$"):
        code_string = code_string.rstrip(code_string[-1])

    print(code_string)
            
def decode(data):
    decode_string = ''
    parse_segment = data.split("$") if isinstance(data, str) else None
    
    if parse_segment:
        #Loop to change each value to the new encode
        for character in parse_segment:
            #loop for compare actual template dict for each value given
            for key, value in temp_example_2_valor_loop.items():
                #Check if the current character it's the same as the template valu and if is, change to the key 
                if character == value:
                    decode_string += f'{key}'

    print(decode_string)

encode("Hola", 23)
decode("45$26$22$11")
