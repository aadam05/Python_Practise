text = "X-DSPAM-Confidence:    0.8475"
total = text.find('0.8475')
t1 = text[23:30]
t1 = float(t1)
print(t1)