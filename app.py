import time
from libs.openexchange import OpenExchangeClient

APP_ID = "5825e386e5c644e1acdd2a988a71cbf0"
client = OpenExchangeClient(APP_ID)

usd_amount = 1000
start = time.time()
aud_amount = client.convert(usd_amount, "EUR", "AUD")
end = time.time()

print(end - start)
usd_amount = 1000
start = time.time()
aud_amount = client.convert(usd_amount, "EUR", "AUD")
end = time.time()

print(end - start)
usd_amount = 1000
start = time.time()
aud_amount = client.convert(usd_amount, "EUR", "AUD")
end = time.time()

print(end - start)
usd_amount = 1000
start = time.time()
aud_amount = client.convert(usd_amount, "EUR", "AUD")
end = time.time()

print(end - start)
print(f"EUR {usd_amount} is equal to {aud_amount:.2f} AUD")