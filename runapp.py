import subprocess

inp = open("app.in", "r")
otp = open("app.out", "w")

subprocess.call("./app", stdout=otp, stdin=inp)
