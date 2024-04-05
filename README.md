# I Need a Cat ASAP
<p align="center">
 <img src="./assets/LOGO-hjemmeside-NYT-siden1933.png" alt="Cat shelter's logo" width=20%>
</p>
Copenhagen's cat shelters are highly monitorized by desperate cat seekers who spend the whole day refreshing the website. The few offers of adoption for flat-cats get taken in a matter of hours.
In a desperate race to be the fastest one to call when a new cat is available, this bot webscraps the shelter's website and notifies me over email when a new cat is available for adoption.

A RaspberryPi running the code will have the solely mission to check if new kittens are available for adoption. If that is the case it will email me, another eager cat seeker.

In order to use it for your own cat-seeking, provide the following information in `config.yml`:
```yaml
sender_email: xxx@gmail.com
password: abc123
receiver_mail: zzz@zzz.com
```

Moreover, to run the file every, e.g., 5 minutes, schedule a crontab job in the RaspberryPi using `crontab -e`:
```
*/5 * * * * /home/pi/Documents/Proyects/INeedACat/find_cat.sh
```
