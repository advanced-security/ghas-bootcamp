
import rstr

print('AWS_KEYID:', rstr.xeger(r'AKIA[A-Z2-7]{16}'))
print('AWS_SECRET:', rstr.xeger(r'[0-9A-Za-z/+=]{40}'))
print('DATADOG_TOKEN:', rstr.xeger(r'[a-f0-9]{32}|[a-f0-9]{40}'))
