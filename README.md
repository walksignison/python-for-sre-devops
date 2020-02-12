1. Print all lines (along with line numbers) containing the string `/bin/bash` from `/etc/passwd`.
2. Get current weather information from `http://api.openweathermap.org` based on zip code passed as a command line argument. 
3. Write a client to test connectivity to a particular socket, IP address and port number to be passed in via command line. 
4. Output the Python version installed, OS version, modules in search path and total modules loaded using `sys`.
5. Reverse the content of a file and write it out to another file, command line argument should be a limit on the number of lines to reverse.
6. Write a `python` program to run any `bash` command passed to it and redirect both `stdout` and `stderr` to the output of this script. 
7. Output the count of all lines of a file passed in by name. 
8. Output the count of all lines passed into the script as `stdin` or filenames as arguments.
9. Write a `grep` program that takes in filename and pattern as command line argument and prints matching lines. 
10. Output the last line of a file passed in by name. 
11. Output the file sizes of all files in a directory passed in via the command line. 
12. Output all the lines containing a particular word. Filename and word passed in via command line. 
13. Output the contents of a particular file passed in via command line to another file with a name of your choosing (without opening and reading the file into memory. HINT: use `subprocess`).
14. Collect a specific file (i.e. `/var/output.txt`) from a list of remote machines. List of username, machine lives in a `hosts.txt`.
15. Replace a specific text string in files provided in a list. List of files provided as a file to be read in.
16. Given a list of files, return a new list containing the names of files from the first list that contain specific text. List of files provided as a comma-separated command line argument.
17. Write a script that runs a `ping www.google.com` command with a packet count passed in via command line. Print out `ping` related stats, like RTT mean, min, max and stdev.
18. Parse and print out timestamp, host and destination from the following logfile:
```
file.log

Nov 31 08:00:00 test-fe1 postfix/smtp[16669]: 7CD8E730020: to=<jon@doe.it>, relay=examplemx2.doe.it[222.33.44.555]:25, delay=0.8, delays=0.17/0.01/0.43/0.19, dsn=2.0.0, status=sent(250 ok:  Message 2108406157 accepted)
Nov 31 08:00:00 test-fe1 postfix/smtp[16669]: 7CD8E730020: removed
```
19. Create a directory named `/tmp/course/foo/bar`, copy `/tmp/course/foo` to `/tmp/course/foo2` and remove `/tmp/course/foo`.
20. Suppose you have an application running on a Linux system that has versioned releases.  The current version is pointed to with a symlink named "current", like:
```
/app/
/app/v_1/
/app/v_2/
/app/v_3/
/app/current -> /app/ver2/
```
Write a script that:

i. Keeps the 3 most recent releases

ii. Keeps the current version

iii. Deletes all other releases not covered by i. and ii. that are older than 30 days

<br />
<br />
<br />
<br />

<sub>References:

https://github.com/tuladhar/Python-for-SysAdmin-Part-I

https://github.com/ioggstream/python-course

https://github.com/endavis/sysadmin

https://github.com/Apress/pro-python-system-admin-14

https://github.com/linuxacademy/content-python-for-sys-admins

https://github.com/linuxacademy/content-python3-sysadmin</sub>


