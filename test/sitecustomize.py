
'''Setup testing entry point for the following:
    * Add gevent exception workaround'''

# Prevent gevent monkeypatching used on lib/storage/s3 to throw KeyError
# exception. Should be loaded as early as posible:
#   http://stackoverflow.com/questions/8774958
import gevent.monkey
gevent.monkey.patch_thread()
