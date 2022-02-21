# INeedACat
<p align="center">
  <img src="https://kattens-vaern.dk/sites/all/themes/kattensvaern/images/logo.png" />
</p>
The cat shelter is a highly monitorized place by the desperate cat seekers in Copenhagen. The few offers of adoption for flat-cats run outt in a matter of hours.
In a desperate race to be the fastest one to call when a new cat is available, this bot webscraps the shelter website for changes.

A RaspberryPi running the code will have the solely mission to check if the new cats available differ from the old ones. If that is the case, it will email me, another eager cat seeker.

In order to use it for your own cat-seeking, provide the following information in `config.yml`:
```yaml
sender_email: xxx@gmail.com
password: abc123
receiver_mail: zzz@zzz.com
receiver_mail2: zzz@zzz.com
```

Moreover, to run the file every, e.g., 5 minutes, schedule a crontab job in the RaspberryPi using `crontab -e`:
```
*/5 * * * * /home/pi/Documents/Proyects/INeedACat/find_cat.sh
```
