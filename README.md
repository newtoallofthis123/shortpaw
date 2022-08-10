# ShortPaw

ShortPaw is a awesome little url shortener written using flask on the backend. This a improvement on my previous project NoobShort. I tried ajax for the first time. So, hope this feels very modern and well built. Some of my other projects are not very well styled hope you have a good time using ShortPaw. Feel free to reach out to me on Discord. Woof Woof!

# API

```python
# POST API for ShortPaw
import requests

# Normal Url
request_url = 'https://shortpaw.herokuapp.com/api'
data = {'url': 'https://netflix.com'}
# returns {'og_url': 'https://netflix.com', 'hash': 'tw28dekl', 'time':  '16:32:46 2022-01-27'}
# Custom Url

request_url = 'https://shortpaw.herokuapp.com/custom_api'
data = {'url': 'https://netflix.com', 'custom_url': 'netflix'}
# returns {'og_url': 'https://netflix.com', 'hash': 'netflix', 'time':  '16:32:46 2022-01-27'}
```
