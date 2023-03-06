### Common cron syntax:

<img width="700" alt="Screenshot 2023-02-16 at 10 55 59 PM" src="https://user-images.githubusercontent.com/31228460/219571648-ffcdee08-7c6d-487c-8503-f9ff8e7e1971.PNG">

- *: Any value (e.g., * * * * * means every minute)
- */n: Every nth value (e.g., */15 * * * * means every 15 minutes)
- n: Specific value (e.g., 0 0 1 1 * means January 1st)
- -: Range of values (e.g., 0 0 * * 1-5 means every weekday at midnight)
- ,: List of values (e.g., 0 0 * * 1,3,5 means every Monday, Wednesday, and Friday at midnight)
- @yearly: Run once a year at midnight on January 1st (equivalent to 0 0 1 1 *)
- @daily: Run once a day at midnight (equivalent to 0 0 * * *)
- @hourly: Run once an hour at the start of the hour (equivalent to 0 * * * *)

- [Cron website](https://crontab.guru/)
