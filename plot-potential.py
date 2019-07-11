import matplotlib.pyplot as plt
import json

with open('bob.json') as infile:
    cache = json.load(infile)
with open('bob2.json') as infile:
    cache2 = json.load(infile)
with open('bob3.json') as infile:
    cache3 = json.load(infile)

plt.figure(1)
ax1 = plt.subplot(313)
plt.plot(cache["membrane"]['v'])
plt.title('stimulation level = 0.0')
ax2 = plt.subplot(312, sharex=ax1)
plt.plot(cache2["membrane"]['v'])
plt.title('stimulation level = 0.5')
plt.setp(ax2.get_xticklabels(), visible=False)
ax2 = plt.subplot(311, sharex=ax1)
plt.plot(cache3["membrane"]['v'])
plt.title('stimulation level = 1.0')
plt.setp(ax2.get_xticklabels(), visible=False)

plt.figure(2)
plt.plot(cache["membrane"]['v'], label='0.0')
plt.plot(cache2["membrane"]['v'], label='0.5')
plt.plot(cache3["membrane"]['v'], label='1.0')
plt.legend()
plt.show()