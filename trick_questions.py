import random
 
def main():
 
     responses = ['Yes, of course!', 'Without a doubt, yes!', 'You can count on it!',
                  'No way!', 'I don\'t think so.', 'For sure!', 'Ask me later.',
                  'I\'m not sure.', 'I can\'t tell you right now.', 'The answer is no.',
                  'Without a doubt, no.', 'Go outside and play.']
     print('*** Question and Answer ***')
     print('This program will answer your hardest questions.')
     while True:
         print('Enter 1 to have your question answered, or')
         print('      2 to quit ', end='')
         while True:
             try:
                 choice = int(input('--> '))
                 while choice < 1 or choice > 2:
                     choice = int(input('ERROR: only enter 1 or 2 --> '))
                 break
             except ValueError:
                 print('ERROR: only enter 1 or 2 ', end='')
         if choice == 1:
             input('Go ahead...think of a question. Press ENTER when you\'re ready for the answer.')
             print('The answer to your question:')
             print('   ', end='')
             answer = responses[random.randint(0, len(responses))]
             print(answer)
         if choice == 2:
             break
 
     print('Program ending. Have a superior day.')
 # call the main function
main()
