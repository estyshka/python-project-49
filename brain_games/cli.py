def welcome_user():
    import prompt
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)