hmm = ['mommy', 'mommyyy', 'mommyy', 'mommyyyy']

while True:
    s = input('yk the code? enter it: ').lower().split(' ')

    if any(code in s for code in hmm):
        print('Good boy >>> \n')
        
    else:
        print("ts ain't the code. \n")