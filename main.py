from helper import *

username = input("\nEnter Username\n")
password = input("\nEnter Password\n")
gcpid = input("\nEnter GCP Project ID\n")

#print(username,password,gcpid)

print("\nStarting browser....")

web = webDriver()

web.googleLogin(username,password)
web.openConsole()
web.openProject(gcpid)
