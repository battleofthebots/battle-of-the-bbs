# Battle of the BBS

This challenge requires challengers to register an account with a Mystic BBS instance with a malicious name (e.g. "bob; bash") and then run a door/external program to command inject to a shell

## Infra

The dockerfile downloads and installs version 1.12 A48 of MysticBBS to the /mystic directory, and then patches the fresh install with a preconfigured configuration with an Admin User `admin:Four_Word_Long_Password`. It exposes an ASCII version of the BBS over telnet port 23. Commands can be sent via the telnet protocol, which is just plaintext with CRLF as a line separator. Colored ANSI output is also supported, as prompted when connected to the server.

## Building
```sh
docker build . -t battle-of-the-bbs
```
## Running
```sh
docker run -p 23:23 . -t battle-of-the-bbs
```

## Exploiting
```sh
python3 solve.py 172.17.0.2
```
The script sends the commands to create a new account named `b;bash` with a password `0`. It can only be run once, as it isn't equipped to handle logging into an already created account. To get around this limit of the PoC, you can change the username before the semicolon or you can use --command to run a reverse shell that should stay open.

## Troubleshooting

- Make sure that line endings are CRLF and not just \n
- Whenever a command is sent when using raw sockets/netcat, it is always repeated back before the response is made (hence the two .recv calls in the PoC)
- If you get no response back after multiple attempts, you might be ip banned. I can't figure out how to completely disable it, but it should only happen after multiple connections from the same IP in a minute span
