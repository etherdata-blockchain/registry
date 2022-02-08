import os
from subprocess import run, getoutput


# run docker create password command
def create_pass(username, password):
    # run htpasswd command
    # docker run --entrypoint htpasswd httpd:2 -Bbn testuser testpassword > auth/htpasswd
    run(["docker", "run", "--entrypoint", "htpasswd", "httpd:2", "-Bbn",
        username, password], stdout=open("auth/htpasswd", "w"))


# create auth folder if not exist
def create_auth_folder():
    # run command
    run(["mkdir", "-p", "auth"])


# check if htpasswd file exist, and return True if exist
def check_htpasswd_file():
    if os.path.isfile("./auth/htpasswd"):
        return True
    return False

# get username and password from user


def get_username_password():
    username = input("Username: ")
    password = input("Password: ")
    return username, password


# main function
def main():
    # create auth folder if not exist
    create_auth_folder()

    # create htpasswd file if not exist
    if not check_htpasswd_file():
        username, password = get_username_password()
        create_pass(username, password)
    else:
        print("File already exist")
        # delete file if user want to overwrite
        if input("Do you want to overwrite? (y/n): ") == "y":
            username, password = get_username_password()
            create_pass(username, password)


if __name__ == "__main__":
    main()
