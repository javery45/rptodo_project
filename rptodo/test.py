from time import sleep

s="▲►▼◄"
#s="░▒▓█"
#s="▄█▀"
#s="|/-\\"

print("Loading....", end="", flush=True)

for i in range(20):
    print(f"\b{s[i%len(s)]}", end="", flush=True)
    sleep(0.15)