import server
if input('Run? [Y/n] ').lower == 'y':
    server.app.run()
else:
    print('Ok, exiting now. ')
    quit()