# INeedACat
<p align="center">
  <img src="https://kattens-vaern.dk/sites/all/themes/kattensvaern/images/logo.png" />
</p>
The cat shelter is a highly demanded place where the few offers of adoption for flat cats run in a matterr of hours.
In a desperate race to be the fastest one to book an appointment to get the cat, this bot can help.

A RaspberryPi has the solely mission to check the website of the shelter every few minutes and check if new kitties are looking for a home.
If that is the case, it will email me.

In order to use it, provide the following information in `config.yml`:
```yaml
sender_email: xxx@gmail.com
password: abc123
receiver_mail: zzz@zzz.com
receiver_mail2: zzz@zzz.com
```

Moreover, to run the file every e.g. 5 minutes, schedule a crontab job using `crontab -e`:
```
*/5 * * * * /home/pi/Documents/Proyects/INeedACat/find_cat.sh
```
