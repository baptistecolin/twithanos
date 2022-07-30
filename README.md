## 🔮 TWITHANOS 🔮

This script will soft-block\* a random half of your Twitter followers. Inspired by MCU character Thanos, who ... well you know.

NB : The selected half is built so that no mutual will be part of it. If your mutuals make up for more than half of your followers, then only your non-mutuals will be soft-blocked.

\* soft-blocking = blocking then unblocking someone, which makes them forcedly unfollow you.

### Why would you do that ??

Several reasons (non-exhaustive list)  :

* Lots of stupid people are interacting with you on an excessively frequent basis and you want this to stop
* You're just so done with this Twitter bs
* You've lost a bet with a friend
* "_Pour vivre heureux, vivons cachés_"

## Dependencies

* Python 3
* The Python libraries `json`, `twitter` and `random`

## User Manual

**WARNING : There is NO way to undo what this script does, except politely asking each softblocked person to follow you back. Be very careful what you do when manipulating this script !**

Once you've cloned this repo, create a `credentials` file next to the `twithanos.py` file. `credentials` should have the following JSON structure :

```
{
   "api_key" : "",
   "api_secret_key" : "",
   "access_token" : "",
   "access_token_secret" : ""
}
```

with each empty string filled with the appropriate [Twitter-provided API credential](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens).

Now that your `credentials` file is ready, just launch the following command :

`$ python3 twithanos.py`

The script will compute how many followers you'll lose, then list the names of all the people it has put in the death row. It will not block them right away, it will ask you to confirm if you actually want to softblock them all. Take some time to ponder your decision, take another look at the list of people that are going to get softblocked : maybe some of them are just fine and deserve to be spared ? (or maybe not)

If you're ok with this list, type `y` and the deed will be done. If you type anything else than `y`, then nothing will happen.
