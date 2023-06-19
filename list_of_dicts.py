messages = []

# case no past messages
past_messages = []

system_message = {'role': 'system', 'content': 'description of system role'}
current_message = {'role': 'user', 'content': 'current user question'}

messages.append(system_message)
for msg in past_messages:
    messages.append(msg)
messages.append(current_message)

print('case 0 past messages:', messages)

# case 1 past messages
messages = []
past_messages = [{'role': 'user', 'content': 'last user question'},
                 {'role': 'assistant', 'content': 'answer past question'}]

messages.append(system_message)
for msg in past_messages:
    messages.append(msg)
messages.append(current_message)

print('case 1 past messages:', messages)

# case 2 past messages
messages = []

past_messages = [{'role': 'user', 'content': '1st user question'},
                 {'role': 'assistant', 'content': '1st answer past question'},
                 {'role': 'user', 'content': '2nd user question'},
                 {'role': 'assistant', 'content': '2nd answer past question'}]

messages.append(system_message)
for msg in past_messages:
    messages.append(msg)
messages.append(current_message)

print('case 2 past messages:', messages)

