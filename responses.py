import random

# This is a list of responses that the bot will use when it is asked a question.

def handle_response(message) -> str:
  p_message = message.lower()

  if p_message == 'hello':
    return 'Hey there!'

  if p_message == 'roll':
    return str(random.randint(1, 6))

  if p_message == '!help':
    return "`Whatcha need help with?`"

  return "I didn't understand what you wrote. Try typing '!help'."