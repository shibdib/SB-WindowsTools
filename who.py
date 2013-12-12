#!/usr/bin/env python
# !!!!!!This script was originally written by: sethdmoore!!!!!!!
# This hacky script iterates over your starbound log file and prints a list of
# of connected clients. This will work until some update changes log format

# Set this to be the full path to your log file
STARBOUND_LOGFILE = "C:\Program Files (x86)\Steam\SteamApps\common\Starbound\starbound_server.log"

# Log keywords
# connected disconnected = duh
# connection = reaped ... we delete these keys from the dict
# " " = loading ship world received from client


def main():
    clients = {}
    with open(STARBOUND_LOGFILE, 'r') as log:
        for line in log:
            # Chat begins with two spaces in the log and contains a caret.
            # Find it and strip it as we don't want to count chat
            status = line.split(':  ')
            if len(status) > 1:
                status = ""
            # Now we can detect carets as connection messages
            status = line.split('<User: ')
            if len(status) > 1:
                # Strip new lines and ending carets
                status = status[1].replace("\n", "")
                # Detect client number and set their status
                #if status.split(" ")[1] == "<User:":
                if len(status.split("> ")) > 1:
                    clients[status.split("> ")[0]] = status.split("> ")[1]

    # Clean reaped players from dictionary
    for player, status in clients.items():
        # Player's connection has been reaped, keyword connection
        if status == 'connection':
            del clients[player]
		
		#creates a file called players.txt	
	f = open('players.txt', 'w')
	    #header for players.txt
	f.write("**TITLE** \n")
    f.write("Total Connected Players: %s \n \n" % len(clients.keys()))
    for player, status in clients.iteritems():
        f.write("- %s \n" % (player))
	f.write("\n \n Updated every x minutes.")

if __name__ == '__main__':
    main()
