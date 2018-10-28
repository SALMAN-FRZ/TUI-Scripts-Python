from pip.utils.appdirs import user_cache_dir  # before pip v.10

print(user_cache_dir('pip'))
print(user_cache_dir('wheel'))
